# Bureau of Statistics survey data review

This project starts with what a survey response actually records. The person’s occupation, the employer’s industry and the employer’s name answer three different questions. The assignment eventually asks for an occupation classifier. This stage covers the data and the exploratory text clusters so the evidence can be reviewed before deciding how to predict a code.

## Reusable data investigation and notebook authoring protocol

This section is a **portable working manual**. It describes how to investigate unfamiliar structured data and produce an executable notebook whose questions, measurements, conclusions, and modeling decisions can be checked by another data scientist. Reuse it in other projects by replacing only the source, schema, target, and project-specific questions. The case-specific findings below are not general rules.

### 1. Establish what each source contributes

Read the **assignment or business brief**, **field dictionary/metadata**, **original data**, and any **existing interpretation or presentation** together before implementing field transformations:

| Source | What to establish | What it does *not* establish |
| --- | --- | --- |
| Brief and questionnaire instructions | Business objective, unit of observation, population/scope, response rules, update behavior, prediction target, required deliverables | That the data actually obey every stated rule |
| Field metadata/codebook | Exact field meaning, declared type, allowed values, conditional applicability, units and code semantics | Actual completeness, value validity, ordering, or whether text is a free-entry UI control |
| Observed dataset | Row counts, missingness, distributions, duplicates, conflicts, relationships, unusual values and their record keys | Causality, true respondent identity, semantic correctness, or information not recorded |
| Existing interpretation/presentation | Research questions and prior proposed decisions; known issues worth reproducing | Fresh empirical evidence: reported counts and conclusions must be verified by executing code |

Use field **names** to join metadata to data; metadata row order may differ from data column order. Inspect how Excel stores and *displays* numbers, dates and classification codes; neither worksheet dimensions nor numeric storage alone determine semantics. Retain a raw, auditable snapshot. Identify the observation key, record boundaries, and any non-data rows **before filtering**; do not silently discard records that should be examined for missing IDs.

### 2. Derive questions by *field meaning*, not by field name

Start with the fundamental questions: **What is recorded? What does it mean? Why was it collected? What evidence is missing? What can the observed values actually establish?** Narrow them to questions that require computation. Different fields may share a single test if they answer one dependent question.

| Field type / relationship | Questions to answer with code | Evidence or test |
| --- | --- | --- |
| Record identifier / running key | Is it complete, unique, correctly typed, and sequential *if sequential numbering is specified*? Does a record key identify a submission, respondent, or version? | Missing/duplicate counts; integer/range checks; observed key structure. Never infer history without a stable identity/version or timestamp |
| Nominal category | Are values members of the codebook? Does a numeric-looking code actually represent an unordered label? | Frequencies, undefined codes, explicit missing category; preserve categorical semantics |
| Ordinal category | Does the metadata establish an order? Do exceptions such as “other” or “none” break it? | Exact code-to-meaning mapping; verify order before ordinal encoding |
| Numeric measurement / count | What are the units, valid bounds, integer requirement, distribution, and missingness? | Parse failures, fractional/negative/impossible values, ranges and outliers; justify any bounds |
| Dates / durations | What event does the date represent, and what valid reference date would a duration require? | Parse and range checks; no invented “current” reference date for historical duration |
| Free or potentially free text | Is it a genuine description, placeholder, reference to another answer, optional title, acronym or mixed-language value? | Completeness, source phrases, language/script patterns, placeholders and reference cases; do not assume “TEXT” proves a specific form control |
| Entity/name text | Are differently written names actual aliases, transliterations, generic descriptions, or different entities? | Candidate pairs and context; semantic similarity is a proposal, not verified identity |
| Conditionally applicable field | Who is eligible to answer? Is blank not applicable, unanswered, or unknown? Are some filled values inconsistent? | Joint cross-tabulation with governing field; mutually exclusive applicability states and ID-linked contradictions |
| Structured/hierarchical code | Is the value a number or a code with fixed width, prefixes and partial symbols? | String-format and prefix checks; check Excel leading-zero formatting; preserve partial information |
| Label/target | Is it the intended outcome? Are labels partial, noisy or available only after the prediction decision? | Completeness, class counts, disagreements, prefix coverage and label-source provenance |
| Candidate predictor / information source | Is the value available **at the time of inference**? Could it leak the target or be fitted using held-out records? | Prediction-time availability analysis; train-only fitting; scenario/ablation when uncertain |

Do not force every variable into one representation. Separate direct outcome evidence from organizational or contextual information. When the business rule involves two or more fields, investigate them **together**, show the relevant records and derive one decision from the joint evidence. Ask an additional question only when the existing evidence implies a consequential unresolved issue.

### 3. Author each investigation as a reviewer-facing Markdown/code pair

**Markdown comes before the calculation**, with only:

