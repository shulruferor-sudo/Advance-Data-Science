# Advanced Data Science

Or Shulrufer’s public workspace for advanced data science, shared datasets, reusable scientific figures, project development and scientific publication.

[Repository](https://github.com/shulruferor-sudo/Advance-Data-Science)

## Workspace

| Location | Purpose |
| --- | --- |
| `Datasets/Datasets.ipynb` | Obtain and maintain datasets independently, one dataset section at a time. |
| `Datasets/arxiv_research_papers_2020/` | All 8,836 extracted arXiv research-paper texts, source metadata and normalization records. |
| `project_notebooks/from_linguistic_context_to_semantic_structure/Proof.ipynb` | The project’s single computational notebook, including checks and displayed results. |
| `project_notebooks/from_linguistic_context_to_semantic_structure/results/` | Project-specific partitions, numerical references, predictions and checkpoints. |
| `project_notebooks/from_linguistic_context_to_semantic_structure/models/` | This project’s pretrained model files. |
| `project_python/` | Python pipelines derived from validated project notebooks; currently reserved. |
| `Figures.ipynb` | One independent notebook of reusable scientific figure generators. |
| `PDF_Creation/Projects_LaTeX/` | LaTeX manuscript sources. |
| `PDF_Creation/PDF_Creator.ipynb` | One compilation notebook with a separate execution cell for each paper. |
| `PDFs/` | Successfully compiled PDFs. |

The Unicode manuscript remains in ChatGPT Library and is not maintained in this repository. Git history preserves previous repository versions. No numbered duplicate notebooks or manuscript-generating programs are maintained.

## Shared datasets

Only `Datasets/Datasets.ipynb` downloads, normalizes, repairs or updates shared datasets. Run its setup cells and the section for the desired dataset. Every dataset has one enclosing folder named for its meaningful contents and scope, even if the upstream release contains many folders or loose files. All constituent files, metadata and provenance stay inside that enclosing folder. Reruns update the same location and reuse verified files.

The first dataset folder is `arxiv_research_papers_2020`: scientific research-paper text suitable for text mining and document classification. Its original upstream identity is [SlowGuess/Arxiv_2020_OCR](https://huggingface.co/datasets/SlowGuess/Arxiv_2020_OCR), revision `a68009864dbc3b1decb1a37a6c4f769887169a44`. All 8,836 sources are retained without subsampling, text truncation or new optical character recognition. Folder renaming does not change provenance or source checksums. Existing original and normalized text Git trees are retained unchanged.

Set `DATASETS_ROOT` to the directory containing dataset folders. By default this is the repository’s `Datasets/` directory. Set `ADVANCED_DATA_SCIENCE_ROOT` when the runtime’s working directory is outside the checkout. In Colab, files in the runtime are temporary: use a mounted persistent destination or explicitly save files to the repository. A notebook document alone does not transfer or persist its accompanying files.

Projects only read available dataset files. They never execute dataset loaders, download missing data or modify shared datasets. Missing files are caught with `except FileNotFoundError`: the notebook prints `Dataset not found` and skips dependent calculations. Run the dataset notebook manually, then rerun the project’s dataset cell. Project partitions, trained models, numerical references and predictions remain in the project’s directory, not in the shared dataset.

Dataset revisions are explicit. Rerunning the notebook must not silently substitute a different upstream release. Verified files, original source names, source links, checksums and normalization records remain traceable.

## Notebook development and Python deployment

Each project has one notebook. Every code cell has a separate rendered Markdown title and explanation immediately above it. The explanations connect prerequisites, operations and outputs so the presentation follows the computation’s dependencies.

Develop, execute, inspect and validate the project in its notebook. Necessary mathematical assertions and coverage checks stay in that notebook; there is no separate test notebook. Once the notebook works correctly and its results are validated, consolidate the same code into a Python pipeline in `project_python/`, preserving its mathematical definitions, inputs and outputs. No deployment pipeline is claimed before that validation.

The current project preserves training-only vocabulary and inverse-document-frequency fitting, source-family separation, all cluster counts 2–100, the maximum finite variance ratio criterion with the established exact tie rule, fixed selected assignments, original grouped moments and contextual profiles, subsequent singular value decomposition, target alignment and feature-aware final-block BERT training. Classification comparisons use the same source population. Measured results are reported as obtained, without forcing superiority.

## Independent figures

`Figures.ipynb` owns reusable figure code, not projects. It installs its own plotting dependencies and neither loads another notebook nor obtains datasets. Supply measured input paths explicitly for empirical figures. `RENDER_FIGURES` is off until rendering is requested in the notebook; explanatory figures are synthetic and are not classification findings. The default output location is `figure_outputs/` in the working directory. Generated files are outputs, not a second collection of figure code.

## PDF creation

`PDF_Creation/PDF_Creator.ipynb` compiles existing LaTeX sources; it does not generate manuscript prose. Sources are in the adjacent `Projects_LaTeX/` directory and successful documents are saved in `PDFs/`. Each paper has one execution cell. Configure the figure input directory explicitly.

When a PDF already exists, the compiler makes a `.backup.pdf` copy, builds the replacement in a temporary directory and validates that it is a readable PDF. Only then does it atomically replace the destination and remove the backup. A failed compilation preserves the previous PDF and backup. Missing LaTeX or figures is an error, not permission to substitute content.

The current LaTeX manuscript is preserved from the existing revision. Its final scientific revision and PDF release still depend on complete measured computational results; rearranging the workspace does not establish scientific completion.

## Open in Colab

- [Datasets](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/Datasets/Datasets.ipynb)
- [Project notebook](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/project_notebooks/from_linguistic_context_to_semantic_structure/Proof.ipynb)
- [Figures](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/Figures.ipynb)
- [PDF creation](https://colab.research.google.com/github/shulruferor-sudo/Advance-Data-Science/blob/main/PDF_Creation/PDF_Creator.ipynb)

Open from a saved checkout or configure the root paths explicitly. Project notebooks intentionally do not clone or fetch datasets. To refresh notebook code from GitHub, reopen its link; an already-open Colab document keeps its existing cells.

## Execution and continuation

GitHub Actions executes the project notebook from its committed paths and saves project checkpoints. Dataset acquisition remains a manual, separate operation. Existing jobs run in their own checkouts and are not cancelled by this reorganization. Legacy run artifacts and the former `corpus/` cache remain recovery sources for a computation started before the move; reconcile their latest checkpoints into the project directory before continuing from a stale copy.

The source corpus was verified at commit `ec6217619d033362a64c2b585c342ccfe0411aa6`. Earlier implementation tests and pretrained-model recovery fixtures establish implementation behavior, not full-corpus classification findings. The original ordered research plan remains: reconcile state; establish execution; chunk all texts; fit training-only lexical weights; evaluate all cluster counts; compute selected-reference features and decompositions; train prescribed comparisons; verify results; render result plots; validate self-contained execution; revise the paper from measured findings; validate the manuscript and PDF against the implementation.

The shared workspace overview is to be refreshed each Friday morning in Jerusalem time. It should show measured progress, current problems, available figures and results, and prioritized next actions that advance the author’s work. Recommendations remain separate from observed outcomes.

### Failure reporting

All four notebooks report failures at cell boundaries using Python `try`/`except`. Messages identify the operation, exception type and reason, and what to assess. Failed subprocesses also show the final diagnostic output. Unexpected errors are re-raised with their original traceback, stopping execution instead of allowing a failed operation to look successful. Keyboard interruption remains available. A missing project dataset prints its missing path and skips dependent calculations; acquisition remains a separate manual action. Correct the cause, then rerun the affected cell and dependent cells. Existing checkpoints and PDF backups remain governed by their recovery rules.
