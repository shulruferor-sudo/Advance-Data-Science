from __future__ import annotations

import json
import os
import time
import warnings
from pathlib import Path

os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['CBS_OCCUPATION_WORKBOOK_PATH'] = '/mnt/data/DUMMY_DATASET.xlsx'

import numpy as np
import pandas as pd
from scipy.sparse import issparse
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import StratifiedGroupKFold
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

experiment_directory = Path('/mnt/data/occupation_classification_v10_evidence')
experiment_directory.mkdir(exist_ok=True)
source_directory = Path('/mnt/data/occupation_classification_v9_evidence')
source_notebook = Path('/mnt/data/occupation_classification_full_evidence_final_training_v7.ipynb')
selected_text_column = os.environ['V10_COLUMN']
output_directory = experiment_directory / selected_text_column
output_directory.mkdir(exist_ok=True)


class CatBoostMulticlassAdapter(ClassifierMixin, BaseEstimator):
    def __init__(self, iterations=100, depth=6, learning_rate=None, l2_leaf_reg=3, random_strength=1, random_seed=42):
        self.iterations = iterations
        self.depth = depth
        self.learning_rate = learning_rate
        self.l2_leaf_reg = l2_leaf_reg
        self.random_strength = random_strength
        self.random_seed = random_seed

    def fit(self, training_features, training_labels):
        self.classes_ = np.unique(training_labels)
        model_parameters = dict(iterations=self.iterations, depth=self.depth, l2_leaf_reg=self.l2_leaf_reg, random_strength=self.random_strength, random_seed=self.random_seed, loss_function='MultiClass', verbose=False, thread_count=1, allow_writing_files=False)

        if self.learning_rate is not None:
            model_parameters['learning_rate'] = self.learning_rate

        self.fitted_classifier_ = CatBoostClassifier(**model_parameters)
        training_matrix = training_features.toarray() if issparse(training_features) else training_features
        self.fitted_classifier_.fit(training_matrix, training_labels)
        return self

    def predict_proba(self, prediction_features):
        prediction_matrix = prediction_features.toarray() if issparse(prediction_features) else prediction_features
        return self.fitted_classifier_.predict_proba(prediction_matrix)

    def predict(self, prediction_features):
        return self.classes_[np.argmax(self.predict_proba(prediction_features), axis=1)]


def construct_soft_voting_classifier(selected_parameters=None):
    model_parameters = selected_parameters or {}

    forest_parameters = dict(model_parameters.get('RandomForestClassifier', {}))
    xgboost_parameters = dict(model_parameters.get('XGBClassifier', {}))
    lightgbm_parameters = dict(model_parameters.get('LGBMClassifier', {}))
    catboost_parameters = dict(model_parameters.get('CatBoostClassifier', {}))
    logistic_parameters = dict(model_parameters.get('LogisticRegression', {}))

    return VotingClassifier(estimators=[
        ('random_forest', RandomForestClassifier(**forest_parameters, random_state=42, n_jobs=1)),
        ('xgboost', XGBClassifier(**xgboost_parameters, random_state=42, n_jobs=1, verbosity=0)),
        ('lightgbm', LGBMClassifier(**lightgbm_parameters, random_state=42, n_jobs=1, verbosity=-1)),
        ('catboost', CatBoostMulticlassAdapter(**catboost_parameters, random_seed=42)),
        ('logistic', LogisticRegression(**logistic_parameters, max_iter=1000, random_state=42)),
    ], voting='soft', n_jobs=1)


notebook_json = json.loads(source_notebook.read_text())
context = {'__name__': '__main__'}

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    for original_cell_number in (2, 4, 6, 8, 22):
        original_cell_source = ''.join(notebook_json['cells'][original_cell_number]['source'])
        exec(compile(original_cell_source, f'preserved_v7_cell_{original_cell_number}', 'exec'), context)

column_summaries = pd.read_csv(source_directory / selected_text_column / 'every_parameter_candidate_summary.csv')
column_summaries = column_summaries.loc[column_summaries['completed_folds'].eq(10)].copy()
column_summaries = column_summaries.sort_values(['mean_macro_f1', 'mean_macro_recall', 'std_fold_macro_f1'], ascending=[False, False, True])
selected_representation_path = column_summaries.iloc[0]['representation_path']
representation_config = next(config for config in context['EVALUATED_TEXT_ENCODING_PATHS'] if config['path_name'] == selected_representation_path)
model_families = ['RandomForestClassifier', 'XGBClassifier', 'LGBMClassifier', 'CatBoostClassifier', 'LogisticRegression']
selected_parameters = {}

for model_family in model_families:
    model_candidates = column_summaries.loc[column_summaries['representation_path'].eq(selected_representation_path) & column_summaries['classifier_name'].eq(model_family)]
    assert len(model_candidates) == 2
    selected_parameters[model_family] = json.loads(model_candidates.iloc[0]['candidate_parameters'])

