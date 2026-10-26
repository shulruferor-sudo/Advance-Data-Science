# Advanced Data Science

Or Shulrufer's public workspace for reusable datasets, scientific figures and advanced data science projects.

## Workspace structure

The requested structure separates shared scientific resources from project implementations:

| Location | Purpose |
| --- | --- |
| `datasets/` | Shared datasets and their loaders, source identities, checksums and normalization records. Any project can use any dataset. |
| `project_notebooks/` | One computational notebook per project, containing its explanations, executable calculations, checks and displayed results. |
| `project_python/` | Python implementations derived from validated project notebooks for use in larger systems. |
| `Figures.ipynb` | One shared notebook containing reusable figure generators, each introduced by a Markdown title and explanation. |
| `README.md` | Workspace organization, dataset access and project execution instructions. |

The first shared dataset is the complete 8,836-source arXiv text corpus already committed here. Its loader must reuse verified local files, preserve every source, and expose the dataset independently of project-specific training partitions, model checkpoints and results. Moving it must preserve its original and normalized text checksums.

Each project notebook contains its own executable verification. A separate test notebook is not part of the requested structure. Successful execution and scientific validity remain distinct: coverage, partition separation, numerical agreement, target alignment and training updates require explicit checks within the notebook.

The repository name requested is **Advanced Data Science**. The current GitHub address remains https://github.com/shulruferor-sudo/Paper-1 until the repository itself is renamed.

## Migration state

The structure above is the requested destination, not a claim that the files have already moved. The active scientific workflow and its queued continuation still use the current root notebook paths and `corpus/`. Those paths remain intact while the active job uses them. Relocation must update notebook startup, dataset loading, result locations, figure inputs, workflow paths and Colab links together. Existing manuscripts, checkpoints and measured results remain preserved. The historical layout and continuation record below describe the current executable checkout until that coordinated migration is complete.

## Current research project

Or Shulrufer

Advance data science. Canonical repository: https://github.com/shulruferor-sudo/Paper-1

The current executable project consists of one `corpus` folder, three Jupyter notebooks, two manuscript sources and this README. These paths remain in place until the coordinated migration described above. Changes are recorded through Git commits and, for existing Library deliverables, through their version histories.

| File | Purpose |
| --- | --- |
| `Proof.ipynb` | Executable computational evidence for the paper: obtain the corpus and run every scientific stage in order. |
| `Unit_Tests.ipynb` | Unit tests of the computational proof notebook's actual code, without a duplicate implementation. |
| `Figure_Generator.ipynb` | Generate the manuscript illustrations and measured-result plots after computational validation. |
| `Unicode.md` | The Unicode Markdown manuscript source. |
| `PDF_Creator.tex` | LaTeX code compiled to create the PDF. |
| `corpus/` | Complete source texts, metadata, normalization records, checkpoints and measured outputs. |
| `README.md` | Project purpose, execution and revision instructions. |

The `.md` and `.tex` files are edited directly. No separate program generates either manuscript source. The existing manuscript sources are preserved for revision. Their earlier news-corpus and TextTiling passages are historical draft material and are not results for the current arXiv corpus. The computational checks and measured classification comparisons must pass before those sections are rewritten. No PDF is included in this commit, and no new manuscript figures are rendered.

Use **Actions → Run research notebook → Run workflow** to execute on GitHub. The test notebook runs first. The `.github` directory contains the configuration required to execute these notebooks on GitHub; it is not an additional manuscript, notebook or project version. To run the notebooks yourself in Jupyter, run the cells in order; the setup cell locates or obtains the project, followed by installation of the pinned dependencies from the computational notebook. Manuscript figure rendering additionally requires PyMuPDF 1.26.6, Pillow 12.3.0, scikit-learn 1.8.0, XeLaTeX, PGFPlots and Latin Modern fonts. The figures notebook preserves the ten existing explanatory Python generators, the three-dimensional variance generator, three method diagrams and three empirical plot generators.

