# Occupational classification from survey responses

[Open the analysis notebook](Assignment_Solution.ipynb) · [Run in Colab](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/projects/Bureau%20of%20Statistics/Assignment_Solution.ipynb) · [Presentation](Assignment_Presentation.pptx)

## Problem and objective

The task is to investigate questionnaire responses and assess whether they can support reliable occupational coding. The goal is not simply to predict a four-digit code: it is to understand what each answer contributes, detect inconsistent or ambiguous records, measure generalization, and identify cases requiring manual review.

The simulated workbook contains 200 records and 18 fields. The occupation target, `SemelMishlachSofi`, is complete in 191 records and partially specified in nine. The complete labels span 59 observed occupation codes, many with very few examples. These data constrain what any model comparison can establish.

## Investigation: question → evidence → decision

The notebook examines fields according to their meaning in the questionnaire, not merely their data type.

- **Work performed:** `EzoAvoda`, `TeurPeula`, and `TeurTafkid` can describe different aspects of the respondent's occupation. Their coverage, wording, and references to other answers must be examined before they become features.
- **Employer and organizational context:** `ShemAvoda`, `SugAvoda`, and department fields can provide supporting context, but an employer's activity is not the same as the respondent's occupation.
- **Coded responses:** Employment status, salary source, education, and management questions require their questionnaire definitions and routing rules. Missing, inapplicable, and contradictory responses are not interchangeable.
- **Dates and identifiers:** `ID` is a running index and is not an occupation predictor. Tenure calculated against notebook execution time is not necessarily tenure at the survey date.
- **Mixed-language text:** Hebrew and Latin spellings can fragment TF-IDF features for the same concept. LaBSE-based matching is explored as a possible normalization aid, but semantic similarity alone does not establish that two names or occupations are equivalent. Incorrect substitutions must be checked rather than accepted automatically.

The analytical question for every transformation is whether it preserves the information needed to distinguish occupations without introducing unsupported assumptions.

## Representations and models

The notebook investigates field-specific text representations, categorical and numerical features, and classifier alternatives. TF-IDF provides a sparse lexical baseline. L2 normalization controls vector magnitude; it does **not** reduce the number of features or make the representation less sparse. TruncatedSVD can compress TF-IDF into dense components, while feature selection can reduce dimensions and retain sparse inputs. Neither is automatically beneficial: alternatives should be compared using the same validation protocol.

Any learned vocabulary, IDF weights, imputation statistics, matching candidates, dimensionality reduction, or feature selection must be fitted on training data only within each validation fold. A description-group split helps test generalization beyond repeated wording, but its scores should not be interpreted as a direct numerical estimate of leakage.

## Evaluation and interpretation

The notebook contains model comparisons, held-out evaluation, and predictions for partially coded records. **The current run configuration and reported metrics must be read from the executed notebook outputs**; older README figures are not treated as current results. In particular, fold count, search size, selected model, and held-out scores can change when the notebook is edited or rerun.

Macro-F1 is important because occupation classes are unevenly represented. Accuracy remains useful but can conceal weak performance on rare classes. Results describe agreement with the provided codes in this simulated sample—not independently verified coding accuracy or production readiness.

For a partially known four-digit code, a model prediction can conflict with the digits already supplied. Compatible alternatives should be shown separately, and no accuracy can be assigned to records whose missing digits have not been independently labeled.

## Reproduction

Run [`Assignment_Solution.ipynb`](Assignment_Solution.ipynb) from top to bottom in a suitable Python/Colab environment. It may download data or models and perform computationally expensive validation. Confirm that the workbook source, package versions, random seeds, execution date, validation splits, and saved outputs correspond to the run being reported.

The notebook is an investigation and modeling demonstration. Operational use would require verified labels, representative evaluation data, explicit handling of inconsistent questionnaire answers, calibrated review rules, and monitoring of coding errors.
