# From Linguistic Context to Semantic Structure

Or Shulrufer

Advance data science. Canonical repository: https://github.com/shulruferor-sudo/Paper-1

The main project consists of one `corpus` folder, three Jupyter notebooks, two manuscript sources and this README. Filenames stay fixed. Changes are recorded through Git commits and, for existing Library deliverables, through their version histories.

| File | Purpose |
| --- | --- |
| `From_Linguistic_Context_to_Semantic_Structure.ipynb` | The one computational pipeline. Obtain the corpus and run each scientific stage in order. |
| `From_Linguistic_Context_to_Semantic_Structure_Tests.ipynb` | Exercise the computational notebook's actual functions without duplicating their implementation. |
| `From_Linguistic_Context_to_Semantic_Structure_Figures.ipynb` | Define all manuscript illustration and result-plot generators. Rendering remains disabled until approval. |
| `From_Linguistic_Context_to_Semantic_Structure.md` | The Unicode Markdown manuscript source. |
| `From_Linguistic_Context_to_Semantic_Structure.tex` | The LaTeX manuscript source from which the approved PDF will later be compiled. |
| `corpus/` | Complete source texts, metadata, normalization records, checkpoints and measured outputs. |
| `README.md` | Project purpose, execution and revision instructions. |

The `.md` and `.tex` files are edited directly. No separate program generates either manuscript source. The existing manuscript sources are preserved for revision. Their earlier news-corpus and TextTiling passages are historical draft material and are not results for the current arXiv corpus. The computational checks and measured classification comparisons must pass before those sections are rewritten. No PDF is included in this commit, and no new manuscript figures are rendered.

Use **Actions → Run research notebook → Run workflow** to execute on GitHub. The test notebook runs first. The `.github` directory contains the configuration required to execute these notebooks on GitHub; it is not an additional manuscript, notebook or project version. To run the notebooks yourself in Jupyter, run the cells in order; the first code cell installs the pinned dependencies from the computational notebook. Manuscript figure rendering additionally requires PyMuPDF 1.26.6, Pillow 12.3.0, scikit-learn 1.8.0, XeLaTeX, PGFPlots and Latin Modern fonts. The figures notebook preserves the ten existing explanatory Python generators, the three-dimensional variance generator, three method diagrams and three empirical plot generators.

After the notebooks are validated, an optional single Python pipeline will be derived for larger systems. It will use scikit-learn transformations and PyTorch training where they serve this same pipeline. Its mathematical definitions, source partitions, fitted state and outputs will match the validated notebook. Do not create that deployment file during notebook development.

The current executable stage obtains and normalizes the complete existing [arXiv text corpus](https://huggingface.co/datasets/SlowGuess/Arxiv_2020_OCR) at revision `a68009864dbc3b1decb1a37a6c4f769887169a44`. It retains all 8,836 documents and verifies their complete released bytes. It retrieves publication dates and primary category labels from arXiv. It performs no new PDF extraction or optical character recognition and applies no document subsampling or text truncation.

GitHub Actions executes the same notebook and preserves its outputs, figures, progress records and resumable corpus cache. After all corpus checks pass, it commits the complete original texts, normalized texts and provenance records into this repository. These files then have ordinary Git history and do not depend on an Actions cache. Existing local copies remain valid and unchanged. The workflow can also be started with **Run workflow** from the Actions page.

Keep canonical filenames. Revise the same files through Git commits. Store manuscript and non-code checkpoints in the existing Paper Final Library items through their version history. ChatGPT Library stores files and does not execute Python notebooks.

Corpus preparation is the current execution stage. Clustering, coefficient-of-variation profiles, singular value decomposition, classification and the final paper remain downstream stages of the agreed project. A successful corpus-preparation run does not establish classification performance or completion of the full experiment.

Standard GitHub-hosted jobs have a six-hour execution limit. This workflow uses a five-hour notebook step and reserves time to save checkpoints. It uses the account's existing Actions allowance and billing configuration without changing either.