configuration_manifest = {
    'occupational_text_column': selected_text_column,
    'representation_path': selected_representation_path,
    'constituent_model_types': model_families,
    'default_model_parameters': {'random_state': 42},
    'independently_optimized_model_parameters': selected_parameters,
    'seed': 42,
    'number_of_cross_validation_folds': 10,
    'selection_source': 'V9 full development cross-validation',
    'selection_bias_notice': 'Parameter and representation choices used development labels; these fold scores are not nested-CV estimates.',
}
(output_directory / 'selected_model_parameters.json').write_text(json.dumps(configuration_manifest, ensure_ascii=False, indent=2))

training_inputs = context['training_model_inputs']
training_labels = context['training_occupation_codes'].astype(str).to_numpy()
participant_groups = context['training_description_groups']
validation_splits = list(StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=42).split(training_inputs, training_labels, participant_groups))

metric_records = []
prediction_records = []
exception_records = []

for fold_number, (training_positions, validation_positions) in enumerate(validation_splits, start=1):
    training_features, validation_features, _, selected_group_count = context['transform_single_description_column_using_training_only_fits'](
        selected_text_column,
        representation_config,
        training_inputs.iloc[training_positions],
        training_inputs.iloc[validation_positions],
    )

    assert len(set(participant_groups.iloc[training_positions]) & set(participant_groups.iloc[validation_positions])) == 0
    actual_occupation_labels = training_labels[validation_positions]

    for candidate_name, candidate_parameters in [('DefaultFiveClassifierSoftVoting', None), ('OptimizedFiveClassifierSoftVoting', selected_parameters)]:
        try:
            fresh_ensemble = construct_soft_voting_classifier(candidate_parameters)
            fitting_start = time.monotonic()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                fresh_ensemble.fit(training_features, training_labels[training_positions])
                predicted_probabilities = fresh_ensemble.predict_proba(validation_features)
                predicted_occupation_labels = fresh_ensemble.predict(validation_features)

            assert np.all(np.isfinite(predicted_probabilities))
            assert np.allclose(predicted_probabilities.sum(axis=1), 1.0, atol=1e-5)
            assert set(predicted_occupation_labels).issubset(set(training_labels[training_positions]))

            metric_records.append({
                'occupational_text_column': selected_text_column,
                'representation_path': selected_representation_path,
                'ensemble_name': candidate_name,
                'validation_fold_number': fold_number,
                'number_of_validation_records': len(validation_positions),
                'selected_number_of_contextual_groups': selected_group_count,
                'macro_f1': f1_score(actual_occupation_labels, predicted_occupation_labels, average='macro', zero_division=0),
                'macro_recall': recall_score(actual_occupation_labels, predicted_occupation_labels, average='macro', zero_division=0),
                'macro_precision': precision_score(actual_occupation_labels, predicted_occupation_labels, average='macro', zero_division=0),
                'accuracy': accuracy_score(actual_occupation_labels, predicted_occupation_labels),
                'elapsed_fit_and_predict_seconds': time.monotonic() - fitting_start,
                'number_of_independently_trained_constituent_models': len(fresh_ensemble.estimators_),
            })

            for sample_position, actual_label, predicted_label, probability_vector in zip(validation_positions, actual_occupation_labels, predicted_occupation_labels, predicted_probabilities):
                prediction_records.append({
                    'occupational_text_column': selected_text_column,
                    'ensemble_name': candidate_name,
                    'validation_fold_number': fold_number,
                    'source_row_index': int(training_inputs.index[sample_position]),
                    'actual_occupation_label': actual_label,
                    'predicted_occupation_label': predicted_label,
                    'maximum_predicted_class_probability': float(max(probability_vector)),
                })

            print('COMPLETED', selected_text_column, candidate_name, fold_number, round(metric_records[-1]['elapsed_fit_and_predict_seconds'], 2), flush=True)

        except Exception as model_exception:
            exception_records.append({
                'occupational_text_column': selected_text_column,
                'ensemble_name': candidate_name,
                'validation_fold_number': fold_number,
                'error_type': type(model_exception).__name__,
                'error_message': str(model_exception),
            })
            print('FAILED', selected_text_column, candidate_name, fold_number, repr(model_exception), flush=True)

        pd.DataFrame(metric_records).to_csv(output_directory / 'each_ensemble_each_fold.csv', index=False)
        pd.DataFrame(prediction_records).to_csv(output_directory / 'each_ensemble_each_validation_prediction.csv', index=False)
        pd.DataFrame(exception_records, columns=['occupational_text_column','ensemble_name','validation_fold_number','error_type','error_message']).to_csv(output_directory / 'each_ensemble_exception.csv', index=False)

results = pd.DataFrame(metric_records)
assert len(results) == 20
assert not len(exception_records)
summary = results.groupby(['occupational_text_column','representation_path','ensemble_name'], as_index=False).agg(
    ten_fold_mean_macro_f1=('macro_f1','mean'),
    ten_fold_mean_macro_recall=('macro_recall','mean'),
    ten_fold_mean_accuracy=('accuracy','mean'),
    ten_fold_standard_deviation_macro_f1=('macro_f1','std'),
    completed_folds=('macro_f1','size'),
)
summary.to_csv(output_directory / 'both_ensembles_ten_fold_summary.csv', index=False)
print('SAVED', selected_text_column, summary.to_json(orient='records'), flush=True)