# Occupational classification from survey responses

[Assignment_Solution.ipynb](Assignment_Solution.ipynb) contains the complete analysis, field preparation, classifier comparison, held-out evaluation, and occupation predictions.

[Open in Colab](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/projects/Bureau%20of%20Statistics/Assignment_Solution.ipynb) · [Presentation](Assignment_Presentation.pptx)

## Data and preparation

The simulated dataset contains 200 survey records and 18 fields. The target is `SemelMishlachSofi`. There are 191 complete labels across 59 occupation classes and nine partial labels reserved for prediction. ID provides record traceability and is excluded from model inputs.

Each field has its own analysis, conclusion, and transformation. The text fields preserve confidentiality responses, expand references within the same questionnaire, and use separate TF-IDF vocabularies. LaBSE standardizes Latin-containing values in the selected fields using existing Hebrew values. Nominal categories use one-hot encoding. Management remains ordered. Years on the job use the processing date because the survey date is unavailable. The notebook states the interpretation used for each missing-value replacement.

## Classification

A description-group split reserves 38 records for a final test. Ten group folds on 153 development records compare 229 configurations, including nine individual classifier families, soft and hard voting, and a majority baseline. Vocabulary, IDF, matching candidates, numerical replacements, scaling, and clusters are fitted within each training fold. The test scores do not change the CV-selected configuration.

| Selected configuration | Result |
| --- | --- |
| Classifier | Random forest |
| TF-IDF normalization | l2 |
| Added cluster memberships | True |
| Mean validation macro F1 | 0.481 |
| Held-out accuracy | 57.9% |
| Held-out macro F1 | 0.471 |

The final model is fitted on all 191 complete labels and predicts the nine incomplete records. Predictions retain the original partial codes and distinguish unconstrained predictions from compatible alternatives. The missing digits have no verified reference labels, so those nine predictions have no reported accuracy.

## Execution

Run the notebook from top to bottom. It retrieves the workbook, loads LaBSE on the CPU, prepares the fields, evaluates the parameter grid, and displays the results. The full search performs 2,290 cross-validation fits, followed by held-out evaluation and final training. Results, figures, and fitted artifacts are written to the runtime's output folders. The reported tenure reference is 2026-11-06.

The scores measure agreement with supplied manual labels in a small simulated sample. Independently adjudicated labels, participant identifiers, submission dates, and external calibration are needed before defining an operational automation threshold.