1. **Feature or question type:** what the source metadata defines, and the relevant rule from the brief.
2. **Question:** exact research question(s), in the notebook's presentation language.
3. **How it will be answered:** the smallest specific check, cross-field comparison, table or plot required.

Then a **single Python code cell** should implement the check on the **already loaded DataFrame**. Write the corresponding question as a concise comment directly above its code. A field can have its own pair, or a related group of fields can share one pair when the same question genuinely spans them. **Do not write “Findings” or “Conclusion” in Markdown before the code has produced results.** Present measured evidence first, then a conclusion justified by that evidence, not a predetermined statement. Do not reframe known metadata rules as discoveries.

Copy-ready notebook pattern (replace the placeholders, not the sequence):

```markdown
### <Field or relationship> — <semantic role>

**Metadata and business rule:** <precise definition and applicable constraint>.

**Question:** <one answerable investigative question>?

**Verification:** <specific measurement, comparison or validation on the loaded data>.
```

```python
# Q: <one answerable investigative question>?
values = data[COLUMN]                         # Reuse the existing loaded DataFrame
summary = pd.DataFrame({
    "Records": [len(values)],
    "Missing": [int(values.isna().sum())],
    "Distinct": [int(values.nunique(dropna=True))]
})
display(summary)                                # Show the measured evidence

# State a finding only if the displayed evidence supports it.
```

The pattern is a **shape**, not a mandate to print these three counts for every field. Replace generic counts with the check the *actual question* needs. Prefer one necessary table, chart or comparison over repeated descriptive summaries. If the answer cannot be observed from the available fields, state the limitation rather than inventing verification.

### 4. Preserve a sequential notebook

1. **Imports and notebook-wide settings (before data preparation):** import libraries, configure display and define the runtime seed. Do not retrieve data or load pretrained model weights in the imports cell.
2. **`## Data preparation` — first executable cell: load the source data.** Put this H2 heading **immediately before the first data-loading code cell**, never after it. Download/open the identified source, verify its integrity, and read the dataset and field metadata into DataFrames once. Preserve a copy of the source records. A metadata table and a small data preview may follow.
3. **`### Investigation`:** ask only the field-type and cross-field questions justified by the brief and codebook. Place each relevant question next to the executable check on the **already loaded** DataFrame. Show measured outputs before claiming findings.
4. **`### Decisions`:** interpret the investigation results against source definitions, distinguish observed facts from assumptions, and decide what to preserve, review, normalize, encode or exclude. No empirical conclusion precedes its calculation.
5. **`### Transformations`:** perform the justified changes in derived data views, preserving raw values and record keys. Load task-specific language/embedding model weights in this section, in their own code cell, and apply them in a separate step. Do not silently treat proposed entity matches as verified.
6. **`## Classification and evaluation` (after data preparation):** construct predictors, establish prediction-time availability, fit learned preprocessing on training folds only, compare baselines and alternatives, and report held-out evidence.
7. **Results and interpretation:** display metrics, relevant plots, anomalous record IDs and limitations; write conclusions that follow the executed findings.
8. **Export:** save a reproducible notebook and necessary outputs. Previously saved outputs do not verify new or moved code until rerun.

Each executable cell must have one clear purpose and explicit inputs/outputs from earlier cells. Never overwrite an existing stage merely to append a new investigation. Preserve working computations and prior results unless they are incorrect or deliberately superseded.

### 5. Code and notebook presentation

Write for the person evaluating the work.  
Explain the investigation in natural, vivid and precise scientific English.  
Use the researcher's voice and active language to describe work actually performed.  
Avoid formulaic wording, generic filler, assistant references, promotional claims, process commentary and approval requests.  
Every sentence should convey a distinct, meaningful point.

**Markdown presentation**

In short explanatory sections, put each complete, meaningful sentence on its own visible line.  
Use Markdown line breaks when necessary to preserve those lines in the rendered notebook.  
Do not add bullets to ordinary explanatory sentences.  
Avoid isolated sentence fragments and unnecessary lines of only a few words.  
Keep tables, genuine lists, code blocks and longer passages in the format that makes them easiest to read.

**Punctuation**

Do not use semicolons, en dashes or em dashes in prose, headings, code comments or output labels.  
Prefer periods, commas, parentheses and new lines.  
Use a hyphen only where conventional spelling or established technical notation requires it.  
Punctuation required by programming language syntax is allowed.

**Code and results**

Prefer compact, horizontally readable code that shows one question, its analysis and its result together whenever practical.  
Group related expressions without sacrificing clarity or meaningful variable names.  
Use concise comments to explain the purpose of a calculation rather than narrating every operation.  
Reuse previously loaded data and computed values instead of repeating earlier steps.  
Display only the tables, records and plots needed to answer the current question.  
Present calculated results before writing any empirical finding or conclusion.

