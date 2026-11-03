# Bureau of Statistics survey data review

This project starts with what a survey response actually records. The person’s occupation, the employer’s industry and the employer’s name answer three different questions. The assignment eventually asks for an occupation classifier. This stage covers the data and the exploratory text clusters so the evidence can be reviewed before deciding how to predict a code.

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