After the notebooks are validated, an optional single Python pipeline will be derived for larger systems. It will use scikit-learn transformations and PyTorch training where they serve this same pipeline. Its mathematical definitions, source partitions, fitted state and outputs will match the validated notebook. Do not create that deployment file during notebook development.

The computational notebook obtains and normalizes the complete existing [arXiv text corpus](https://huggingface.co/datasets/SlowGuess/Arxiv_2020_OCR) at revision `a68009864dbc3b1decb1a37a6c4f769887169a44`. It retains all 8,836 documents and verifies their complete released bytes. It retrieves publication dates and primary category labels from arXiv. It performs no new PDF extraction or optical character recognition and applies no document subsampling or text truncation.

GitHub Actions executes the same notebook and preserves its outputs, figures, progress records and resumable corpus cache. After all corpus checks pass, it commits the complete original texts, normalized texts and provenance records into this repository. These files then have ordinary Git history and do not depend on an Actions cache. Existing local copies remain valid and unchanged. The workflow can also be started with **Run workflow** from the Actions page.

Keep canonical filenames. Revise the same files through Git commits. Store manuscript and non-code checkpoints in the existing Paper Final Library items through their version history. ChatGPT Library stores files and does not execute Python notebooks.

Corpus preparation and normalization passed for all 8,836 documents in run 40248242815. The complete corpus is now preserved in this repository at commit `ec6217619d033362a64c2b585c342ccfe0411aa6`; run 40250580314 passed acquisition, source labels, normalization and the final byte verification for all 8,836 sources. The earlier corpus remains in its original Git history. The notebook now contains the original numerical definitions, contiguous Chonky segmentation, the complete 99-candidate cluster search, grouped moments and contextual profiles, subsequent singular value decompositions, pretrained BERT training, all prescribed comparisons and completion checks. The full arXiv computational run is still in progress; a `verification.json` record is created only after its measured comparisons and consistency checks complete. Corpus preparation and unit tests do not establish classification performance or full experiment completion.

Standard GitHub-hosted jobs have a six-hour execution limit. This workflow uses a five-hour notebook step and pauses computation at a saved checkpoint after approximately four hours of scientific execution. Scheduled continuations check every six hours and resume incomplete computation. They stop substantive execution once `corpus/results/verification.json` records completion. Manual runs remain available. Per-source chunk boundaries, individual cluster fits and optimizer progress are reused. Large model and result artifacts are preserved in checksum-verified parts below GitHub’s single-file limit; original files remain in place while processes use them. It uses the account's existing Actions allowance and billing configuration without changing either.


## Continuation and evidence record

This section is a separate assessment of the project state. It is not an original chat transcript and is not manuscript prose. Original chat files, research-era files and historical manuscript sources remain unchanged. Available conversation retrieval provides excerpts and summaries, not a complete message-by-message transcript of all earlier sessions. No claim of reviewing every earlier message is made.

### Governing decisions from the author

- Keep one project titled **From Linguistic Context to Semantic Structure**, authored by **Or Shulrufer**. Use this public repository; public readers have no automatic write permission.
- Keep the three notebooks, two manuscript sources, one corpus folder and this README. The `.github` folder is execution configuration. Use Git history rather than numbered copies. The latest naming correction requires filenames by purpose: `Proof.ipynb`, `Unit_Tests.ipynb`, `Figure_Generator.ipynb`, `Unicode.md`, and `PDF_Creator.tex`. The author controls the repository name. Install dependencies from the computational notebook.
- Edit the Unicode Markdown and LaTeX source directly. Do not generate them through a separate manuscript-writing program. Derive an optional single Python deployment pipeline only after notebook validation.
- Use every document and its complete extracted text from the pinned corpus. Do not select a smaller cohort, truncate texts, download PDFs or perform optical character recognition.
- Preserve source partitions across every comparison. Fit vocabulary, inverse document frequencies and learned feature transformations on training sources only.
- Select the cluster count solely by the highest finite **variance ratio criterion**, also called the **Caliński–Harabasz index**, across every count from 2 through 100; use the established tie rule. Classification accuracy does not select the cluster count.
- Preserve the original coefficient-of-variation calculations and perform singular value decomposition afterward. Coefficient of variation and cross-validation are different concepts.
- Train the classifier with term-frequency–inverse-document-frequency features and the aggregated contextual vector. Verify feature alignment, nonzero gradients and parameter updates. Compare the same encoder with and without aggregation on the same partitions.
- Repair demonstrated implementation defects and rerun affected stages. Report measured comparisons faithfully; improved accuracy must be measured, not assumed.
- Complete computational validation before revising manuscript findings. Preserve the supplied historical research eras and scientific definitions. Read the pertinent full reference before changing a scientific decision.
- Finish the figure generators, measured figures, manuscript and compiled PDF in that order after computational validation. The latest instruction requests completion of every figure; do not stop for a redundant rendering permission after its evidence checks pass.
- Preserve original chat files separately. Assess author instructions, assistant proposals and execution evidence separately before consolidation. Commit completed changes immediately.

### Verified state

| Component | Evidence and current state |
| --- | --- |
| Root project files | Three notebooks, Unicode Markdown, LaTeX and README published in this repository. Dependency files removed in commit `57eb00d868d9dfa87087f4f77a9094263030a940`. |
| Earlier complete corpus | Run [40248242815](https://github.com/shulruferor-sudo/personal-workspace/actions/runs/40248242815) passed. All 8,836 original texts verified byte-for-byte: 671,413,967 bytes. Dates and primary categories verified for all sources. All 8,836 normalized documents retained; zero empty documents. Corpus tree: `72383646464d12abc216246447527014bc591b9d`. |
| Current tests | GitHub run [40254325732](https://github.com/shulruferor-sudo/Paper-1/actions/runs/40254325732), job `121352896349`: all 26 tests passed, matching the local result. Coverage includes real pretrained-model interfaces, all 99 numerical fixture candidates, exact interrupted-training recovery and probability-roundoff handling. Tested notebook SHA-256: `a0476087af6b78daa7434c2ff46c037b9abad818b213a0654c5b101a3d8be15a`. |
| Current corpus placement | Run [40250580314](https://github.com/shulruferor-sudo/Paper-1/actions/runs/40250580314) completed successfully. All 8,836 original texts, verified primary categories, normalized texts and records are committed under `corpus/` at `ec6217619d033362a64c2b585c342ccfe0411aa6`. Original bytes total 671,413,967; zero normalized sources are empty. |
| Old project removal | Commit `fa8b967b85216a31d846bb11924df0e8267114a9` removed the transferred notebooks, manuscripts, README, dependencies and workflow from the earlier repository after its run finished. Commit `b758063fe4502d98a70906a746eb73aeaacc895e` subsequently removed the remaining obsolete corpus folder after exact original-text, normalized-text, normalization-record and source-manifest matches were verified. Earlier files remain available in Git history. |
| Supplied materials | Paper Final inventory: 112 files and 15 folders, including nine historical-era documents, the introduction, original-method references, numerical code, classification code, saved checks and model files. Paper 1: 109 files. Paper 2: eight files. Inventory is distinguished from full content review. |
| Numerical and classification work | Integrated in `Proof.ipynb`: original definitions, complete cluster search, profiles, singular value decomposition, direct pretrained BERT forward/training and all agreed controls. Ten scientific integration tests pass in addition to the 13 acquisition tests and three real pretrained-model tests (26 total). The numerical fixture executes all 99 candidate counts and verifies identical restart results. The real BERT checks verify target alignment, a final-block update and exact interrupted-training recovery; the real contextual model check verifies contiguous reconstruction of irregular fixture text. Corpus-wide measured results remain governed by the final verification cell. The earlier 3,000-source sampling rule is superseded. |
| Manuscripts | Existing revisions preserved byte-for-byte during transfer. Historical news-corpus/TextTiling passages await revision after current-corpus validation. No current-arXiv classification findings or final-paper claim is established. |
| Figures | Three-notebook structure includes the preserved figure generators. No new manuscript figure or PDF has been rendered. |

### Preserved component mapping

The existing source components are in the author's Paper Final materials. Their names below identify originals, not additional deliverable files to create. Their required functions are consolidated into the computational notebook, with tests in the test notebook. Historical paths below identify provenance; execution does not import those files.

| Required operation | Preserved component | Required continuation |
| --- | --- | --- |
| Contextual chunking | `experiment/code/run_expanded_segmentation.py`; Chonky model and tokenizer | Integrated original separator-end rule, without the historical 3,000-document restriction. Execution verifies exact contiguous coverage for every source. |
| Original numerical definitions | `experiment/code/Work_Context_Diagnostic.py` | Preserve raw-count inverse document frequency, normalization, coordinate distances and grouped moments. |
| Complete cluster sweep and subsequent calculations | `experiment/code/run_expanded_numerics_csr.py` | Integrated the bounded-memory sparse implementation. Run every cluster count 2–100 and preserve all criterion values, selected assignments, centroids, contextual profiles and subsequent singular value decompositions. |
| Supervised feature combination | `experiment/code/Work_Contextual_Behavior_Fusion.py`; `experiment/code/run_classification.py` | Integrated target-aligned feature concatenation and supervised training with the final encoder block and classifier, preserving training settings and controls. The direct BERT forward avoids a corpus-sized hidden-state cache. |
| Measured comparisons | `experiment/code/summarize_expanded_classification.py` | Use the saved predictions for identical source partitions, with aggregation versus without aggregation and the agreed baseline, decomposition and frozen-encoder controls. |
| Original method and historical research | `experiment/analysis/reference_source/Paper 1/`; the nine `Year…` documents and `Introduction.md` | Read source documents in full before method decisions. Preserve the cumulative historical explanation. Keep original source records separate from the author's final manuscript. |
| Model reconstruction | `experiment/code/Work_runtime_manifest.json`; `experiment/bert/`; `experiment/context_segmenter/` | Verify published revisions and saved file hashes. BERT revision `86b5e0934494bd15c9632b12f734a8a67f723594`; Chonky model revision `4a92de5574053676cbc5fd06bac86a6e13588000`. |

`run_classification.py` and the local `run_expanded_classification.py` differ only in the default output directory (`results` versus `expanded`). They are not different scientific methods. Use one integrated definition with the canonical `corpus/results` path.


### Fixed model and source-partition configuration

The pretrained classifier is [`google-bert/bert-base-uncased`](https://huggingface.co/google-bert/bert-base-uncased), pinned to the saved revision. Its token embedding vectors have 768 coordinates; its input limit is 512 positions, and it has 12 encoder blocks. Token identifiers select embedding-table rows. The comparison models train the final block and a 128-unit classification head. BERT with the scalar local term-frequency–inverse-document-frequency feature is compared with BERT receiving that feature and the full contextual profile. Both use ordinary mean cross-entropy, two epochs, batch size eight and seeds 19, 29 and 41. The earlier encoder blocks and corpus statistics remain fixed.

Source families join exact normalized-text duplicates and equal nonempty digital object identifiers. Five stratified group folds use seed 29, with test fold zero, validation fold one and training folds two through four. If a rare category has no training source, one deterministic whole family moves to training; each move and all class support counts are recorded before fitting. Every source remains included. Labels are primary arXiv categories, not inferred lexical senses. The frozen-encoder controls retain their distinct passage interface. Measured results cannot establish word-sense or segmentation accuracy without corresponding reference labels.


### Ordered continuation

1. Read this record and the existing Paper Final `experiment/analysis/Run_Record.json`; inspect the current GitHub run before writing or restarting anything. Preserve the author's corrections above.
2. Preserve verified corpus commit `ec6217619d033362a64c2b585c342ccfe0411aa6`. The original and normalized text trees match the earlier corpus exactly; the obsolete project folder was removed in commit `b758063fe4502d98a70906a746eb73aeaacc895e`, retaining Git history.
3. Execute the integrated contextual chunker and all-source partitions. Verify punctuation handling and exact, contiguous, non-overlapping text coverage.
4. Execute and verify training-only term-frequency–inverse-document-frequency weighting and zero-vector handling.
5. Execute all 99 prescribed Euclidean k-means candidates, calculate the variance ratio criterion from within- and between-cluster sums of squares, and apply the established selection and tie rules.
6. Fix selected centroids and assignments; compute coordinate distances, grouped population moments, coefficient-of-variation profiles and subsequent singular value decompositions.
7. Execute the trained Bidirectional Encoder Representations from Transformers baseline and all agreed feature comparisons and controls on the same source partitions, preserving the 512-position limit, target alignment and ordinary mean cross-entropy.
8. Complete code review and tests for coverage, numerical correctness, training updates, leakage prevention, prediction coverage, reproducibility and measured baseline comparisons. Repair defects and rerun affected stages.
9. Render the measured cluster-count curve with all 99 values and the exact selected value; render separately labelled classification figures and the remaining approved explanatory figures.
10. Verify self-contained execution using the packaged data, models, checkpoints and notebook. Only then declare earlier folders unnecessary.
11. Edit the existing Markdown and LaTeX directly using the Scientific Research guidance and measured findings. Preserve the original method and full historical narrative.
12. Compile the PDF from the final LaTeX and verify agreement among code, results, equations, figures, Markdown, LaTeX and PDF. This is the completion condition.

For a new conversation: **Continue from this README and the existing Paper Final run record. Preserve originals and completed checkpoints. Inspect scientific run 40253860968 and current-code run 40254325732 first; corpus preparation run 40250580314 has completed. Continue the first unfinished stage from its checkpoints. Do not treat corpus preparation or unit tests as full classification validation, and do not rewrite findings before the computational checks pass.**

A continuation check also revisits the project every six hours to inspect completed computational evidence, repair demonstrated execution defects, and continue the approved figures and manuscript steps after their computational prerequisites pass. It preserves active jobs and ends after the full deliverable is verified.



## Opening the notebooks in Colab

Open [Proof.ipynb](https://colab.research.google.com/github/shulruferor-sudo/Paper-1/blob/main/Proof.ipynb), [Unit_Tests.ipynb](https://colab.research.google.com/github/shulruferor-sudo/Paper-1/blob/main/Unit_Tests.ipynb), or [Figure_Generator.ipynb](https://colab.research.google.com/github/shulruferor-sudo/Paper-1/blob/main/Figure_Generator.ipynb) and run from the first code cell in a fresh runtime. Each code cell has its own Markdown title and explanation immediately above it.

The setup cell obtains the complete repository when it is absent, including the committed corpus and checkpoints. It reuses an existing project without pulling over local edits. An interrupted clone is not published as a usable project. A notebook already open in Colab retains its old cells; reopen the GitHub link to load these corrections. Downloaded runtime files are separate from the notebook document and are not automatically saved back to GitHub.

The test and figure notebooks read the computational notebook's shared dependency specification after setup. Figure rendering additionally installs the pinned PDF/image packages and checks XeLaTeX and Latin Modern fonts. Empirical rendering still requires complete computational verification. GitHub tests cover Python 3.12 and 3.13; the full computation retains its existing Python 3.12 environment.

### Notebook startup revision

The missing sibling-file startup defect was reproduced from the supplied Colab traceback. The revised tests exercise actual setup cells against a local Git fixture from empty directories, repeated execution, parent-directory discovery, preservation of incomplete directories and interrupted clone cleanup. These checks complement the existing scientific and pretrained-model tests; they do not claim a completed full-corpus experiment or an observed interactive Colab run.