For a reporting cell that needs a visual heading, use H2 with one empty print before the heading and two empty prints before each table:

```python
print()
display(HTML("<h2>Data inspection</h2>"))
print(); print()
display(metadata)
print(); print()
display(data.head(3))
```

Do not repeat a heading already shown by the preceding Markdown cell.  
Preserve the project's established table styling and use plots only when they provide readable evidence.

### 6. Evidence and release checks

- **Question-to-code coverage:** every included data question must have an identifiable test, and every test must answer its preceding question. Do not include prose-only questions when the task specifically calls for code-supported investigation.
- **Correctness:** check the actual metadata types/allowed values, exact data scope, source record counts, missing values, edge cases, assumptions and conditional rules. Distinguish stored Excel values from displayed formats; do not treat workbook artifacts outside the survey as records.
- **Traceability:** retain original field values and row identifiers, show conflicting cases by ID, and keep proposed normalizations distinct from validated replacements.
- **Epistemic order:** question → method → executed output → finding → justified decision. The title, explanation and comments may state **what will be tested**; do not prestate an empirical finding as though already computed.
- **Validation:** verify Python syntax, cell dependencies, top-to-bottom execution, shape invariants and source preservation. A notebook edited in GitHub but not rerun has **unverified new results**; mark that distinction outside the reviewer-facing scientific conclusions until execution.
- **Scope control:** implement only the project's established requirements and relevant implied checks. Keep optional enhancements in a separate, clearly labeled proposal; do not weave unapproved proposals into the notebook's code or analysis.
- **Maintenance:** when work reveals a new *transferable* lesson about investigation, code structure, validation or communication, update this section with a concise operational rule. Put dataset-specific findings elsewhere in the README. This manual should stay reusable without needing to rename every variable.

---

## What the assignment asks

The interview brief asks for Python code that predicts `SemelMishlachSofi`, an executable Jupyter notebook with predictions and a GitHub link, and a presentation of up to ten slides. The slides should explain the business problem, the data, the solution, the findings and the next steps for implementation. The brief calls the data simulated and explicitly gives the prediction results little weight. That makes the reasoning behind the data handling important. It gives no scoring rubric and names no required classifier.

The source is the Excel workbook in the [Drive Assignment folder](https://drive.google.com/drive/folders/1XMeO2TSCBxGl2HXWhOMCbBH9XqVUOL5g). The [assignment document](https://drive.google.com/file/d/1V1T1qcuGMP8FPj97RAq2XAXXK_uvY8DA/view) contains the Hebrew interview brief followed by English project instructions. The ten-slide limit applies to the eventual interview submission. The larger collection in [Plots](https://drive.google.com/drive/folders/11kfdp62UIBbsUdcWFxUG_K8Ux3qdmKJY) is a set of candidates for review.

## Wording that changes the analysis

| What the brief says, in English | What follows for this workbook |
| --- | --- |
| A respondent can update and transmit a questionnaire several times. | Repeated submissions are possible. The running row number identifies a record. Without a persistent respondent ID or a submission time, matching text cannot establish identity, sequence or which response supersedes another. |
| The system allows some fields to be left blank. | A blank records the absence of an answer. Its meaning depends on the question. A blank management field does not establish that the person manages nobody. |
| Job title is requested if one exists. | A blank title may be permissible. It could also be an omitted answer. The workbook cannot distinguish those cases. The separate work description may still be informative. |
| The pay source field is filled only for employees or cooperative members. | This is a condition on two fields. A pay code can belong to its allowed list and still be inapplicable for that record. A missing employment status leaves the condition unresolved. |
| Questionnaires are randomly routed to professional coders. | Random routing refers to coder assignment. It provides no evidence that this workbook represents the national workforce. There is no coder ID for estimating differences between coders. |
| Prior sample checks found about 90% of manual codes correct. | This is background about manual coding. It cannot identify the incorrect rows, produce a verified label for each person or establish an accuracy ceiling for this file. |
| X means the coder could not complete the code. | Preserve the pattern. A partial code can retain known digits. Replacing it with zero, treating it as a complete occupation or discarding its known digits would lose information. |
| Codes follow an international standard and prior knowledge of it is unnecessary. | The workbook documents the code structure, but supplies no versioned codebook or independent reference labels. A four-digit display confirms the recorded form. It does not validate the occupational decision. |
| The target is the person’s occupation. | The final industry code describes the employer. It is available for this audit. The workbook does not say when it becomes available to a future coding system. |
| The data are a simulation. | Counts, associations and word patterns describe these 200 rows. Population rates, trends and causal conclusions would require additional evidence. |

## What I checked in the original file

I matched each survey column to its metadata by field name. The order of the job start date and industry code differs between the two sheets. I inspected all 200 rows and all 18 fields, preserving the Excel address, source type, value, number format, displayed code, metadata definition and review finding for each of the 3,600 cells.

| Observation | Why it matters |
| --- | --- |
| The survey records occupy A2 through R201. J202 contains the formula `1.5*1.15`. | Its cached value is 1.725. Reading it as another survey record would introduce a fractional management code and create a false anomaly. |
| The field dictionary occupies A2 through D19. There are 16,309 copies of the text `TarichHathala` in row 18 outside those four columns. | The last occupied Excel column is a poor way to infer the number of variables. There are 18 metadata definitions. |
| All numeric industry and occupation cells use Excel’s four-digit display format. Four industry cells store 123 and one stores 124. | The workbook displays 0123 and 0124. These five cells conform to the documented width. Simply converting the stored numbers to strings produces a false data-quality finding. |
| Of 200 pay-source cells, 177 are present where the question applies, 12 are blank where it does not apply, nine contain an inapplicable answer and two have unknown applicability. | The reason for each state is preserved. The nine contradictions are available by row ID in the cell audit. |
| Cell I40 contains numeric zero in the job-title field for record 39. | The field is declared as text. The metadata does not define zero as a title or a missing-value code. The original value remains available for review. |
| 191 occupation codes are complete. The nine partial responses comprise four `1XXX`, four `XXXX` and one `335X`. | Each pattern carries a different amount of information. A full code is still a manually assigned source label. |
| 189 combinations remain when the running ID is excluded from the 200 full records. | Eleven rows repeat an earlier row on the other 17 fields. This is a property of the data, not a count of confirmed repeat respondents. |
| Records 2, 33, 65 and 96 share all six normalized descriptions. Their source occupation codes are 3311 and 3211. | This is a case for adjudication. Nothing in the file establishes the correct code or the identities of the people concerned. |
| Six of the nine records with a partial occupation code lack substantive content in all six description fields. | An empty cell, a reference to another answer and an explicit refusal to elaborate carry different information. The audit retains all three. |

## Why explore the text one field at a time

The six fields describe the workplace activity, department, department activity, work performed, main tasks and job title. A repeated phrase in two questions can be informative because the questions differ. Pooling the strings would also create links between answers to different questions. Each network therefore uses one field, with no occupation code in its inputs.

A node represents a distinct response after Unicode, whitespace and case normalization. The source spelling is written next to the node. Hovering or selecting it reveals its frequency and record IDs. Different spellings and languages remain separate. Node frequency counts records. Inverse document frequency is calculated on distinct normalized responses so repeating a survey row does not make that wording appear less informative.

The notebook uses word TF-IDF with no IDF smoothing and L2 normalization. For these unit vectors, the squared Euclidean distance is twice one minus cosine similarity. A node nominates up to three nearest neighbors that share at least one token. An edge is retained if either endpoint nominates it. Equal distances are resolved by a stable sort on the normalized response. A node with no shared word has no edge, even if the 3D view places another label nearby.

For each field I checked every admissible K from two through the smaller of 100 and the number of distinct vectors less one. I retained both the Calinski-Harabasz and silhouette scores. In all six fields, the highest Calinski-Harabasz score occurred at the largest admissible K. That leaves almost every wording in its own cluster. For the initial view I chose the highest silhouette among partitions with at least two distinct vectors per cluster. It is an explicit viewing rule, not evidence that the groups are occupational categories. The explorer lets you inspect every K.

The 3D coordinates come from metric multidimensional scaling of the original distances. Across fields the relative distance error ranges from about 0.25 to 0.31. Clicking two nodes shows their distance before projection. The marked edges and cluster assignments are also computed before projection.

## Statistical questions

I compared years of schooling across the seven observed credential categories. The 198 records with both values have a descriptive one-way ANOVA F statistic of 160.09 with 6 and 191 degrees of freedom. Credential groups account for 83.4% of the observed sum of squared deviations in years of schooling. Counting identical full records once leaves 187 usable records and gives 83.5%.

Two groups have zero within-group variance. One has three observations and the other has four. The simulation and possible repeated respondents also prevent an independence claim. The workbook provides neither a probability sample nor respondent-level linkage. The exported table includes the conventional nominal p-value for arithmetic reproducibility. I use the variance decomposition, group sizes, quartiles and observed ranges to explain the sample, without making a population significance claim.

## Review record

On 3 November 2026 I retrieved the original document and workbook from Drive, read the field definitions, checked every survey cell, distinguished stored numbers from displayed codes, traced the conflicting records, computed six independent word networks and checked the descriptive variance decomposition. The source workbook has 907,941 bytes and SHA-256 `e1e7f391c0675dd14830eaae6b5cd114edc256f18b956bb48a454b0b1209e1ac`.

The current checkpoint is the data review. The next decision is which figures to retain for the interview and whether the data interpretation is accepted.
