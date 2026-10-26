<!-- Updated at UTC: 2026-10-25T22:03:23.482785+00:00; updated by /root; contextual-chunking terminology. Creation history retained in Run_Record.json. -->
# From Linguistic Context to Semantic Structure

Or Shulrufer

## Abstract

Fragmented and mixed text can produce unusual word–context relationships, yet legitimate variation can produce similar statistical patterns. Examining these relationships requires corpus measurements that remain linked to individual words and their source passages. We integrate term frequency–inverse document frequency (TF-IDF), contextual-behavior statistics and BERT at the level of a target word occurrence. Euclidean k-means groups L2-normalized TF-IDF passage vectors in the original vocabulary coordinates, and the Caliński–Harabasz variance ratio selects the cluster count from declared candidates. The passage assignments remain fixed while each word weight is compared with its corresponding coordinate in the assigned centroid. Aggregated population moments yield a distance coefficient of variation when the mean distance is positive, while the full statistical profile retains cluster-specific weights, prevalence and variation. A prediction head combines each occurrence's local TF-IDF weight and statistical features with its BERT contextual state. The supervised loss updates that head and BERT's final encoder block. Derivations establish the aggregation and its fixed-reference properties, and synthetic implementation checks verify feature alignment and the training path. The construction makes corpus measurements available to occurrence-level learning while preserving word and cluster identities. Whether these features improve classification or identify damaged contexts remains to be established through independently labeled evaluation.

## Introduction

Variation in a word's use can reflect a legitimate change of meaning or arise from an incomplete passage, extraction damage or mixed material. A numerical departure alone cannot distinguish these explanations. The problem is therefore to describe how words behave across a corpus while retaining the source occurrences needed to interpret that behavior. The author's exploratory network visualizations motivated this connection between measured word patterns and inspection of the passages from which they arose.

Distributional descriptions relate linguistic units to their environments [1], and context representations support the grouping of word uses [2]. The coefficient of variation has also summarized weighted term frequencies across aggregated documents [3]. These approaches establish relevant ways to represent contexts and describe variation, but the quantities retain different information. A passage's term frequency–inverse document frequency (TF-IDF) weights describe its word composition relative to a reference collection. They do not by themselves explain whether a particular occurrence fits its surrounding text or how that word behaves across the corpus's different contexts.

This paper asks how corpus-level measurements can be connected to an individual word occurrence without losing the word coordinates, group references and source passages on which those measurements depend. We use contextual behavior to describe occurrence prevalence, weights when present, variation within fitted passage groups and differences between those groups. The objective is to make this information available both for source inspection and for supervised learning with BERT's representation of the occurrence in its ordered text.

The construction first fits passage groups in the original vocabulary coordinates of normalized TF-IDF rows. Euclidean k-means supplies the group centers, and the Caliński–Harabasz criterion selects a cluster count from a declared candidate set. Each passage then retains its fitted assignment. Each word weight is compared with the corresponding coordinate of that passage's assigned center, and population moments aggregate these distances separately for each word. Their coefficient of variation summarizes unevenness across the reference passages. The full group-conditioned statistical profile remains available because one corpus-wide ratio cannot preserve which contexts produced a pattern. These measurements precede any dimensional compression.

For supervised learning, the target occurrence aligns three inputs: its local TF-IDF weight, its corpus-derived statistical profile and its contextual BERT state. The prediction head combines them, and the supervised loss updates that head and BERT's final encoder block. The contribution is this explicit connection between source-linked measurement and occurrence-level learning, rather than the invention of the individual statistics or feature concatenation. Derivations and numerical checks establish the stated geometric relationships, aggregation and training mechanism under their assumptions. Whether the additional measurements improve classification or identify problematic word–context relationships requires independent labels and controlled evaluation on the relevant source material.

## Background and Scientific Foundations

A numerical method cannot recover a distinction that its observations have already discarded. We therefore begin with words, occurrences and passage boundaries. These choices determine the weight matrix. Its coordinates then support distances, group means and distributions. Each subsequent foundation answers a question raised by those objects, preparing the final combination with an ordered-text encoder.

Four identities must remain distinct. A source is the original document or record. A passage is a selected stretch of that source. A word is an item in the chosen vocabulary, and an occurrence is one appearance of that item at a particular source location. A source can contain many passages, and a word can occur many times within them. Retaining these identities lets a corpus-wide score lead back to the language on which it was calculated.

### Structural and distributional foundations of linguistic context

#### Words, sequences and situations

In Saussure's structural account, a linguistic element acquires value through its relationships and contrasts with other elements [4]. Syntagmatic relations connect elements combined in a sequence. Associative relations connect an element with alternatives or related forms. This distinction identifies something a count representation cannot preserve: two passages may contain the same words in different orders, with different grammatical roles. Keeping the ordered source text alongside the count row preserves evidence needed to examine that difference.

Identifying a word across different passages also requires a rule for what counts as the same linguistic element. The descriptive work of Sapir and Bloomfield examines linguistic forms and structural regularities rather than treating every visible form as an isolated object [5, 6]. In a computational vocabulary, case handling, inflection, abbreviations and language-specific segmentation affect which forms share a column. These are choices in the present representation, not procedures attributed to those earlier authors. They determine what variation within a column can mean.

Linguistic structure does not exhaust the evidence needed to interpret an utterance. Malinowski's context of situation and Firth's contextual approach include the activities and circumstances of use [7, 8]. A selected passage may omit the participants, objects or preceding events on which an expression depends. Retaining its source location therefore serves a scientific purpose: it allows interpretation to recover evidence that the numerical observation leaves out.

Distributional analysis makes the environment of a linguistic unit part of its description. Harris's work on morpheme alternants examined how different forms can occupy complementary environments. His analyses of combinations and connected discourse developed the question at larger structural levels [9, 10, 11, 12]. The relevant environment therefore depends on the unit being studied. A single fixed window cannot be assumed to preserve every relationship at every level.

Harris defined distribution through the environments in which an element occurs [1]. His comparison of oculist, eye-doctor and lawyer illustrates how shared surroundings can provide evidence of similarities and differences in use. Distributional similarity is evidence for interpretation, not an exact identity between distribution and meaning. Firth's accounts likewise distinguish lexical, grammatical and situational contributions [13, 14]. This paper draws on that distinction: its score describes a numerical pattern in recorded usage, while interpretation returns to the source.

The choice of environment is therefore part of the measurement. Neighboring words, grammatical relations, sentences and larger passages preserve different evidence [1]. Changing the selected context changes the observations available for comparison. The method must define its passage boundaries before treating the resulting count matrix and reference statistics as fixed.

#### Why counts do not determine meaning

Consider the sentences “the doctor questioned the patient” and “the patient questioned the doctor.” Their word counts are identical, but the roles of doctor and patient are reversed. Under the same vocabulary and word weights, the two sentences produce the same numerical row. Normalization and the later distance calculations cannot recover an order distinction that the counts have discarded. They measure one aspect of word use, not the complete interpretation of the passage.

Aggregation changes the level of description. A word's profile across clusters summarizes many occurrences, whereas BERT represents a particular occurrence in its sequence. A single corpus-wide CV compresses that profile further and can hide which cluster generated a large deviation. We retain the full group-conditioned profile for learning and keep the one-score diagnostic as a separately interpretable summary.

Firth's distinctions help explain what these two representations retain [14]. Collocation concerns recurring lexical company, colligation concerns grammatical relationships, and context of situation concerns the circumstances of use. A broad passage may identify a topic, while a negation or pronoun changes how a particular sentence should be understood. The count matrix records selected distributional regularities. The ordered text supplies additional evidence to the reader and the encoder.

#### Defining a passage as an observation

A fixed word window, a sentence and a whole document make different observations. A short window can omit a pronoun's antecedent, while a long document can combine several topics. The selected passage should therefore retain its source identifier and offsets, and word occurrences should retain their spans within it. These records make the scope of each numerical row visible and allow the analysis to return to the original language.

Each passage supplies a count-matrix row and a link to its original text. Each target occurrence additionally records its vocabulary identifier, character span and corresponding BERT WordPieces. Multiple occurrences in one passage share its TF-IDF row while retaining different contextual encoder states. Independent occurrence labels define the supervised task.

The connection between language and the mathematics is now explicit. Passage boundaries define the observations. Vocabulary identities define their measured coordinates. Grouping, variation and matrix reduction operate on those measurements. The retained source record allows their results to be interpreted in relation to the text. The mathematical calculation and its linguistic interpretation remain connected through these identities.

### Representing a linguistic context numerically

#### From word distributions to a context vector

A geometric comparison begins only after the textual observation has been defined. Schütze's Dimensions of Meaning and Word Space accounts connect corpus-derived word vectors with representations of particular contexts [15, 16]. A word vector summarizes its co-occurrence pattern across the corpus. A context vector combines, for example by averaging, the word vectors found around a particular use. Thus a context containing suit together with court and law can receive a different representation from one containing suit with cloth and jacket, even though the investigated word is the same. Here the average is over surrounding word vectors. The group mean used later averages passage rows, so it summarizes a different set of objects.

This gives a useful distinction between first-order and second-order representations. A first-order row records the words observed in a passage. A second-order vector combines corpus-derived representations of those words, so different immediate wording can still produce related context vectors. Schütze's word-sense discrimination model weights context-word vectors by logarithmic inverse document frequency [2]. His local feature selection considers positions up to 25 words on either side of a target. That window defines a particular measurement procedure. It is not a universal linguistic boundary, and weighting word vectors in this way is different from the direct passage TF-IDF rows used by the present diagnostic.

### Selecting coherent passages

Selecting a context is a separate problem from representing one. Hearst's TextTiling uses changes in lexical cohesion to locate subtopic boundaries [17, 18, 19, 20]. It compares adjacent blocks formed from fixed-size token sequences. Valleys in the smoothed similarity sequence, measured relative to neighboring peaks, identify candidate boundaries that can be adjusted to paragraph breaks. The final topical segments can therefore have different lengths even though the internal comparisons use fixed units. Early work used TF-IDF, whereas the later block-comparison account used term frequencies. A topical boundary organizes subject matter without guaranteeing that every pronoun or word use is interpretable within the resulting segment.

Kaufmann's VecTile makes a direct connection to Word Space [21, 22]. It sums corpus-derived word vectors for adjacent windows and compares the resulting vectors by cosine. This second-order comparison can relate windows whose words differ but whose corpus associations are similar. Choi's method takes another route: it converts sentence cosine similarities into local ranks and uses divisive grouping to locate boundaries [23]. Utiyama and Isahara's method instead assigns costs from a probabilistic segmentation model and finds a minimum-cost path by dynamic programming [24]. These approaches change the evidence or objective used to choose boundaries. Their shared output does not make their assumptions interchangeable.

Lexical cohesion has also supported word-sense disambiguation, and context-clustering systems have compared vector and similarity representations [25, 26, 27]. Models separating local sense from document topic make the remaining distinction explicit: a broad subject need not determine the meaning of a particular occurrence [28]. For the present paper, selecting passage boundaries determines the rows, word counts and IDF reference. Changing those choices can alter normalized distances and fitted groups. Segmentation must therefore be assessed against its own reference boundaries, while the diagnostic and classifier are assessed for their own stated outputs.

The calculations use finite real vectors and matrices. A scalar is one number, a vector is an ordered list of numbers, and a matrix arranges these lists in rows and columns. Here a row describes an observation and a column identifies a measurement. The Euclidean inner product, or dot product, multiplies matching coordinates and adds the products. Taking the square root of a vector's inner product with itself gives its Euclidean length, also called its L2 norm. Two vectors are orthogonal when their inner product is zero. An orthonormal basis consists of perpendicular unit directions. These definitions supply the geometry used to compare passage rows. Transposing a matrix exchanges its rows and columns. Matrix multiplication combines compatible row and column dimensions.

#### Keeping word contributions identifiable

The vector-space representation gives every retained word a fixed column. Each passage is a row of weights on those columns, and its group centroid is the mean of the rows assigned to that group [29]. A passage weight and the corresponding centroid weight therefore refer to the same word. Their difference can be retained even after the full passage vectors have been used to form groups.

This shared coordinate system is what makes the diagnostic possible. TF-IDF determines each word's weight, row normalization sets the scale for comparing passages, and Euclidean k-means fits a center for each group. The full squared distance to a center is the sum of the squared differences on the individual word coordinates. We can therefore use the whole passage to select its reference group, then examine the word-by-word differences that make up that comparison.

The order matters. Reducing the vocabulary dimensions before this calculation would combine word coordinates and make their separate contributions harder to recover. Changing the normalization or grouping rule would change the reference centers. The method consequently calculates its word measurements in the original vocabulary coordinates, with the representation and fitted groups fixed before the distances are summarized.

The perpendicular axes used here are a mathematical construction. The basis vector for a word has a one in that word's position and zeros elsewhere. Distinct basis vectors have inner product zero, and each has length one. This does not say that words occur independently or that passages are perpendicular to one another. Related words can have correlated values on separate axes. The basis simply keeps the recorded measurements distinguishable.

⟨e[s],e[t]⟩ = 1 if s=t, otherwise 0,    x[i] = ∑[t=1..p] X[i,t]e[t],    ‖x[i]−μ[g]‖₂² = ∑[t=1..p](X[i,t]−μ[g,t])²

**Notation**

| Symbol | Definition |
| --- | --- |
| e | Standard vocabulary basis vectors, each containing one unit entry and zeros in the other positions. |
| X | Observation by vocabulary matrix of term weights. |
| x | Passage vector expressed in the stated vocabulary basis. |
| μ | Cluster centroid vectors in that same basis. |
| p | Number of retained vocabulary axes. |
| i | Passage index. |
| g | Cluster index. |
| s | First vocabulary axis index. |
| t | Second vocabulary axis index. |

To see the distance decomposition, write the passage-to-centroid difference as a sum along these basis directions. Taking its inner product with itself produces squared terms on the same axes and cross terms between different axes. The cross terms vanish because the basis directions are perpendicular. The remaining sum contains one squared difference for each word. Averaging passages to obtain a centroid preserves these column identities.

### Averages and variation

#### Why use a mean as the group representative?

To compare a passage with its group, we first need a representative of that group. Least squares chooses a representative by minimizing the sum of squared differences from the observations. Legendre published the method in 1805, and Gauss developed a probabilistic treatment in 1809 [30, 31]. The minimizing property itself can be established for fixed observations without a probability model. Represent each observation as a vector in the same coordinate system. With perpendicular unit axes, squared Euclidean distance is the sum of the squared coordinate differences. Correlations between measured features do not alter this coordinate identity.

d(x,y)² = ‖x − y‖₂² = ∑[t=1..p] (x[t] − y[t])²

**Notation**

| Symbol | Definition |
| --- | --- |
| d | Euclidean distance between compatible observation vectors. |
| x | Real p dimensional observation vector. |
| y | Real p dimensional observation vector in the same coordinate system. |
| p | Positive integer number of measured feature coordinates. |
| t | Feature index from 1 to p. |

Figures 1 and 2 show the calculation in two dimensions. Each matrix row becomes a point. A horizontal change of 4 and a vertical change of 3 produce a distance of 5 because 4² + 3² is 25. The example also shows why feature scales matter. Increasing one coordinate's scale changes its contribution to distance and may change which observations are nearest. In the corpus method, word weighting therefore helps determine the geometry of passage comparisons.

![Figure 1](figures/Work_coordinates.png)

**Figure 1. Six synthetic observations, shown both as matrix rows and as points in two dimensions.**

The rows are (1, 1), (2, 1), (1, 2), (5, 4), (6, 4) and (5, 5). The point labels preserve their row identities. The coordinates are illustrative measurements, not assigned meanings.

![Figure 2](figures/Work_distance.png)

**Figure 2. The distance from (1, 1) to (5, 4). Coordinate differences of 4 and 3 give Euclidean distance 5.**

The two points form the ends of a right triangle with horizontal side 4 and vertical side 3. Their squared distance is 16 + 9, or 25.

The arithmetic mean minimizes the total squared distance from the observations. To see why, consider any proposed center. Each observation's difference from that center can be written as its difference from the mean plus the mean's displacement from the proposed center. The following identity separates these two contributions. It shows exactly how much additional squared error results from choosing a center other than the mean.

μ = (1/n)∑[i=1..n] x[i],    ∑[i=1..n] ‖x[i] − a‖₂² = ∑[i=1..n] ‖x[i] − μ‖₂² + n‖μ − a‖₂²

**Notation**

| Symbol | Definition |
| --- | --- |
| μ | Real p dimensional mean vector of the fixed observations. |
| x | Collection of n real p dimensional observation vectors. |
| a | Arbitrary real p dimensional constant representative. |
| n | Positive integer number of observations. |
| p | Positive integer feature dimension. |
| i | Observation index from 1 to n. |

When the squared length is expanded, the cross term contains the sum of deviations from the mean. That sum is zero. The remaining error is the squared variation around the mean plus the number of observations times the squared displacement of the proposed center. The added term is nonnegative and vanishes only when the proposed center equals the mean. Thus the mean, also called the centroid, is the unique least-squares representative. This is why a k-means update averages the observations assigned to each cluster.

#### Variation within and between groups

Now divide the observations into nonempty groups, with each observation in exactly one group. A passage can differ from its group's mean, and the group mean can differ from the overall mean. The within-group sum of squares measures the first kind of variation. The between-group sum of squares measures the second, weighting each group mean by the number of observations it represents. Together they account for the total squared variation around the overall mean.

SSW = ∑[g=1..k]∑[i∈C[g]] ‖x[i] − μ[g]‖₂²,    SSB = ∑[g=1..k] n[g]‖μ[g] − μ‖₂²,    SST = SSW + SSB

**Notation**

| Symbol | Definition |
| --- | --- |
| SSW | Nonnegative scalar within group sum of squared deviations. |
| SSB | Nonnegative scalar between group sum of squared deviations. |
| SST | Nonnegative scalar total sum of squared deviations from the overall mean. |
| x | Collection of n fixed real p dimensional observations. |
| μ | Mean vector notation, with μ[g] the mean of group g and unindexed μ the overall mean. |
| C | Partition of observation indices into k nonempty groups. |
| n | Observation count notation, with n[g] the size of group g and n the total count. |
| k | Positive integer number of groups. |
| p | Feature dimension shared by observations and means. |
| g | Group index from 1 to k. |
| i | Observation index belonging to the stated group. |

Within each group, split an observation's deviation from the overall mean into these two parts. The deviations from that group's own mean sum to zero, so the cross term again disappears. Adding over groups proves the analysis-of-variance (ANOVA) identity above. The same calculation applies separately to each coordinate. We can therefore describe the variation of the whole collection and still identify how much each word coordinate contributes.

In the six-point example, group the first three observations together and the last three together. Their centroids are (4/3, 4/3) and (16/3, 13/3), and the overall mean is (10/3, 17/6). The within-group sum of squares is 8/3 and the between-group sum is 75/2. Adding them gives the total, 241/6. Figure 3 shows the distances used in this accounting. The observations stay fixed. Grouping changes which mean is used as their reference.

![Figure 3](figures/Work_variance.png)

**Figure 3. The six-point example split into two groups. Thin lines show deviations from group means. Heavier lines show the displacement of each group mean from the overall mean.**

The first three observations form one group and the last three form another. The within-group, between-group and total sums of squares are 8/3, 75/2 and 241/6, respectively.

![Figure 4](figures/Work_Cluster_Variance_3D.png)

**Figure 4. Within-group and between-group variation for twelve synthetic unit-length vectors in three dimensions. Solid lines join observations to their group means. Dashed lines join group means to the overall mean. Diamonds mark group means and the star marks the overall mean.**

There are four observations in each illustrative group. Within-group squared variation is 0.051705732, between-group variation is 3.308676244, and their total is 3.360381976. Dividing by the respective degrees of freedom gives mean squares of 0.005745081 and 1.654338122. Their Caliński–Harabasz ratio is 287.957301. The centroids are arithmetic means and are not renormalized. This example illustrates the accounting. The method chooses its group count through a separate search.

Figure 4 applies the same calculation to three coordinates. Each solid segment contributes an observation's squared distance from its group mean. Each dashed squared distance is multiplied by that group's size because the mean represents all of its observations. These two sums recover the total squared variation. The displayed three-group partition is an illustration. The method's procedure for choosing a group count is defined later.

#### Describing observed variation and making statistical inferences

The identities above describe the observations actually supplied. Using them to make claims about unobserved data requires additional assumptions. Student's work on small-sample means and Fisher's development of analysis of variance show how sampling models enter that step [32, 33, 34, 35, 36]. For this paper, the important distinction is between calculating a property of a fixed corpus and estimating a property of a wider population.

Variance is the expected squared deviation from a mean under a specified distribution. If every observed row receives equal weight, the empirical variance divides its squared-deviation sum by the number of rows. The usual sample variance instead divides by one fewer row. Under independent sampling from a common finite-variance distribution, that adjustment gives an unbiased estimator of the population variance. These denominators answer different questions. Our corpus diagnostic describes a declared finite reference collection, so its population moments use the full row count. Covariance measures how two centered quantities vary together and enters the next identity.

Var(U + V) = Var(U) + Var(V) + 2Cov(U,V)

**Notation**

| Symbol | Definition |
| --- | --- |
| U | Scalar random contribution with a finite second moment under the stated probability model. |
| V | Scalar random contribution with a finite second moment under that same model. |
| Var | Population variance under the model. |
| Cov | Population covariance under the model. |

To derive this formula, subtract each random quantity's mean, add the centered quantities and expand the square. Taking the expectation leaves their two variances and twice their covariance. The variances add without the extra term only when covariance is zero. This is different from the cancellation of centered residuals in the fixed-partition identity above. Correlated vocabulary measurements do not invalidate that Euclidean accounting.

Estimating a mean from n observations imposes one constraint on their residuals: they sum to zero. This leaves n − 1 residual directions and explains the sample-variance denominator. Under independent Gaussian sampling, the sample mean and residual sum of squares are independent. Student's t statistic uses that result to compare the sample mean with a hypothesized population mean after scaling by the estimated standard error. Its distributional guarantee depends on the sampling assumptions. It does not follow from a numerical variance calculation alone.

The classical ANOVA F test compares a between-group mean square with a within-group mean square. Its null distribution assumes predefined groups, independent Gaussian errors and a common positive error variance, with enough observations to leave positive residual degrees of freedom. Clustering instead chooses groups from the observed geometry. A ratio calculated on those groups can describe separation and compactness, but it does not automatically provide an F-test probability. The Caliński–Harabasz criterion used later is interpreted in this descriptive way.

The classical ANOVA degrees of freedom follow from the fitted means. The group means contribute k − 1 centered directions, and the within-group residuals contribute n − k. Under the Gaussian null model just stated, the corresponding standardized squared lengths are independent chi-squared quantities. Their mean-square ratio has an F distribution. The resulting tail probability concerns observations under that null model. It is not the probability that the null hypothesis is true, and it does not become valid merely because a clustering score has the same algebraic form.

For two predefined groups with a common error variance, the one-way ANOVA F statistic equals the square of the pooled two-sample t statistic. Both reduce the comparison to the difference between the group means relative to within-group variation. This connection joins Student's and Fisher's inferential developments. The corpus method borrows the accounting of variation, while using a descriptive clustering criterion instead of those sampling distributions.

The coefficient of variation asks how large a standard deviation is relative to the mean of the same measurements [37]. For a positive mean, it is their ratio. Multiplying the ratio by 100 expresses it as a percentage. Multiplying every measurement by one positive constant multiplies both the mean and standard deviation by that constant, so the ratio stays unchanged. In our diagnostic, the measurements are nonnegative absolute differences from matching centroid coordinates. Their CV describes unevenness relative to their average size. A high CV can occur even when all the differences are small, so it must be read alongside the underlying measurements.

### Grouping observations under a stated criterion

#### Two examples of grouping rules

Ward's method begins with individual observations and repeatedly merges the pair of groups that adds the least within-group squared deviation [38]. The recorded sequence of merges forms a hierarchy, usually drawn as a dendrogram. This differs from constructing a minimum spanning tree, which minimizes a sum of edge costs. Ward's method helps explain how the earlier least-squares identity can define a grouping rule. Our diagnostic uses k-means instead, fitting a partition separately for each candidate group count.

ΔW(A,B) = (nA nB / (nA + nB))‖μA − μB‖₂²

**Notation**

| Symbol | Definition |
| --- | --- |
| ΔW | Nonnegative scalar increase in within group sum of squares caused by the merge. |
| A | Nonempty set of observation indices in one current group. |
| B | Nonempty disjoint set of indices in the other group. |
| n | Group size notation, with nA and nB the positive sizes of the two groups. |
| μ | Mean vector notation, with μA and μB in the same Euclidean feature space. |

The merged centroid is the size-weighted average of the two original centroids. Replacing each group's own mean with the merged mean adds its size times its squared displacement from that merged mean. Adding the two penalties gives the displayed merge cost. Both group size and distance between centroids therefore affect which merge Ward's method chooses. The same least-squares identity underlies k-means, although its search procedure is different.

The shortest-dendrite approach of Florek and colleagues groups points by cutting selected edges of a minimum spanning tree: a connected, cycle-free graph containing every observation, with the smallest total edge length. In Figure 5, five edges connect the six observations, with lengths 1, 1, √18, 1 and 1. Cutting the long middle edge leaves the two triples used in the earlier example. Their geometry makes the results agree in this case. That agreement does not make the two grouping objectives identical or guarantee agreement on other data [39, 40].

![Figure 5](figures/Work_tree.png)

**Figure 5. A minimum spanning tree for the six synthetic observations. Removing its long middle edge separates the points into two components.**

The edges join 1–2, 1–3, 2–4, 4–5 and 4–6, with total length 4 + √18. Removing edge 2–4 separates the first three observations from the last three. This illustrates a graph-based grouping rule. The corpus diagnostic uses Euclidean k-means.

The direction of a ratio depends on what its terms measure. Salton, Wong and Yang describe a similarity-density ratio whose numerator is average similarity between group centroids and whose denominator is average similarity of documents to their own centroids [29]. Smaller values favor separation between groups and similarity within them. The Caliński–Harabasz criterion instead compares between-group squared separation with within-group squared variation, including count adjustments. It favors larger values. These directions follow from the definitions of similarity and distance, not from the mere use of a ratio.

### Graphs: defining relations and connectivity

#### Define the relation before drawing it

A graph represents objects as vertices and specified relationships as edges. Euler's Königsberg bridge problem illustrates the abstraction [41]. Vertices represent land regions and edges represent bridges. Several bridges may connect the same pair of regions, so the representation is a multigraph. The map's exact shape is unnecessary for asking which regions are connected. The same separation matters in a corpus network: vertex and edge definitions determine the relation being studied, while the drawing displays it.

The bridge problem asks whether a route can use every bridge exactly once. In graph terminology, this route is a trail: edges may not repeat, although vertices may. Whenever the route enters an intermediate vertex, it must leave on another edge, using the incident edges in pairs. Only the starting and ending vertices can therefore have odd degree, where degree counts incident edge ends. Figure 6 has four odd-degree vertices, so such a trail is impossible. Rearranging the drawing cannot change that conclusion because the connections remain the same.

![Figure 6](figures/Work_bridges.png)

**Figure 6. A multigraph representing seven bridges. Parallel curves represent different bridges between the same regions. The vertex degrees are 5, 3, 3 and 3.**

Vertices A, B, C and D represent four land regions. Two edges join A to B, two join A to C, and one edge joins each of A to D, B to D and C to D. All four degrees are odd, which rules out a trail using every edge exactly once.

For a corpus graph, a vertex might represent a document, a passage, a word or a lexical sense. An edge might record co-occurrence, a grammatical relation or a measured difference. These choices define the object being studied. The drawing is only a display of that object. A crossing without a vertex does not create a connection, and a long line need not represent a large contextual distance. Later, our word-to-cluster graph will record specific coordinate comparisons and retain this distinction between an edge's meaning and its appearance.

A path follows edges from one vertex to another without repeating vertices. A connected component is a maximal set of vertices reachable from one another, and a cycle returns to its starting vertex without repeating the other vertices. These definitions concern the recorded connections. They remain unchanged when vertices move in a drawing, and they give precise meanings to the connectivity and tree constructions that follow.

#### Describing a graph with matrices

An adjacency matrix places the weight of each edge in the row and column of its endpoints. Consider an undirected graph with nonnegative weights. Its adjacency matrix is symmetric, and the sum of the weights incident on a vertex is its strength. Subtracting adjacency from the diagonal matrix of strengths gives the graph Laplacian. To understand what this matrix measures, assign a number to each vertex. The expression below adds the squared differences between numbers at connected endpoints, weighted by their edges.

Δ[i,i] = ∑[j=1..v] A[i,j],    L = Δ − A,    zᵀLz = ½∑[i=1..v]∑[j=1..v] A[i,j](z[i] − z[j])² ≥ 0

**Notation**

| Symbol | Definition |
| --- | --- |
| A | Symmetric nonnegative v × v adjacency matrix of the declared graph. |
| Δ | Diagonal v × v matrix of vertex strengths, with off diagonal entries zero. |
| L | Real v × v graph Laplacian. |
| z | Arbitrary real v dimensional vector assigning a scalar to each vertex. |
| v | Positive integer number of vertices. |
| i | Vertex index from 1 to v. |
| j | Vertex index from 1 to v. |

Expanding each squared difference proves the identity. The squared endpoint terms combine into the diagonal strength term, while the products of endpoint values give the adjacency term. Every weighted square is nonnegative, so the result cannot be negative. This is what positive semidefinite means for the symmetric Laplacian. The result is zero exactly when each positive-weight edge joins equal values. Following edges through a connected component then forces every vertex in that component to have the same value. Different components may have different constants. Consequently, the null space, the set of vectors mapped to zero, has one independent constant direction for each component. The argument relies on undirected, nonnegative weights.

An eigenvector is a nonzero vector whose direction is unchanged by a matrix, although its length or sign may change. The multiplier is its eigenvalue. For a real symmetric matrix, orthonormal eigenvectors provide a basis for describing its action. Fiedler studied the second-smallest Laplacian eigenvalue as algebraic connectivity [42]. For a graph with at least two vertices under the stated nonnegative-weight assumptions, it is positive exactly when the positive-weight graph is connected. The four-cycle in Figure 7 has eigenvalues 0, 2, 2 and 4 in both drawings. Its connectivity is a property of the graph, independent of its layout.

The nonnegative quadratic form also explains why the Laplacian's eigenvalues are nonnegative: applying it to an eigenvector gives that eigenvalue times the vector's squared length. Zero-eigenvalue directions span the null space. We will use the same relationship between a symmetric matrix, its quadratic form and its eigenvectors when constructing the singular value decomposition of a rectangular data matrix.

![Figure 7](figures/Work_topology.png)

**Figure 7. Two drawings of the same four-cycle. Moving the vertices changes the layout but leaves the adjacency matrix, Laplacian and eigenvalues unchanged.**

The edges join a to b, b to c, c to d and d to a. The adjacency matrix has ones at those symmetric positions and zeros elsewhere. The Laplacian has 2 on its diagonal and −1 at adjacent off-diagonal positions. Its eigenvalues are 0, 2, 2 and 4.

#### Trees and linguistic relations

A tree is a connected graph with no cycles. A spanning tree includes every vertex of a connected graph. Kirchhoff's analysis of electrical networks connected systems of current equations with choices of branches that leave no closed circuit [43]. This makes a useful link between relational structure and linear equations. Adding edge costs poses a different question: which spanning tree has the smallest total cost? The shortest-dendrite approach uses such a tree and cuts selected edges to form groups [39]. Ward's method instead chooses merges by their increase in squared deviation [38]. The resulting groups can coincide on an example without the methods optimizing the same quantity.

A visible network pattern also raises a question about its origin. Erdős and Rényi studied random graph formation, Watts and Strogatz examined the coexistence of local clustering and short paths, and Barabási and Albert modeled growth that favors already connected vertices [44, 45, 46]. These are different mechanisms, not interchangeable explanations for a corpus graph. They establish why interpretation needs a stated reference model. In this paper, the first requirement is more basic: identify how the language records generated the edges before interpreting the drawing.

A graph can also represent explicitly named semantic relations. Quillian modeled relations among word concepts, and WordNet groups lexical senses into synonym sets and connects them through specified relations [47, 48]. A word linked to two senses is a different object from a word linked to two groups of corpus passages. Figure 8 illustrates the distinction with bank. Our graph records relationships between word measurements and fitted passage groups. Those groups require interpretation. They are not sense labels supplied by the graph itself.

![Figure 8](figures/Work_semantic.png)

**Figure 8. The word bank in two different representations: a schematic relation to senses and a corpus association graph. The edge meanings differ.**

The sense schematic connects bank to a financial sense and a river-edge sense. The association graph connects bank to money, loan, shore and river, with additional money–loan and river–shore edges. The schematic is not a literal WordNet entry. An association edge does not itself identify a sense.

### Lexical networks and their communities

#### From passage–word records to two kinds of graph

A lexical network represents words as vertices and connects them under a stated extraction rule. Widdows and Dorow built a noun graph from corpus occurrences linked by the conjunctions “and” or “or”, weighting a link by how often the relation occurred [49]. The linguistic evidence defined the links. Girvan and Newman's community study, by contrast, addressed a different problem: how to divide an already specified network [50]. Their procedure repeatedly removed an edge used by many shortest routes, recalculating this edge-betweenness measure after each removal. Together these studies separate two decisions: what evidence creates an edge, and what criterion groups the resulting vertices. The inspection graph used here has another role. It connects words to already fitted passage groups and records their measurements.

Before comparing passages or words, the nonnegative passage-by-word matrix can be read as a bipartite graph. Passages form one vertex set and word features form the other. Each positive entry gives an edge and its weight, recording which feature contributes to which passage. This retains the weighted incidence but not word order. Comparing two rows then asks which weighted word features the passages share. Comparing two columns asks which passages contribute to both word features. Multiplying the matrix by its transpose gives the row comparisons. Reversing the order gives the column comparisons. The resulting Gram matrices describe two projections of the same records, with different vertex sets and edge meanings.

R = XXᵀ ∈ ℝ^(n × n),    K = XᵀX ∈ ℝ^(p × p),    X = D F J,    R = D F J² Fᵀ D,    K = J Fᵀ D² F J

**Notation**

| Symbol | Definition |
| --- | --- |
| R | Observation Gram matrix of the row normalized passage vectors. |
| K | Vocabulary Gram matrix of those same measurements. |
| X | Row L2 normalized n × p TF IDF matrix. |
| F | Nonnegative n × p raw count matrix. |
| J | Nonnegative diagonal p × p matrix of regular logarithmic IDF values. |
| D | Diagonal n × n matrix with the reciprocal unnormalized row length for each positive length row and zero for a zero row. |
| n | Number of passage observations. |
| p | Number of retained vocabulary axes. |

An entry in the passage Gram matrix sums products over matching word coordinates. An entry in the word Gram matrix sums products over matching passages. Their connection to SVD is exact: the two products have the same positive eigenvalues, equal to the squared singular values of the passage matrix. The remaining identities expand the calculation into counts, IDF weights and row-normalization factors. They show where each preprocessing choice enters. They do not imply that clustering words and clustering passages will produce matching groups.

These products record inner products, not covariances. Covariance requires centering and the chosen normalization as well. To turn a Gram matrix into a graph, we must also decide whether to remove self-connections, normalize weights or discard weak edges. Those decisions can alter its spectrum and communities. A reduced-rank reconstruction can contain negative entries even when the original matrix is nonnegative, so it cannot be treated automatically as a nonnegative affinity graph.

![Figure 9](figures/Work_projections.png)

**Figure 9. Two projections of the same passage–word records. Row comparisons connect passages through shared words. Column comparisons connect words through shared passages.**

Six binary passage rows use five columns: bank, river, loan, credit and flow. The rows are 11000, 11000, 10100, 10110, 01001 and 00110. The row Gram product counts shared vocabulary between passages. The column Gram product counts shared passages between words. The diagonal entries are self-counts and are removed for the simple graphs shown.

#### Finding communities in an affinity graph

A community is a group of vertices selected according to a network criterion. Merely rewarding internal connections would favor putting every vertex in one group. Newman and Girvan's modularity comparison instead evaluates internal connectivity against a reference based on the vertices' degrees [51]. The weighted form below uses strengths and includes a resolution parameter that changes the reference scale. It applies to an undirected graph with nonnegative weights and positive total weight. This criterion helps interpret lexical communities, while the paper's word-to-cluster inspection records retain the passage groups already fitted by k-means.

s[t] = ∑[u=1..p] A[t,u],    Ω = ½∑[t=1..p] s[t],    Qmod = (1/(2Ω))∑[t=1..p]∑[u=1..p] (A[t,u] − γs[t]s[u]/(2Ω))𝟙[b[t] = b[u]]

**Notation**

| Symbol | Definition |
| --- | --- |
| s | Nonnegative p dimensional vector of lexical node strengths. |
| A | Symmetric nonnegative p × p adjacency matrix of the fixed lexical graph. |
| Ω | Positive scalar total undirected edge weight, requiring at least one positive edge. |
| Qmod | Scalar modularity objective for the stated graph and partition. |
| γ | Positive scalar resolution parameter. |
| b | Integer community assignment for every vocabulary vertex. |
| p | Number of vocabulary vertices. |
| t | Vocabulary vertex index from 1 to p. |
| u | Vocabulary vertex index from 1 to p. |
| 𝟙 | Indicator of equality of the two community labels. |

A community partition depends on both its objective and the algorithm used to search for it. Louvain seeks high modularity through local changes, while Leiden adds refinement to address connectivity problems [52, 53]. A better search does not remove every limitation of the objective. Fortunato and Barthélemy showed that standard modularity can favor merging small, internally dense groups because its reference scale depends on the whole network [54]. The resulting groups therefore depend on the chosen graph and scale, even before any linguistic interpretation. Edge meaning also remains essential: a larger distance expresses separation, whereas a larger affinity weight expresses a stronger connection.

#### Connections within and across communities

Community membership does not describe how a vertex connects beyond its own group. Guimerà and Amaral's account of network roles combined within-module degree with a participation coefficient that describes the distribution of links across modules [55]. We use the analogous weighted form here. For one word, add the edge weights reaching each community and divide those totals by the word's total connection strength. The proportions sum to one. Squaring them, adding the squares and subtracting from one gives a small value for concentrated connections and a larger value for a more even spread. A node with zero total strength has no defined proportions and receives an unavailable value.

s[t,h] = ∑[u:b[u]=h] A[t,u],    P[t] = 1 − ∑[h=1..g] (s[t,h]/s[t])²,    s[t] > 0

**Notation**

| Symbol | Definition |
| --- | --- |
| s | Strength notation, with s[t,h] the strength to community h and s[t] the total strength. |
| A | Nonnegative lexical adjacency matrix. |
| b | Fixed vertex to community assignment. |
| P | Participation vector defined for vertices of positive total strength. |
| g | Positive integer number of communities in the fixed partition. |
| p | Number of vocabulary vertices. |
| t | Vocabulary vertex index from 1 to p. |
| h | Community index from 1 to g, including communities receiving zero strength from t. |
| u | Vocabulary vertex index satisfying the indicated community condition. |

All connection strength reaching one community gives participation zero. Equal strength reaching two communities gives one half. Equal strength reaching all g communities gives one minus the reciprocal of g. Figure 10 contrasts this connection pattern with word weights across passage groups. The figure makes the measurement distinction visible: one panel concerns corpus weights, while the other concerns graph edges. Neither panel displays the passage-to-centroid distance distribution used by the main diagnostic.

![Figure 10](figures/Work_roles.png)

**Figure 10. Word weights across passage groups and a word’s connections across graph communities describe different measurements. Neither panel is the main coordinate-distance diagnostic.**

The left panel shows synthetic word weights in two passage groups, with means 0.6825 and 0.085. The right panel gives one word equal connection strength to two graph communities, producing participation one half. A difference in passage weights and a spread of graph connections can be examined together without treating them as the same quantity.

The corresponding weighted within-community descriptor compares a node's internal connection strength with the mean internal strength of nodes in its community, then divides the difference by their standard deviation. It extends the within-module degree z-score of Guimerà and Amaral [55] and requires a positive standard deviation. Participation describes spread across communities, while the standardized internal strength describes prominence within one community. A node can be prominent locally and still have few connections outside its own group.

We can also calculate a coefficient of variation across the same community-strength totals. Include every fixed community, including those receiving zero strength. The mean of these totals is the word's total strength divided by the number of communities. Using population variance gives the identity below. It links two summaries of the same graph measurements and reveals when they repeat information.

CVcommunity[t]² = g(1 − P[t]) − 1

**Notation**

| Symbol | Definition |
| --- | --- |
| CVcommunity | Population coefficient of variation across all g community strengths for each positive strength vocabulary vertex. |
| g | Fixed positive integer number of graph communities, including zero strength entries. |
| P | Weighted participation vector for the same graph and partition. |
| t | Vocabulary vertex index with positive total strength. |

Divide the variance of the community strengths by their squared mean. Expanding the variance leaves the number of communities multiplied by the sum of squared strength proportions, minus one. Participation is one minus that same sum, which gives the identity. For a fixed number of communities, either value determines the other. Agreement between them is therefore an algebraic consequence, not a second source of evidence. The identity does not apply to the main diagnostic's distances across passages, because those are different observations.

### Singular value decomposition: from bilinear forms to approximation

#### What singular value decomposition preserves

A matrix can be difficult to understand entry by entry. Singular value decomposition (SVD) describes its action through paired orthogonal directions in its input and output spaces. The underlying question arose in the study of bilinear forms, which depend linearly on each of two vector arguments. Beltrami and Jordan examined how separate orthogonal changes of those two coordinate systems could simplify the relationship [56, 57]. This differs from diagonalizing one symmetric matrix in a single basis. The modern decomposition pairs each input direction with an output direction and a nonnegative scaling factor, called a singular value. We first establish the complete factorization, then examine what is lost when only some directions are retained [58].

The construction starts with the product of the matrix's transpose and the matrix itself. This product is symmetric, and its quadratic form is a squared length, so it is positive semidefinite. Its orthonormal eigenvectors give input directions and its nonnegative eigenvalues give squared singular values. For each positive singular value, apply the original matrix to the corresponding input direction and divide by that value. This produces a unit output direction. Completing the input and output bases gives the factorization below.

M = UΣVᵀ,    UᵀU = Iₙ,    VᵀV = Iₚ,    Mv[j] = σ[j]u[j],    Mᵀu[j] = σ[j]v[j]

**Notation**

| Symbol | Definition |
| --- | --- |
| M | Arbitrary real n × p matrix, treated as a linear map from p to n coordinates. |
| U | Real n × n orthogonal matrix of output singular directions. |
| Σ | Real n × p rectangular diagonal matrix of nonnegative singular values. |
| V | Real p × p orthogonal matrix of input singular directions. |
| I | Identity matrix notation, with its dimension given by the index. |
| u | Columns of U, each a real n dimensional vector. |
| v | Columns of V, each a real p dimensional vector. |
| σ | Nonnegative singular value sequence in nonincreasing order. |
| n | Positive integer output dimension and observation count when M is a data matrix. |
| p | Positive integer input dimension and feature count when M is a data matrix. |
| j | Paired nonzero singular direction index from 1 to rank(M). |

Each paired equation states the matrix's action on one direction: it maps an input direction to its paired output direction, scaled by the singular value. Adding these actions reconstructs the matrix. The matrix maps its input null space to zero. The representation need not be unique. Paired vectors may change signs together, and directions associated with repeated singular values may be rotated within their shared subspace without changing the reconstructed matrix.

The two matrix products compare different objects. Multiplying the passage matrix by its transpose gives inner products between passage rows. Reversing the order gives inner products between vocabulary columns. These Gram matrices share the same positive eigenvalues, equal to the squared singular values, but their eigenvectors live in different spaces. This is a precise connection between passage and vocabulary structure, not an assertion that passages and words form the same groups. Golub and Kahan, and later Golub and Reinsch, developed practical methods for computing the decomposition [59, 60]. The passage and word Gram matrices introduced above therefore describe two sides of the same singular decomposition.

Latent semantic analysis applies a reduced singular representation to a term–document matrix [61]. Its coordinates combine vocabulary features, allowing documents to be related through distributional patterns. The interpretation still depends on how the matrix was built. We must therefore define the passages and vocabulary before reducing their matrix. In the method developed here, SVD supplies additional classifier features only after the original word-coordinate measurements have been calculated and retained.

#### What compression discards

Full SVD retains the complete matrix. Truncated SVD keeps only a chosen number of leading singular directions. Multiplying a passage row by the retained feature directions gives a shorter vector of coordinates. Mapping those coordinates back into vocabulary space reconstructs only the retained part of the row. The difference from the original is the discarded part. The following equation states its total squared reconstruction error.

T = V[:,1..q],    Z = MT,    M̂ = ZTᵀ,    ‖M − M̂‖F² = ∑[j=q+1..r] σ[j]²

**Notation**

| Symbol | Definition |
| --- | --- |
| T | Real p × q matrix of retained orthonormal right singular directions. |
| V | Right singular vector matrix of M. |
| Z | Real n × q matrix of projected observation coordinates. |
| M | Original real n × p matrix. |
| M̂ | Real n × p rank q reconstruction in original feature coordinates. |
| σ | Singular values of M in nonincreasing order. |
| q | Retained integer rank from 1 to r. |
| r | Rank of M, assumed positive here. |
| n | Number of observations. |
| p | Number of original features. |
| j | Discarded singular direction index from q + 1 to r. |
| ‖ · ‖F | Frobenius norm, whose square sums all squared matrix entries. |

The Eckart–Young approximation theorem shows that keeping the leading singular directions gives the smallest Frobenius reconstruction error among matrices of the allowed maximum rank [62]. The squared Frobenius norm is the sum of squared entries. To see why the largest singular values matter, consider projection onto any q-dimensional subspace. Each singular direction contributes a fraction between 0 and 1 of its squared singular value, and these fractions together cannot exceed q. The retained sum is therefore largest when the q largest contributions are kept in full. Any matrix of rank at most q has a row space of dimension at most q, and projecting the original matrix onto that space cannot be less accurate than that candidate. This extends the argument from projections to all rank-constrained reconstructions.

Mirsky extended this approximation result to other matrix norms that are unchanged by orthogonal coordinate transformations [63]. These are numerical guarantees. They do not guarantee that the retained directions preserve every linguistic distinction. Nor is each singular vector necessarily stable: near repeated singular values, individual directions can rotate substantially even when the singular values change little [58]. This is why the diagnostic keeps its word measurements on the original vocabulary axes and treats the reduced directions as auxiliary features.

An orthogonal projection separates a vector into perpendicular retained and discarded parts. The Pythagorean theorem therefore adds their squared lengths. Projection also commutes with averaging: projecting a group mean gives the mean of the projected group. We can apply the same separation to every residual used in the earlier within-group, between-group and total sums of squares. For a fixed partition, each sum divides into a retained and a discarded contribution.

‖a‖₂² = ‖P a‖₂² + ‖(Iₚ − P)a‖₂²,    SST = SSTret + SSTdisc,    SSW = SSWret + SSWdisc,    SSB = SSBret + SSBdisc

**Notation**

| Symbol | Definition |
| --- | --- |
| a | Arbitrary real p dimensional difference or centered residual vector. |
| P | Real p × p orthogonal projector TTᵀ, satisfying Pᵀ = P and P² = P. |
| I | Identity matrix notation. |
| p | Original feature dimension. |
| SST | Total sum of squares notation, with ret and disc denoting retained and discarded components. |
| SSW | Within group sum of squares notation with the same component labels. |
| SSB | Between group sum of squares notation with the same component labels. |
| ret | Label for the retained orthogonal subspace. |
| disc | Label for its discarded orthogonal complement. |

The retained and discarded parts are orthogonal, so their cross term is zero. Applying this fact to each observation-to-mean residual and each displacement between means gives the displayed decompositions. A projection cannot increase a pairwise distance, but it can shorten different distances by different amounts. Nearest neighbors and fitted groups can therefore change after reduction. In our method, grouping and word-coordinate diagnosis are completed before the auxiliary SVD features are formed.

Consider three rows: (10, 0), (0, 1) and (0, 2). Their singular values are 10 and √5. A rank-one truncated SVD keeps the first coordinate because it carries more squared magnitude. The other two rows both become zero in the reduced representation, even though they were different in the original data. This is the optimal rank-one reconstruction under squared error. If a useful distinction depended on the second coordinate, however, compression would remove it. Small reconstruction error and preservation of every useful distinction are therefore different requirements.

Centering and compression are separate choices. Principal component analysis (PCA) first subtracts each column's mean, then finds singular directions describing variation around that mean. Uncentered SVD approximates the original matrix. The method uses the latter for its auxiliary features, keeping the reference matrix itself as the object being approximated.

### How bidirectional encoders represent ordered language

#### From token identifiers to contextual states

BERT uses the order of the words that the count matrix leaves out. Its tokenizer first converts the text into token identifiers. Each identifier selects a learned vector from an embedding table. The integer itself is not the representation. Mikolov and colleagues' word-vector models and Pennington and colleagues' GloVe assign the same stored vector to a vocabulary entry each time it is used [64, 65]. A contextual encoder then changes the representation according to the surrounding sequence. This gives the classifier information that a fixed corpus-wide word profile cannot supply on its own.

A supervised neural model learns from predictions paired with independently assigned labels. It maps input features through learned matrices, biases and nonlinear functions, then measures prediction error with a loss. Backpropagation applies the chain rule to calculate how that loss changes with the trainable parameters, and an optimizer uses those derivatives to update them [66]. The chosen labels define the prediction task. The corpus clusters and diagnostic scores are input information, not automatically the labels to be predicted.

A gradient collects the derivatives of a scalar loss with respect to parameters. A Jacobian collects the derivatives of a vector output with respect to its inputs. The chain rule connects these derivatives through successive model operations. This distinction matters when some components are fixed: a value can affect the prediction even though the process that produced it is not being trained. In the legacy passage interface, BERT and the corpus calculations supply fixed features, while the added classifier learns how to use them. In the occurrence-level interface developed below, the corpus statistics remain fixed while the prediction head and BERT's final encoder block are trained.

Recurrent models pass information through a sequence by updating a hidden state one position at a time [67]. Repeated updates can weaken or amplify derivatives over long distances. Long short-term memory and gated recurrent units use gates to control what is retained and changed [68, 69]. They illustrate the problem that contextual models must solve: information from one part of a sequence must remain available where it is needed later.

A decoder that receives only one fixed source summary must recover all later output decisions from that summary [70]. Bahdanau, Cho and Bengio's attention model lets each output step combine the source states it needs [71]. The Transformer makes attention central to sequence processing itself [72]. Its encoder compares positions directly without carrying every interaction through recurrent updates. The following calculation explains how those comparisons determine which information is returned.

#### Comparing positions and combining their information

An attention score measures compatibility before it becomes a weight. Several scoring functions are possible, including a learned nonlinear function, a dot product or a bilinear comparison [73]. Softmax converts the permitted scores for one retrieval into nonnegative weights summing to one. A weighted sum then combines the associated value vectors. Keeping comparison, normalization and combination separate makes the complete calculation easier to follow.

Queries, keys and values name three roles in this retrieval. The query represents the position seeking information. Each key is compared with that query to determine a weight. The corresponding value supplies the information that will be combined using that weight. Separating the vectors used for selection from the vectors returned as content also appears in memory-network models [74].

In self-attention, all three sets of vectors are obtained from the current sequence states by separate learned projections [72]. Query and key vectors need the same width so their dot products are defined. The value vectors can have another width because they are combined only after the weights have been calculated. The displayed equation follows this order, including score scaling and masking. The hidden features belong to token positions, so a row of vocabulary-wide TF-IDF weights is not a substitute for one of these token states.

Q = HWQ,    Ka = HWK,    Va = HWV,    S = QKaᵀ/√dkey,    Γ = softmaxrows(S + Mmask),    O = ΓVa

**Notation**

| Symbol | Definition |
| --- | --- |
| H | Real ℓ × dmodel current hidden state matrix, with one row per sequence position. This display omits projection biases. |
| WQ | Trainable dmodel × dkey query projection matrix, written W with label Q in typeset mathematics. The bias-free form is used here. |
| WK | Trainable dmodel × dkey key projection matrix, written W with label K. |
| WV | Trainable dmodel × dvalue value projection matrix, written W with label V. |
| Q | Real ℓ × dkey query matrix. |
| Ka | Real ℓ × dkey attention key matrix, distinct from the corpus Gram matrix K. |
| Va | Real ℓ × dvalue attention value matrix, distinct from the SVD basis V. |
| S | Real ℓ × ℓ compatibility score matrix before masking. |
| Γ | ℓ × ℓ attention weight matrix with nonnegative rows summing to one before attention dropout. |
| Mmask | ℓ × ℓ additive mask, zero on permitted interactions and negative infinity on excluded ones. |
| O | Real ℓ × dvalue retrieved output matrix. |
| ℓ | Positive integer number of sequence positions. |
| dmodel | Positive integer hidden dimension. |
| dkey | Positive integer shared query and key dimension. |
| dvalue | Positive integer value dimension. |
| softmaxrows | Row wise exponential normalization over permitted finite scores, requiring at least one permitted key in every evaluated row. |

The query and key projections determine which positions receive high comparison scores. The value projection determines what those positions contribute. The displayed equation omits projection biases to show the basic matrix calculation. BERT's actual query, key and value layers also include learned biases. In the simplified form, expanding the query-key product gives a learned bilinear comparison. With biases, additional affine terms appear. Either form can be asymmetric. These scores are learned comparisons between token states, not the corpus weights or distances measured by the diagnostic.

The internal query and key coordinates are not uniquely determined by the attention scores. Multiply every query by an invertible matrix and every key by its inverse transpose. The two changes cancel when a query is multiplied by a key, leaving all scores unchanged. Different coordinates can therefore produce the same attention behavior. This is one reason to avoid assigning a unique linguistic meaning to a hidden coordinate solely from its position in the calculation.

#### Score scaling, softmax and learning

Why divide a dot-product score by the square root of the key width? Consider a reference calculation in which all query and key coordinates are independent, centered and have variance one. Each matched coordinate product then has variance one. Summing one such product per coordinate makes the score variance equal to the key width. Division by its square root brings the variance back to one. This motivates the scaling rule without assuming that trained representations continue to satisfy the reference assumptions.

Softmax responds to differences between scores. Adding the same constant to a whole row changes neither its weights nor their sum. Large differences can concentrate almost all weight on a single position. The derivative below shows how this concentration changes the sensitivity of the weights, and therefore how a later loss can affect the attention calculation.

a[j] = exp(s[j])/∑[r=1..ℓ] exp(s[r]),    ∂a[j]/∂s[r] = a[j](𝟙[j=r] − a[r])

**Notation**

| Symbol | Definition |
| --- | --- |
| a | Real ℓ dimensional weight vector for one permitted attention row. |
| s | Real ℓ dimensional score vector for that row, after restricting to permitted finite keys. |
| ℓ | Positive integer number of permitted keys in this formula. |
| j | Key index from 1 to ℓ. |
| r | Score coordinate index from 1 to ℓ. |
| 𝟙 | Equality indicator for the two indices. |

Applying the quotient rule to the softmax expression gives a derivative written entirely in terms of its output weights. A weight near zero has a small multiplicative factor, while a weight near one has a small derivative with respect to its own score. For numerical evaluation, subtract the largest finite score before exponentiating. The common shift leaves the result unchanged and reduces overflow risk. Each evaluated row must contain at least one permitted finite score. Excluding every position leaves no defined normalization.

For a small example, take a unit query along the first coordinate axis and two unit keys, one along each axis. With key width two, the scaled scores are about 0.7071 and zero. Softmax gives weights of approximately 0.669762 and 0.330238. If the two values point along those same axes, the returned vector has those weights as its coordinates. Changing only the values changes the content returned while leaving the comparison weights fixed.

Before attention dropout, the returned vector is a convex combination of the value vectors: its weights are nonnegative and sum to one. It therefore lies within their convex hull. This statement concerns the weighted-sum step. Later output projections, residual additions and nonlinear operations can take the complete encoder state outside that hull.

#### Multiple heads and sequence order

Multi-head attention repeats this calculation with several sets of learned projections. Each head can compare positions in a different way and return a different combination of values. The outputs are placed side by side and projected back to the model's hidden width. This operation combines attention heads inside BERT. The later concatenation of corpus features with a BERT output happens outside the encoder and serves a different purpose.

Yhead = concat(O[1],…,O[hcount])WO

**Notation**

| Symbol | Definition |
| --- | --- |
| Yhead | Real ℓ × dmodel multi head output matrix. |
| O | Collection of hcount head outputs, each a real ℓ × dvalue matrix. |
| WO | Trainable matrix with hcount times dvalue rows and dmodel columns. |
| hcount | Positive integer number of attention heads. |
| ℓ | Sequence length. |
| dvalue | Value width of each head in this equal width construction. |
| dmodel | Hidden width returned to the surrounding layer. |
| concat | Concatenation along the feature axis, producing ℓ rows and hcount times dvalue columns. |

Several heads provide opportunities to learn different patterns, but they need not all contribute distinct information. Experiments removing heads have found redundancy that depends on the model, task and layer [75]. Likewise, adding corpus features to a classifier creates capacity to use those measurements. Whether that capacity improves prediction must be established by comparison with appropriate baselines.

Attention needs positional information to distinguish sequence order. Without it, and with no mask or a correspondingly permuted mask, rearranging the input rows simply rearranges the output rows. This property is called permutation equivariance. Transformer positional encodings and BERT's learned position embeddings let the sequence positions affect the calculation [72, 76]. A count vector, in contrast, remains unchanged when its words are reordered.

Attention is one part of an encoder layer. A feedforward network transforms the features at each position with shared parameters and a nonlinear activation. The original Transformer uses a rectified linear activation, while BERT uses a Gaussian error linear unit. Residual connections add a sublayer's input to its output. Layer normalization centers and scales the hidden coordinates at a position, with a numerical stabilizer and learned scale and offset. Together these operations transform the retrieved information into the next sequence representation.

The next encoder layer receives states that already contain information gathered by earlier layers. Repeating this process lets later comparisons depend on increasingly transformed context. For a given input, an attention head can be viewed as a directed weighted relation between token positions. Its weights depend on the input and learned parameters. The diagnostic graph instead connects vocabulary items and fitted passage groups using stored corpus measurements.

Dense self-attention assigns a score to every pair of sequence positions. Doubling the sequence length therefore gives four times as many pairwise scores. Storing the full score matrix requires quadratic space, although actual memory use depends on how attention is implemented. Longformer reduces the interaction pattern to local and selected global attention [77]. Such choices address computational capacity. The separate linguistic question is how much source text must be retained to preserve the context being studied.

#### Using a pretrained BERT encoder

Context-sensitive representations and effective adaptation developed together. Peters and colleagues' ELMo combined forward and backward recurrent states into word representations that changed with context [78]. Howard and Ruder's ULMFiT showed how a pretrained recurrent language model could be adapted to text classification [79]. These approaches distinguish two questions: what context a representation contains, and which pretrained parameters a downstream task changes. Both questions matter when using a pretrained encoder with additional corpus features.

BERT combines a bidirectional Transformer encoder with a pretraining objective designed for that access to context [76]. Left and right context interact through every layer. Predicting selected tokens from modified input enabled bidirectional pretraining while withholding many target identities. Original BERT selected 15 percent of WordPiece positions. Of those selected positions, 80 percent were masked, 10 percent replaced by random tokens and 10 percent left unchanged. A second objective predicted whether two segments followed one another. These objectives produced a reusable encoder, commonly adapted by fine-tuning. Later work changed aspects of the pretraining procedure [80]. The integration below fine-tunes the final encoder block together with added prediction layers, while retaining the supplied embedding architecture and earlier blocks. This limited fine-tuning policy is an explicit implementation choice.

The tokenizer may divide a linguistic word into several WordPiece tokens. BERT combines each token's lookup vector with position and token-type embeddings, then computes contextual states. The legacy passage classifier uses the final [CLS] state to represent a passage. The selected occurrence classifier instead averages the contextual states of the target word's WordPieces, aligning that occurrence with its corpus-word coordinate. [SEP] marks segment boundaries, and the attention mask identifies padding.

The selected BERT Base configuration has 12 encoder layers, 12 attention heads per layer and hidden width 768. Each head uses key width 64, and an input has at most 512 positions including special tokens [76]. These dimensions are properties of the selected model. They set concrete requirements for the tokenizer, masks and classifier interface described in Methodology.

A representation must also be suited to the task being evaluated. Models trained to compare a context with candidate sense definitions answer a different question from models trained to compare whole sentences [81, 82]. Having a vector does not establish that every distance between such vectors measures the intended meaning. Here the corpus diagnostic measures a defined pattern of coordinate distances, while independently assigned occurrence labels determine what the selected classifier learns to predict.

A large attention weight shows where one computation places weight. Its value alone does not establish causal importance or a linguistic explanation. Research on attention-based explanations shows that the conclusion depends on the explanatory claim and how it is tested [83, 84]. The same discipline applies to the diagnostic: state what a number measures, then evaluate any further interpretation against independent evidence.

A pretrained BERT encoder and an added prediction head have different learning roles. The encoder converts ordered text into contextual states, and the head learns how those states and additional inputs relate to task labels. The legacy passage construction trains the added cluster embedding and prediction layers with a fixed encoder. The selected occurrence construction trains the prediction head and final encoder block, while retaining fixed embeddings and earlier blocks. Adapters and low-rank parameter updates define further adaptation procedures [76, 85, 86].

## Methodology

The methodological objective is to measure how identified words behave across corpus contexts and make those measurements usable for source inspection and supervised occurrence classification. The construction preserves passage, word and cluster identities because aggregating away those relationships would prevent a numerical departure from being traced to its language. Training passages define the TF-IDF geometry, the fitted groups and the full group-conditioned profiles. Coordinate-distance aggregation then supplies a corpus-wide CV for each word, while occurrence-aligned features connect the retained profile to BERT. The derivations establish the quantities and their relationships. Predictive or semantic usefulness requires independent task evidence.

### Text normalization before snippet selection

Contextual slicing partitions the normalized source text into contiguous, non-overlapping chunks. This operation is also called contextual chunking. The algorithm determines each chunk's boundaries and textual extent; chunks need not have equal lengths. Each chunk constitutes one sample, represented by one TF-IDF vector. Across text-processing literature and libraries, these text units may also be called documents, snippets or slices. The term source document denotes the input before chunking. Concatenating the chunks in source order must exactly reconstruct the normalized source body, with every retained position covered once and no gaps or overlap. Before contextual chunking into snippets, all source text is converted to lowercase. Non-printing control characters are removed, while newlines and ordinary spaces are retained. Carriage-return and carriage-return/line-feed endings are normalized to line feed. Tabs and other horizontal space separators are converted to ordinary spaces. Visible characters, including punctuation and visible non-ASCII characters, are retained. Consecutive spaces and newlines remain in their original order.

The normalized text remains linked to the unmodified source through an edit map, so every retained character span can be traced to its origin. Normalization precedes snippet selection, occurrence-span recording and word counting because these operations determine the observations and weights used throughout the method. Fragmented sentences, omissions and incomplete context remain in the text. Character cleaning therefore changes the input representation without reconstructing missing linguistic content.

### Preserving the source record

Each passage retains its source identifier, character boundaries, extraction version and reading order, together with the spans of its word occurrences. Contextual chunking defines the passage rows used for counting. Rules for headings, tables and optical-character-recognition output must be declared for any source type to which they apply, because changing these rules changes both the retained language and the numerical reference. The numerical core accepts an aligned count matrix and does not itself determine passage boundaries.

The raw-text corpus preparation uses the complete released 20 Newsgroups by-date archive [101]. Original released bytes and document identifiers are retained. Headers are stored as metadata, while normalized bodies supply the text for contextual chunking. Quotations, signatures, short fragments and explicit omissions remain, with no document selection by cleanliness, length or BERT's input limit.

The selected implementation applies the default NLTK 3.10.4 TextTiling tokenizer to each normalized body. A successful segmentation must reconstruct that body exactly when its snippets are concatenated. A failed segmentation remains attached to the preserved source and its error record. No alternative chunking rule has been specified for these failures, so full-corpus reference fitting remains unresolved at that boundary.

Passage selection is intended to retain the evidence needed for contextual interpretation, but length alone cannot establish that the relevant evidence survives. Software history slicing offers a limited analogy: its tests and compilation dependencies specify what a retained subset must preserve [87]. Here the preservation question concerns language, so the analogy motivates explicit retention criteria rather than supplying a linguistic segmentation algorithm.

Boundary quality, numerical separation and predictive usefulness require different references. WindowDiff compares the number of passage boundaries within moving windows against a segmentation reference [88]. The clustering criterion assesses the fitted numerical partition, while independent task labels assess classifier predictions. A compact partition cannot establish that the preceding segmentation preserved the intended linguistic context.

### Word weights and the reference collection

The selected TF-IDF representation combines each word's raw count in a passage with its rarity across the training reference [89, 29, 90]. IDF is the natural logarithm of the number of reference passages divided by the number containing the word. Multiplying whole occurrence counts by this value gives the unnormalized weight matrix, with no smoothing or additive offset. Its columns retain the declared vocabulary identities, so subsequent coordinate comparisons continue to refer to the same words.

The selected training passages serve both as observations and as IDF reference units. This choice fixes the population in which word rarity is measured. Documents, sentences and selected passages can yield different frequencies even when drawn from the same source text [91]. Each resulting coordinate therefore combines a local passage count with a frequency defined over that fixed training reference.

F[i,t] = count(t,c[i]),    d[t] = ∑[a=1..m] 𝟙[t occurs in r[a]],    δ[t] = ln(m/d[t]),    A[i,t] = F[i,t]δ[t],    1 ≤ d[t] ≤ m

**Notation**

| Symbol | Definition |
| --- | --- |
| F | Nonnegative n × p matrix of raw retained term frequencies in selected passages. |
| count | Nonnegative integer count under the declared vocabulary and tokenization rule. |
| c | Collection of n selected contextual passages. |
| d | Reference frequency vector of length p. |
| r | Declared collection of m IDF reference units, fixed from permitted training data. |
| δ | Nonnegative p dimensional regular logarithmic IDF vector, zero exactly for words present in all reference units. |
| A | Nonnegative n × p TF IDF matrix before row normalization. |
| n | Number of selected observation passages. |
| m | Number of reference units, equal to the training passage count in the selected route. |
| p | Number of retained vocabulary features. |
| i | Observation index from 1 to n. |
| t | Vocabulary feature index from 1 to p. |
| a | Reference unit index from 1 to m. |
| 𝟙 | Indicator equal to one when its stated condition holds and zero otherwise. |

X[i,:] = A[i,:]/‖A[i,:]‖₂ if ‖A[i,:]‖₂>0, otherwise 0,    ‖x[i]‖₂=1 for nonzero rows,    ‖x[i]−x[j]‖₂²=2(1−cos(x[i],x[j])) for two nonzero rows

**Notation**

| Symbol | Definition |
| --- | --- |
| A | Regular TF IDF matrix before passage normalization. |
| X | Passage by vocabulary matrix after row L2 normalization, used in k means and the diagnostic. |
| x | Row vectors of the normalized passage matrix. |
| i | First passage index. |
| j | Second passage index. |
| cos | Cosine similarity, defined for two nonzero vectors as their inner product divided by the product of their Euclidean lengths. |

For two nonzero normalized passage rows, squared Euclidean distance equals two minus twice their inner product, and that inner product equals their cosine similarity. The displayed identity concerns two unit rows. Cluster centers are arithmetic means and are not renormalized, so their lengths generally differ from one. Passage-to-center comparisons consequently retain the Euclidean rule rather than substituting a cosine comparison.

The chosen IDF formula gives zero weight to a word present in every reference passage. Its weighted column and coordinate distances are then zero, even though the source records still contain its occurrences. The mean distance is zero, so an ordinary coefficient of variation cannot be calculated. The method records that score as unavailable. This avoids confusing a missing ratio with a measured score of zero.

Suppose the reference contains two documents: “a b” and “a c.” The word “a” appears in both, so its regular IDF is zero. If the same text is counted as four one-word reference units, “a” appears in two of four and its IDF becomes the natural logarithm of two, about 0.693147. The words did not change. The counting units did. If the original documents remain the IDF reference while only the observation passages are changed, IDF instead stays fixed and passage counts change.

Row L2 normalization removes uniform passage scale while retaining the relative composition of its weighted vocabulary. Multiplying all counts in one passage by the same positive factor leaves its normalized row unchanged when the IDF reference is fixed. Each nonzero row is divided by its Euclidean length. A zero row remains zero and has no defined direction.

### Fitting passage groups with k-means

For each candidate cluster count, Euclidean k-means assigns complete passage vectors to their nearest centers and replaces each center by the mean of its assigned vectors [92, 93]. These alternating steps establish the partition before any individual word distances are aggregated. The implementation computes a mean by averaging differences from one group member and adding that member back, preserving exactly constant coordinates in the tested calculation. The fitted memberships and centers then supply both the cluster-count criterion and the diagnostic. Zero within-group variation makes the finite selection ratio unavailable.

J(k) = ∑[i=1..n] ‖x[i] − μ[a[i]]‖₂²,    a[i] = argmin[g=1..k] ‖x[i] − μ[g]‖₂²,    μ[g] = (1/n[g])∑[i:a[i]=g] x[i]

**Notation**

| Symbol | Definition |
| --- | --- |
| J | Within cluster squared Euclidean objective for the fitted k center candidate. |
| x | Passage vectors in the original vocabulary coordinates. |
| μ | Fitted center vectors in the same space. |
| a | Nearest center membership of each passage. |
| n | Number of passages, with n[g] the positive membership count of cluster g. |
| k | The cluster count of the current candidate. |
| i | Passage index from 1 to n. |
| g | Cluster index from 1 to k. |
| argmin | A minimizing index, with the first center index resolving equal distances. |

With centers fixed, nearest-center assignment minimizes each passage's contribution to the squared-distance objective. With assignments fixed, the arithmetic mean minimizes each group's contribution. The alternating steps therefore decrease or preserve the objective, but different initial centers can lead to different fitted partitions. Multiple starts address this initialization dependence without establishing a global minimum.

### Selecting the number of groups

The cluster count is selected by comparing separately fitted k-means partitions. For corpus evaluation, the declared search covers every integer from 2 through 100, subject to the admissibility conditions below. The Caliński-Harabasz criterion evaluates each resulting partition [40]. This outer comparison selects a count from fitted candidates and differs from cutting a fixed Ward hierarchy [38].

Caliński and Harabasz introduced the variance ratio for partitions obtained by cutting a shortest dendrite [40]. Because the score depends on within-group and between-group sums of squares, the present method applies it to k-means partitions and selects the largest admissible finite value. This application is an explicit implementation choice. The score describes fitted separation and does not inherit the inferential interpretation of a classical ANOVA model with externally specified groups.

Within-group variation is the sum of squared Euclidean distances from each passage to its assigned center. Between-group variation compares each center with the overall mean and weights that squared distance by the group's passage count. Dividing these sums by their respective degrees-of-freedom terms gives the ratio below. Larger values describe greater separation between centers relative to dispersion within the fitted groups.

VRC(k) = (SSB / (k − 1)) / (SSW / (n − k)),    1 < k < n,    SSW > 0

**Notation**

| Symbol | Definition |
| --- | --- |
| VRC | Scalar variance ratio criterion for a specified partition and representation. |
| SSB | Between group sum of squares in that representation. |
| SSW | Within group sum of squares in the same representation. |
| k | Integer number of nonempty groups. |
| n | Total integer observation count. |

The six-point example divided into two groups has a score of 56.25. For the corpus calculation, each candidate count receives a fresh k-means fit and its own complete score. We select the largest finite score and choose the smaller cluster count in an exact tie. A zero within-group denominator is recorded as undefined. The selected count describes a numerical grouping of passages, not a number of lexical senses. If no candidate has an admissible finite score, the implementation uses one overall center and records that cluster-count selection was unavailable.

For a fixed dataset, total squared variation is constant. At a fixed cluster count, reducing within-group variation transfers the same amount to between-group variation. Substituting total minus within-group variation into the criterion gives the expression below and establishes its decrease as positive within-group variation increases. Comparing different cluster counts additionally changes the degrees-of-freedom terms.

VRC(k) = ((n−k)/(k−1))(SST/SSW − 1),    SST > 0,    SSW > 0

**Notation**

| Symbol | Definition |
| --- | --- |
| VRC | The standard Caliński Harabasz ratio, with between group mean square in its numerator. |
| SST | Fixed total squared variation of the reference observations. |
| SSW | Positive within group squared variation of the partition. |
| n | Reference passage count. |
| k | Fixed candidate count satisfying 1 < k < n. |

The count adjustment is essential when comparing partitions with different numbers of clusters. Selecting the smallest unadjusted within-cluster sum would generally favor additional centers, whereas the stated ratio evaluates the balance between separation and dispersion at each count. Reversing its numerator and denominator would also reverse the preferred direction.

kbest = min argmax[k ∈ Kset] VRC(k),    Kset ⊆ {2,…,n−1}

**Notation**

| Symbol | Definition |
| --- | --- |
| kbest | Selected count when the admissible set is nonempty, with the smaller count resolving an exact maximum-score tie. If the set is empty, the implementation uses one center and records selection as unavailable. |
| Kset | Declared finite set of candidate counts whose fitted partitions have nonempty groups, positive within group dispersion and a finite score. |
| VRC | Caliński Harabasz variance ratio score of the Euclidean k means partition fitted for the indicated count. |
| k | Candidate count in the admissible set. |
| n | Total reference passage count. |
| argmax | The set of candidate counts attaining the highest score. |
| min | Tie breaking operation selecting the smallest maximizing count. |

![Figure 11](figures/Work_ksearch.png)

**Figure 11. Selecting the number of clusters. Fit k-means for each declared count and retain the greatest admissible finite CH score.**

Each candidate uses the same normalized TF-IDF passage matrix. Its within-cluster and between-cluster sums of squares determine the adjusted variance ratio. The selected centers then supply the coordinate distances used in the word diagnostic.

K-means determines memberships for each candidate count, and the outer criterion selects among those fitted partitions. The general helper defaults to counts from two to one fewer than the number of reference passages, while the declared corpus sweep restricts that search to 2 through 100. Invalid denominators remain unavailable rather than receiving a favorable score. Once selection is complete, memberships and centers are fixed for word-distance aggregation. Neither fitting nor count selection optimizes the later CV.

A cluster can be consistent about a word because the word is usually present or because it is usually absent. Likewise, a difference between cluster means can reflect different topics, source formats or uses of language. The numerical partition does not distinguish these explanations. Word prevalence and the linked source passages are needed to interpret the pattern.

### How individual words contribute to a cluster

Each word's contribution to within-cluster variation is obtained by subtracting its cluster mean weight from each assigned passage weight, squaring those differences and summing them. Summing across words and clusters recovers the k-means within-cluster sum of squares. The diagnostic instead retains the unsquared scalar Euclidean distances, equal to the absolute coordinate differences, so their variation can be measured separately for each word. Squared departures belong to the clustering objective and are not substituted for these diagnostic measurements.

μ[g,t] = (1/n[g])∑[i∈C[g]] X[i,t],    D[g,t] = ∑[i∈C[g]] (X[i,t] − μ[g,t])²,    B[t] = ∑[g=1..k] n[g](μ[g,t] − μ[t])²

**Notation**

| Symbol | Definition |
| --- | --- |
| μ | Mean notation, with μ[g,t] a scalar group feature mean and μ[t] the scalar overall feature mean. |
| D | Nonnegative k × p matrix of within group, per feature squared dispersion. |
| B | Nonnegative p dimensional vector of between group feature contributions. |
| X | L2 normalized n × p TF IDF matrix in the original vocabulary coordinates. |
| C | Fixed partition into k nonempty observation groups. |
| n | Count notation, with n[g] the positive size of group g. |
| k | Number of groups. |
| p | Number of vocabulary features. |
| g | Group index from 1 to k. |
| t | Feature index from 1 to p. |
| i | Observation index within the stated group. |

### A corpus-wide score for uneven word distances

With the fitted partition fixed, every word weight in a passage is compared with the corresponding word coordinate of that passage's assigned center. The scalar Euclidean distance is the absolute difference between those two weights. Repeating this comparison across passages gives one nonnegative distance column per word while preserving the original vocabulary axes. The full-vector nearest-center assignment shown below is the passage assignment already established by clustering, not a new assignment for each word.

a[i] = argmin[g=1..k] ‖x[i] − μ[g]‖₂,    R[i,t] = |X[i,t] − μ[a[i],t]|,    ‖x[i] − μ[a[i]]‖₂² = ∑[t=1..p] R[i,t]²

**Notation**

| Symbol | Definition |
| --- | --- |
| a | Integer nearest centroid assignment for each passage, with a fixed index tie rule. |
| R | Nonnegative n × p matrix of element to element distances to the selected fitted centroid. |
| X | L2 normalized n × p TF IDF matrix in the original vocabulary coordinates. |
| x | Passage row vectors in the original p dimensional vocabulary space. |
| μ | Fixed fitted centroid vectors, with μ[a[i],t] the element on axis t of the centroid selected for row i. |
| n | Positive number of reference passages. |
| p | Positive number of vocabulary axes. |
| k | Positive number of fitted centroids. |
| i | Reference passage index from 1 to n. |
| g | Candidate centroid index from 1 to k. |
| t | Vocabulary axis index from 1 to p. |
| argmin | An index attaining the smallest full vector distance under the fixed tie rule. |

Every word in a passage must use the same selected center. For example, consider a unit passage row (0.6, 0.8) and stored centers (0, 1) and (1, 0). Its squared distances are 0.4 and 0.8, so the full-vector comparison selects (0, 1) and gives absolute coordinate differences (0.6, 0.2). Choosing the nearest coordinate separately would give (0.4, 0.2), as though the reference were (1, 1), which is not a fitted center. The implementation checks that stored centers are the means of their assigned passages and that assignments agree with the nearest-center rule. Once these references are fixed, each word's distance column is summarized across the complete corpus.

m[t] = (1/n)∑[i=1..n] R[i,t],    v[t] = (1/n)∑[i=1..n] (R[i,t] − m[t])²,    CVdistance[t] = √v[t]/m[t],    CVdistance[t]² = (∑[i=1..n] R[i,t]²)/(n m[t]²) − 1,    m[t] > 0

**Notation**

| Symbol | Definition |
| --- | --- |
| m | p dimensional vector of population means of coordinate distances across the full reference corpus. |
| v | Nonnegative p dimensional vector of population variances of those same distances. |
| CVdistance | Per word coefficient of variation of coordinate distances, defined only for a positive distance mean. |
| R | The n × p coordinate distance matrix defined above. |
| n | Positive reference passage count, supplying the denominator for empirical population moments. |
| i | Reference passage index from 1 to n. |
| t | Vocabulary axis index from 1 to p. |

Consider one coordinate with weights 0, 1, 2 and 5. Their mean is 2, so their absolute distances from that mean are 2, 1, 0 and 3. These distances have mean 1.5 and population variance 1.25, giving a coefficient of variation of about 0.745356. Applying CV directly to the original weights would instead give about 0.935414. The two answers differ because they summarize different measurements. This small example explains the aggregation step only. The complete method still constructs and normalizes passage vectors before fitting the centers.

Aggregation reconstructs each word's full distribution of coordinate distances from the fixed groups. A group's contribution to the overall mean is weighted by its passage count. The overall population variance combines variation within groups with differences between their distance means. These means describe distances, whereas the fitted centroid coordinates describe TF-IDF weights. The law of total variance gives the reconstruction below, after which the population standard deviation is divided by the reconstructed mean to form CV.

w[g] = n[g]/n,    m[t] = ∑[g] w[g]m[g,t],    v[t] = ∑[g] w[g](v[g,t] + (m[g,t] − m[t])²)

**Notation**

| Symbol | Definition |
| --- | --- |
| w | Passage proportion weights of the nonempty nearest centroid groups. |
| n | Corpus count notation, with n[g] the size of nearest centroid reference group g. |
| m | Distance mean notation: m[g,t] is the mean within the stated nearest centroid group, and m[t] is the full corpus mean. |
| v | Population distance variance notation: v[g,t] is the within group variance and v[t] the full corpus variance. |
| g | Index over nonempty nearest centroid reference groups. |
| t | Vocabulary axis index. |

Passage-count weighting gives every reference passage the same contribution, regardless of its group's size. A distance's departure from the corpus mean decomposes into its departure from the group distance mean and that group mean's departure from the corpus mean. The centered cross term vanishes, yielding the two variance contributions [94]. This finite-population identity does not require normality or equal group variances.

If stored group summaries use sample variances, their centered sums of squares must first be recovered by multiplying each variance by one fewer than its group count. Pooling those sums represents only within-group variation. The complete corpus variance also requires differences between group means and the full population denominator. The displayed conversion applies when each reported group sample variance is defined.

s²pool[t] = (∑[g=1..k] (n[g] − 1)s[g,t]²)/(N − k),    v[t] = ((N − k)/N)s²pool[t] + (1/N)∑[g=1..k] n[g](m[g,t] − m[t])²,    s²all[t] = (N/(N − 1))v[t]

**Notation**

| Symbol | Definition |
| --- | --- |
| s²pool | Degrees of freedom weighted pooled within group variance of distances on each axis. |
| s | Group sample standard deviation notation, with s[g,t]² using divisor n[g] minus one. |
| s²all | Sample variance of all distances combined, using divisor N minus one. |
| v | Population variance of the full reference distance column, using divisor N. |
| m | Distance means, with m[g,t] the group mean and m[t] the observation weighted full reference mean. |
| n | Group count notation, with each n[g] at least two for this displayed sample variance conversion. |
| N | Total count of the distance observations, equal to the sum of the group counts. |
| k | Number of nonempty summary groups. |
| g | Summary group index from one to k. |
| t | Vocabulary axis index. |

For example, store the four fixed distances above in batches (2, 3) and (1, 0). Their means are 2.5 and 0.5, and both sample variances are 0.5. The pooled within-batch sample variance is also 0.5. After converting to the four-observation population denominator, its contribution is 0.25. Differences between batch means contribute another 1, giving the correct total variance of 1.25. Adding the unconverted 0.5 would incorrectly give 1.5. These batches only reorganize fixed distances. They do not refit the contextual groups. For a singleton batch, the centered sum of squares is zero, so centered-sum bookkeeping remains valid even though its sample variance is undefined.

Counts, distance sums and squared-distance sums provide an equivalent aggregation because each total adds across disjoint groups on the same word axis. Their substitution into the CV definition gives the expression below. Direct subtraction of nearly equal raw moments can be numerically unstable, so the implementation evaluates centered moments using the principle of Pébay's merge formulas [95].

N = ∑[g] n[g],    S[t] = ∑[g]∑[i∈G[g]] R[i,t],    Q[t] = ∑[g]∑[i∈G[g]] R[i,t]²,    CVdistance[t] = √(N Q[t]/S[t]² − 1),    S[t]>0

**Notation**

| Symbol | Definition |
| --- | --- |
| N | Total number of reference distance observations per vocabulary axis. |
| n | Group membership counts, with n[g] the number of reference passages assigned to group g. |
| S | Per word sum of all coordinate distances, computed by merging the corresponding group sums. |
| Q | Per word uncorrected sum of squared coordinate distances, computed by merging the corresponding group sums of squares. |
| R | Nonnegative coordinate distances to the matching elements of the nearest fitted centroid. |
| G | Nearest centroid groups, with G[g] the passage index set of group g. |
| CVdistance | Population moment coefficient of variation of all reference distances on the word axis. |
| g | Group index. |
| i | Passage index within the stated group. |
| t | Vocabulary axis index. |

The distance sum divided by the reference count gives the mean, and the mean squared distance minus the squared mean gives the population variance. Their substitution yields the displayed CV identity. For numerical evaluation, each nonzero distance column is divided by its maximum before centered moments are accumulated. That common positive scale cancels from CV. Scaled summaries and representability indicators preserve the computational record when original-unit moments underflow.

A large distance CV means that the distances are concentrated unevenly across passages. This interpretation has a precise connection to Hoyer's established measure of nonnegative sparseness, which compares the L1 and L2 norms [96]. Substituting the distance-CV identity into that measure gives the following relation for a nonzero distance column.

h[t] = (√n − ‖r[t]‖₁/‖r[t]‖₂)/(√n − 1) = √n(1 − 1/√(1 + CVdistance[t]²))/(√n − 1),    n > 1,    r[t] ≠ 0

**Notation**

| Symbol | Definition |
| --- | --- |
| h | p dimensional vector of Hoyer nonnegative sparseness values for nonzero distance columns. |
| r | Distance column family. Each r[t] is the n dimensional nonnegative column R[:,t]. |
| n | Reference passage count, greater than one for this sparseness definition. |
| t | Vocabulary axis index. |
| ‖·‖₁ | L1 norm, the sum of absolute coordinates. |
| ‖·‖₂ | Euclidean L2 norm. |
| CVdistance | Population coefficient of variation of the same nonzero distance column. |

The L1 norm is the sum of the nonnegative distances, and the squared L2 norm is their squared-distance sum. For a fixed number of passages, Hoyer sparseness increases with distance CV, so the two measures rank these columns in the same order. The proposed contribution is therefore the choice and traceable construction of the distance measurements, together with their use in the stated interface. It is not a new general measure of dispersion. This relation identifies the mathematical property represented by a large score: concentration of residual distances across passages.

The aggregation forms CV from the reconstructed distance population rather than averaging cluster CVs. A different procedure, such as NIOSH's laboratory-precision combination of squared group CVs with degrees-of-freedom weights [97], describes a different estimand. Replacing the population standard deviation by a sample standard deviation would multiply the present ratio by the square root of the total count divided by one fewer observation. Reporting the ratio as a percentage would additionally multiply it by one hundred.

Two boundary cases make the meaning clear. If every distance is the same positive value, CV is zero. The distances are perfectly even, although their common magnitude may be large. If every distance is zero, the mean is zero and CV is undefined. The stored validity mask distinguishes this unavailable score from a measured zero. The mean distance and the CV therefore answer different questions: how large the departures are, and how unevenly they are distributed.

Each word receives one corpus-wide CV when its mean coordinate distance is positive. This aggregation summarizes the passage index but retains every reference passage in the measurement population, including passages where the word is absent. Conditioning on occurrence would instead change both the population and the statistic. A high value can therefore reflect topic concentration or systematic absence, and it is neither an occurrence label nor a count of senses. The source-linked coordinate distances remain necessary for interpreting which passages contributed to the score.

Multiplying every distance for one word by the same positive constant changes its mean and standard deviation by the same factor, leaving CV unchanged. Repeating every distance the same number of times also leaves the population moments unchanged. These are useful fixed-reference properties. They do not cover adding different passages, changing their relative frequencies or refitting the centers. Small additive changes can also matter when the mean distance is close to zero. Unitlessness does not make the score insensitive to all changes in data.

Sorting words by decreasing distance CV prioritizes uneven departures from the fixed group references for source inspection. The occurrence classifier below instead receives the full word-by-cluster profile, its validity flags, between-group variation and local distance together with the local TF-IDF weight. Global distance CV is not a feature in that specified occurrence interface. The separately supplied SVD helper can weight vocabulary columns by CV after aggregation, as an explicitly distinct extension. The singleton example in the Discussion shows why an unusual passage can have no residual signal under its selected grouping.

![Figure 12](figures/Work_longformat.png)

**Figure 12. From one passage-word comparison to a traceable record. The same distance records supply the word score and the optional network display.**

The six-passage example gives both words an IDF equal to the natural logarithm of 1.5. After L2 normalization, the fitted centers are approximately (0.982894, 0.105409) and (0.105409, 0.982894). Both word distance CVs are approximately 0.842277. The full records retain passage and word identifiers, original counts, normalized weights, center coordinates, distances and normalization metadata.

Figure 12 follows a complete example from counts to records. The Appendix gives six passage rows over two words. Each word occurs in four passages, so both IDF values are the natural logarithm of 1.5. After row normalization, the first two passages have the same direction. The two fitted centers are approximately (0.982894, 0.105409) and (0.105409, 0.982894). Comparing each passage with its assigned center produces twelve coordinate-distance records, including comparisons for absent words. Aggregating by word gives a CV of about 0.842277 for each column. Passage, word and cluster identifiers remain attached to every record.

Weight distributions supply additional information about the group differences underlying the diagnostic. Prevalence records the proportion of positive weights, while conditional moments describe those positive entries. For example, weights 0.72, 0.63, 0.68 and 0.70 average 0.6825, whereas 0.05, 0.10, 0.06 and 0.13 average 0.085. Source inspection is needed to explain that difference. These weight summaries complement the distance CV and form part of the full group-conditioned profile used for learning.

Skewness and excess kurtosis describe distributional shape through standardized third and fourth centered moments. Excess kurtosis subtracts the Gaussian reference value of three, and both quantities require positive variance. The following definitions use coordinate distances as the measurement population. The group-conditioned profile below applies the same definitions to word weights, with that different population stated explicitly.

Skew(Y) = E[(Y − μ)³]/v^(3/2),    ExcessKurtosis(Y) = E[(Y − μ)⁴]/v² − 3

**Notation**

| Symbol | Definition |
| --- | --- |
| Skew | Scalar standardized third central moment of the declared empirical measurement distribution. |
| ExcessKurtosis | Scalar standardized fourth central moment minus three. |
| Y | Scalar coordinate distance under uniform passage selection within the stated group. An explicitly named weight analysis substitutes word weights. |
| μ | Scalar population mean of Y within this formula. |
| v | Strictly positive scalar population variance of Y. |
| E | Expectation under the uniform empirical distribution of the group. |

Centering removes the mean, and the variance powers remove positive scale. The third moment retains the direction of asymmetry. The fourth gives large deviations greater weight. These descriptors are also unchanged by positive scaling and uniform replication, so those properties are not unique to CV. Their purpose is to describe distributional shape, while CV compares standard deviation with a positive mean.

### Why sparse word weights can have a large CV

The CV of word weights can be large simply because most entries are zero. To see this, select a passage uniformly from a fixed group. Let π be the probability that the selected weight is positive. Among positive entries, let α be the mean and β the population variance. Conditioning on presence gives the following decomposition. It concerns the original weights, not distances from fitted centers. Under regular IDF, a positive weight indicates an occurrence only for a word whose IDF is positive.

E[Y] = πα,    Var(Y) = πβ + π(1 − π)α²,    CV² = Var(Y)/E[Y]² = (1 − π)/π + β/(πα²)

**Notation**

| Symbol | Definition |
| --- | --- |
| Y | Nonnegative scalar feature weight obtained by uniform selection of a row from the stated group. |
| π | Positive entry probability in the group, with 0 < π ≤ 1. |
| α | Positive conditional mean E[Y given Y > 0]. |
| β | Nonnegative conditional population variance of Y given Y > 0. |
| CV | Nonnegative population coefficient of variation, defined as standard deviation divided by a positive mean. |
| E | Expectation under the stated uniform empirical distribution. |
| Var | Population variance under that same distribution. |

The overall second moment is the positive-weight second moment multiplied by the probability of a positive entry. Subtracting the squared overall mean gives the full variance. Dividing by that mean squared separates the contribution of zeros from variation among positive weights. If all positive weights are equal, only prevalence matters. Two positive entries among twelve observations give CV equal to the square root of five. Eight positive entries among twelve give the square root of one half. Figure 13 illustrates this effect.

![Figure 13](figures/Work_prevalence.png)

**Figure 13. A word can have a large weight CV simply because it is absent from most observations.**

With twelve observations and equal positive weights, two positive entries give CV equal to the square root of five. Eight positive entries give the square root of one half. The curve applies to equal positive weights and shows the effect of prevalence alone.

If there are no positive weights, the mean is zero and ordinary CV is undefined. A word that occurs in every passage can still have all-zero weights because its regular IDF is zero. This is another reason to retain occurrence counts separately from weights. Changing to a sample denominator or calculating CV across group means would define a different statistic. The measurements and denominator must therefore accompany the reported CV.

Scale cancellation applies after the measurements have been fixed. If one word coordinate and the matching center coordinates are multiplied by the same positive factor, their fixed-assignment distances scale equally and their CV is unchanged. But changing feature scales before clustering can change which center a passage receives. Row normalization also couples each coordinate to the other values in that passage. An upstream weighting change can therefore alter the final score even though common scaling of an already fixed distance column cancels.

Distance CV describes the unevenness of one word's departures from its assigned cluster coordinates across the fixed reference corpus. Retained passage records identify the observations contributing to that unevenness. Determining whether a context is damaged or a word use is inappropriate requires interpretation or independent labels. The score therefore accompanies the complete cluster-by-cluster profile rather than replacing it.

### Inspecting word-to-cluster records

The long table supports an optional bipartite display with words and fitted clusters as vertices. Each passage-word record connects its word to the passage's assigned cluster, so repeated word-cluster pairs remain parallel edges unless explicitly aggregated for display. Coordinate distance is an edge attribute and corpus-wide CV is a word attribute. Distance encodes discrepancy from the reference coordinate, so interpreting it as affinity requires a separately defined transformation.

An unfiltered version of this graph has a simple limitation: every word connects to every nonempty cluster. This follows because the full table includes every passage-word comparison, including absences and zero distances. The mere presence of an edge therefore does not distinguish words or show that a word occurred in that passage. The useful information lies in distances, word scores and linked source records. Any filtering or aggregation used to simplify the display must be stated because it changes what the visible edges mean.

Retaining the passage and word keys with each weight, cluster assignment and center coordinate allows the normalized matrix and its comparisons to be recovered from the long table. A graph restricted to endpoint identifiers loses those measurements and source links. The complete records therefore remain available alongside any simplified display. Visualization supports inspection but is not required for the CV calculation.

### Combining contextual behavior with BERT

The supervised unit is a target word occurrence in a retained passage. Its contextual BERT state, local TF-IDF weight and corpus-derived behavioral profile describe the same identified occurrence at different levels. Source and passage identifiers locate the text, the character span identifies its position, and the vocabulary index selects its word profile. This alignment precedes concatenation because compatible feature dimensions alone do not establish a valid correspondence between the inputs.

#### Preserving the cluster dimension

For every vocabulary word and selected cluster, the profile stores mean weight, within-group sum of squared deviations, prevalence, positive-weight mean, positive-weight population variance, skewness, excess kurtosis and cluster size. The mean, squared-deviation sum and standardized shape moments use all rows, including zero weights. Positive-weight moments condition on positive entries. Skewness and kurtosis are unavailable at zero variance. Counts and validity flags accompany the values so that an undefined quantity remains distinguishable from a measured zero.

P ∈ ℝ^(p×k×s),    M ∈ {0,1}^(p×k×s),    s = 8

**Notation**

| Symbol | Definition |
| --- | --- |
| P | Numerical array of word-by-cluster statistics. Undefined entries are stored as zero only alongside their validity flag. |
| M | Matching binary validity array: one means the corresponding statistic is defined. |
| p | Number of retained vocabulary words. |
| k | Number of groups selected from the training corpus. |
| s | Number of declared statistics per word and cluster, eight in this implementation. |

The profile axes identify words, clusters and statistics. Flattening one word's cluster-by-statistic slice retains every value in a declared order, including the cluster dimension. That dimension is fixed by the selected training reference rather than by a chosen neural embedding width. Refitting a new reference can change the selected cluster count and therefore requires rebuilding the corresponding statistical inputs and prediction layer.

μ[g,t] = mean(X[i,t] : i∈C[g]),    D[g,t] = ∑[i∈C[g]](X[i,t]−μ[g,t])²
B[t] = ∑[g=1..k] n[g](μ[g,t]−μ[t])²

**Notation**

| Symbol | Definition |
| --- | --- |
| X | Training passage-by-word weight matrix in the declared original vocabulary coordinates. |
| μ | Group mean when indexed by g,t; overall word mean when indexed only by t. |
| D | Within-group squared-deviation sum for a word. |
| B | Between-group squared-deviation sum for a word. |
| C | Partition of training passage indices into nonempty groups. |
| n | Group size n[g]. |
| i | Passage index. |
| g | Cluster index from 1 to k. |
| t | Vocabulary index from 1 to p. |
| k | Selected cluster count. |

These quantities retain both stable and variable behavior. Large between-group variation can describe a word concentrated in particular contexts. Large within-group variation can draw attention to heterogeneous passages. Neither is automatically evidence of misuse. The local distance identifies an occurrence's passage relative to its own reference, while the complete profile supplies the wider comparison.

#### Joining the three inputs

BERT receives the retained passage as token identifiers, an attention mask and, when used, segment identifiers. The target occurrence's contextual vector is the mean of its attended WordPiece states. Tokenizer offsets align those positions with the recorded character span and exclude padding and special tokens. Repeated words receive separate occurrence masks. A missing target span or unknown vocabulary index is rejected rather than mapped to another occurrence or word profile.

β[o] = concat(vec(P[t,:,:]), vec(M[t,:,:]), B[t], δ[o])
δ[o] = |X[i,t] − μ[a[i],t]|,    w[o] = X[i,t],    β[o] ∈ ℝ^(2ks+2)

**Notation**

| Symbol | Definition |
| --- | --- |
| β | Full behavioral feature vector for one target occurrence. |
| P | Fitted word-by-cluster-by-statistic array. |
| M | Corresponding validity flags converted to numeric zero/one. |
| B | Between-group squared-deviation sum for the target word. |
| δ | Absolute difference between the target word weight and its assigned group mean. |
| w | Target word TF-IDF weight in its passage under the fitted convention. |
| X | Passage weights in the training vocabulary; new passages use the stored IDF and normalization. |
| μ | Stored cluster-coordinate means. |
| a | Nearest stored cluster index for each passage. |
| i | Passage containing occurrence o. |
| t | Vocabulary word identified by occurrence o. |
| o | Target occurrence index. |
| k | Selected cluster count. |
| s | Eight declared profile statistics. |
| vec | Flattening in a stored cluster-major, statistic-minor order. |
| concat | Concatenation along the feature axis. |

The local weight and distance depend on the passage, while occurrences of the same word share its fitted corpus profile. Their positions and surrounding sequences can still produce different BERT states. The vocabulary index therefore selects word-specific corpus information, and the aligned local inputs retain the passage-level evidence needed to interpret that information for each occurrence.

![Figure 14](figures/Work_headfusion.png)

**Figure 14. Occurrence-aligned fusion and the training path into BERT.**

Text produces a 768-coordinate target-occurrence state. TF-IDF supplies one local weight. The full word-by-cluster profile, validity flags, between-group sum and local distance supply 2ks+2 behavioral coordinates. Their concatenation enters the learned prediction head. The loss updates that head and the last BERT encoder block; corpus statistics and earlier BERT blocks remain fixed.

**Table 1. Aligned information channels for BERT adaptation**

| Information channel | Aligned neural input |
| --- | --- |
| Context | Target WordPiece mean: batch × 768 for BERT Base. |
| Importance | Target word TF-IDF: batch × 1. |
| Contextual behavior | Complete selected-word profile and flags, between-group sum and local distance: batch × (2ks+2). |
| Combined input | Batch × (771+2ks). The selected cluster count k remains explicit. |

u[o] = concat(h[o], w[o], β[o]),    u[o] ∈ ℝ^(771+2ks)
z[o] = tanh(Au[o]+b),    ℓ[o] = Wz[o]+c,    ŷ[o] = softmax(ℓ[o])

**Notation**

| Symbol | Definition |
| --- | --- |
| u | Concatenated occurrence vector. |
| h | 768-coordinate mean of target WordPiece states from BERT Base. |
| w | One TF-IDF coordinate for the target word in its passage. |
| β | Behavior vector of width 2ks+2 defined above. |
| A | Trainable matrix of shape r by (771+2ks). |
| b | Trainable bias vector of length r. |
| z | Joint hidden state of length r. |
| W | Trainable matrix of shape C by r. |
| c | Trainable class bias of length C. |
| ℓ | Unnormalized class-score vector of length C. |
| ŷ | Predicted distribution over C task classes. |
| r | Chosen head width, 128 in the executable example; not a cluster count. |
| C | Number of independently defined task classes, at least two. |
| k | Training-corpus cluster count. |
| s | Number of profile statistics, eight. |
| o | Target occurrence index. |

The first learned matrix combines contextual, importance and behavioral coordinates, and the nonlinear hidden state allows their effects to depend on one another. The second matrix maps that joint state to class scores. These parameters are estimated from labeled examples, so concatenation defines an input interface rather than a trained prediction rule. The number of output classes follows the independent annotation task, with binary classification as the two-class case.

#### How the statistics teach BERT

Independent occurrence labels define the supervised objective. Contextual appropriateness and lexical sense are possible tasks, but each requires its own annotation rules and outcome interpretation. Corpus clusters supply reference measurements and do not become task labels merely because they were fitted. A completed supervised experiment therefore requires an explicitly labeled task in addition to the feature construction.

ℒ = −(1/N)∑[o=1..N] log ŷ[o,y[o]]
θlast[next] = θlast − ε grad[θlast]ℒ,    θhead[next] = θhead − ε grad[θhead]ℒ

**Notation**

| Symbol | Definition |
| --- | --- |
| ℒ | Mean supervised cross-entropy loss. |
| N | Number of labeled occurrences in the evaluated batch. |
| o | Occurrence index from 1 to N. |
| y | Independent class label for each occurrence. |
| ŷ | Predicted probability of each task class. |
| θlast | Trainable parameters of the last BERT encoder block. |
| θhead | Trainable parameters A,b,W,c. |
| ε | Positive optimization step size in the illustrative gradient update. |
| grad | Gradient with respect to the indicated parameters. |
| next | Parameter value after the displayed update. |

The implementation passes unnormalized class scores to cross-entropy. Differentiation then follows the prediction head, the pooled occurrence state and BERT's final encoder block. Corpus statistics remain fixed, but their contribution to the prediction can change the loss gradient and hence the update to that block. The wrapper freezes embeddings and earlier blocks while optimizing the final block and prediction head together.

ℓ = Wₕhθ + Wββ + b    ⇒    grad[θ]ℒ = JₕᵀWₕᵀ(ŷ−y)

**Notation**

| Symbol | Definition |
| --- | --- |
| ℓ | Class scores for one example in an illustrative linear head. |
| Wh | Trainable class-by-context matrix. |
| Wβ | Trainable class-by-statistical-feature matrix. |
| h | Context vector depending on trainable encoder parameters θ. |
| β | Fixed statistical input for this example. |
| b | Class bias vector. |
| Jh | Jacobian of the contextual vector with respect to the trainable encoder parameters. |
| θ | Trainable encoder parameters. |
| ℒ | One-example cross-entropy loss. |
| ŷ | Softmax class probabilities. |
| y | One-hot target class vector. |

The simpler linear head makes this dependence explicit: statistical inputs affect the class scores and the probability error that multiplies the encoder Jacobian. The nonlinear head additionally allows interactions before class scoring. The influence can vanish when statistical weights are zero, a computation saturates or another degeneracy intervenes. Side statistics do not directly condition BERT's contextual state in the same forward pass. They can affect later states through supervised parameter updates.

#### Reference fitting, implementation and limits

Supervised evaluation requires source families to be separated before vocabulary, IDF, cluster search and profiles are fitted, keeping all related occurrences within one split. Training sources determine the reference measurements, validation selects training settings, and a separate test set assesses predictive performance. Optional standardization is fitted on training occurrences only after the diagnostic quantities are fixed. Cluster count, classifier class count and head width remain separate parameters. The helpers require the application to enforce these source and split boundaries.

Work_Contextual_Behavior_Fusion.py computes the full profile, aligns occurrence features and wraps an unmodified BertModel with a trainable final block and prediction head. The earlier helper with a frozen encoder and passage-level head is a separate legacy comparison. The occurrence interface retains the original word-coordinate profile. Graph participation and SVD are separately defined analyses, and any SVD extension follows completion of the original-coordinate diagnostic rather than changing its fitted geometry.

BERT Base supplies 768-coordinate states and accepts at most 512 token positions [76]. The reference English checkpoint is google-bert/bert-base-uncased at revision 86b5e0934494bd15c9632b12f734a8a67f723594. The recorded interface uses Transformers 4.57.1 and PyTorch 2.8.0. Target spans must remain fully represented, and inputs exceeding the supported length require an explicitly declared handling policy. Randomly initialized encoders can test shape and gradient mechanics, but those checks do not measure pretrained language quality or task accuracy.

Existing implementations combine Transformer representations with numerical features [98], establishing a precedent for the interface rather than evidence that this behavioral profile improves prediction. Its contribution to learning must be assessed against BERT with the same trainable final block, using controlled additions of TF-IDF, behavioral features and both. Shared labels, splits and tuning opportunities make those comparisons interpretable.

#### Passage length, irregular text and computational cost

Different corpus problems enter the calculation in different ways. Disrupted reading order changes BERT's sequence. A changed passage boundary changes both the counted vocabulary row and the retained text. Missing antecedents remove information even when the arithmetic is correct. Mixed languages, copied templates and extraction errors can affect both branches. Robustness therefore has to be measured for a named task, model and disturbance, rather than claimed from the architecture alone [99].

A linguistically useful passage can exceed BERT Base's length limit. CLS and SEP leave at most 510 content WordPieces, which need not correspond one-to-one with whole words, and the supplied helper rejects longer inputs. Rechunking would change the retained text and its count row, so both branches would require a consistent declared policy. Any change to reference passage units would also require refitting their counts and statistics. No cropping or window-combination rule is implicit in the present construction.

The resource requirements follow the retained representation. Clustering repeats full-vocabulary passage-to-center comparisons across candidate counts. Profile storage grows with vocabulary size, selected cluster count and statistic count, while dense BERT attention grows quadratically with sequence length. Resource limits must therefore be addressed through declared implementation choices. Removing vocabulary or cluster dimensions would change the measured representation and cannot be treated as a purely computational optimization.

### Relationships needed to follow the method

The method relies on a small set of shared objects: passages, vocabulary columns, fitted groups, distances and task labels. Keeping these objects distinct allows a reader to follow each transformation and identify where a changed choice would affect later results.

Table 2 summarizes the role of each foundation in the established construction. Their connection is carried by the objects being measured: passages, vocabulary coordinates, group references, aggregate word statistics and the aligned inputs to learning.

**Table 2. Scientific foundations and their roles in the construction**

| Foundation | Role and interpretive boundary |
| --- | --- |
| Graph theory | Defined vertices and edges make relations explicit. Laplacian energy connects an edge rule to squared differences. A graph layout does not determine linguistic meaning. |
| Least squares and statistical variation | The mean minimizes squared error. Within-group and between-group sums account for total variation. Sampling assumptions are needed for inference, whereas the present CV describes a finite distance population. |
| Singular value decomposition | Paired orthogonal directions link passage and word Gram matrices. Truncation gives a controlled reconstruction error but can remove useful distinctions. The diagnostic is therefore calculated before compression. |
| Structural and distributional linguistics | Vocabulary identity, ordered combinations and selected environments define the linguistic objects. Distributional evidence supports interpretation without making a numerical group a sense inventory. |
| Numerical clustering | Ward merges and k-means use least-squares reasoning with different searches. The selected k-means partitions supply means and memberships. CH compares admissible candidate counts without establishing an inferential F test. |
| Corpus-based context representation | Word vectors summarize corpus co-occurrence. Context vectors combine representations for a selected use. These second-order features differ from direct passage TF-IDF rows. |
| Contextual chunking | Lexical-cohesion comparisons select textual observations. Boundaries determine counts and the IDF reference. Source identifiers preserve the link to language, while boundary quality requires its own assessment. |
| Lexical networks | Row and column comparisons define different graphs. Community participation summarizes edge strengths, while the main diagnostic summarizes coordinate distances. Its word-to-cluster records retain measurements and source links. |
| Bidirectional language encoding | BERT represents a target occurrence in its ordered passage. The prediction head combines that state with the aligned local TF-IDF weight and full statistical profile. The head and final encoder block learn from independent occurrence labels. |

### Software and Tool Use

ChatGPT assisted literature discovery, mathematical analysis, implementation, and manuscript drafting and revision. Executed numerical checks use the stated synthetic inputs. The author is responsible for reviewing and approving the scientific claims and submitted text.

### How to evaluate usefulness

The empirical objective is to determine whether corpus-derived behavioral information improves an independently defined occurrence task on source material. Mathematical derivations and implementation checks establish properties of the construction but do not answer that predictive question. Evaluation consequently requires source-separated fitting, independent occurrence labels and held-out assessment, with the reference and its feature definitions fixed before test predictions are examined.

Each claimed output has its own assessment target. Marked passage boundaries assess segmentation, and the selected variance criterion describes numerical separation. Assessing problematic word-context relationships requires independent judgments that include rare but legitimate uses, while classifier accuracy requires task labels defined independently of the diagnostic. A fitted cluster or score cannot supply its own semantic ground truth.

The primary comparison uses the same independently labeled occurrences to evaluate BERT alone, BERT with TF-IDF, BERT with the full behavioral profile and the complete combination. Keeping the final-block training policy and tuning budget comparable isolates the effect of the added inputs. Further ablations can examine local distance, validity indicators and individual statistical channels, with uncertainty assessed across the source splits and initializations actually sampled. A global-CV-only input is a reduced comparator and does not preserve the full profile.

Sensitivity evaluation must distinguish changes to the measurements from changes to the classifier. Passage boundaries, extraction quality, language, length, unseen vocabulary and source type can alter the observed representation. Naturally occurring problems and artificial corruption require separate reporting. Cluster-count range, cluster sizes, singletons, unavailable scores and ranking stability are relevant because a fine partition may fit an unusual passage so closely that its residual signal disappears. These inspections do not impose an additional cluster-size threshold on the stated selection rule.

A classifier's confidence needs a separate check. Among predictions assigned a given confidence, the observed correctness rate should be comparable. Temperature scaling adjusts the score scale on separate calibration data without changing the available classes [100]. Accuracy, class-balanced measures, error types and resource costs answer other practical questions. Reporting them separately makes the system's strengths and limits interpretable.

## What the calculations and tests establish

### Mathematical results and reproducible checks

The mathematical results concern the stated reference geometry, variance decomposition, distance summaries and neural training path. Numerical checks cover the worked examples and counterexamples, the eight-statistic profile, validity masks, occurrence alignment and feature widths. Finite differences verify the illustrative encoder-gradient equation. An executed PyTorch test of the occurrence wrapper uses a randomly initialized two-layer BertModel with hidden width 768. It verifies the forward path, a nonzero final-block gradient, changes to that gradient when statistical inputs change, an optimizer update to the final block, preservation of the earlier block and rejection of four invalid inputs. These checks establish the tested implementation mechanics. They do not measure pretrained language quality or classification accuracy.

**Table 3. Numerical examples and their mathematical scope**

| Object checked | Computed result and scope |
| --- | --- |
| Distance CV | Distances 2, 1, 0 and 3 give mean 1.5, population variance 1.25 and CV approximately 0.745356. |
| Six-point partition | Within-cluster sum 8/3, between-cluster sum 75/2 and total sum 241/6 give a variance-ratio score of 56.25. |
| Four-cycle graph | The Laplacian eigenvalues are 0, 2, 2 and 4. Matrix and edge calculations give the same quadratic energy. |
| Full and truncated SVD | Full factors reconstruct the matrix. Truncation has the stated discarded-singular-value error and cannot increase projected pairwise distances. |
| Loss of a distinction | Retaining only the leading direction of rows (10, 0), (0, 1) and (0, 2) maps the latter two distinct rows to zero. |
| Changing scale | Common positive scaling of fixed distances preserves CV. Changing IDF before row normalization and clustering can change the final score. |
| Sparse weights | Direct population CV agrees with the decomposition into prevalence and variation among positive weights. |
| Network-community strengths | The displayed identity relates participation to community CV when all communities, including zero-strength entries, are counted. |
| Attention | The checks cover softmax shift invariance, equivalent query-key coordinate changes and permutation equivariance without positional information. |
| A constant auxiliary vector | An affine layer can absorb an input block shared unchanged by every passage into its bias. |
| Statistical influence on encoder learning | The scalar example gives gradients −0.8026246798 and −0.3956322229 for auxiliary values zero and one. Central finite differences agree within one billionth. This establishes a possible gradient path, not task improvement. |

The counterexamples are as important as the successful calculations. Rank truncation can remove a real distinction while giving the best approximation of its rank. Rescaling fixed distances preserves CV, but changing the geometry before fitting can change the groups and distances. The participation identity shows when two numerical descriptors repeat the same information. These examples give concrete boundaries to the interpretation of the combined construction.

### Corpus preparation and chunking

The corpus preparation used all 18,846 documents in the published 20 Newsgroups by-date archive [101]. Original released bytes were retained, and the prescribed character normalization preceded chunking. No document was removed for short length, incomplete context, quotation content or segmentation difficulty. The collection contains 369 documents with explicit omission markers. These markers identify material for inspection and do not constitute independently annotated semantic-error labels.

Default NLTK TextTiling segmentation succeeded for 15,621 documents and produced 44,548 snippets. Concatenating each successful document's snippets exactly reconstructed its normalized body. Segmentation failed for 3,225 documents: 2,266 had similarity vectors too short for the smoothing window, and 959 lacked paragraph breaks. All failures remain in the source records. A fallback segmentation rule has not been specified, so the complete corpus has not advanced to clustering, CV aggregation or classification. No full-corpus accuracy or broken-context detection rate is established by this preparation result.

## Discussion

The construction connects three descriptions without confusing their roles. TF-IDF measures importance under a declared corpus convention. Group-conditioned statistics retain a word's contextual behavior across the fitted groups. BERT supplies an occurrence-specific representation of ordered text. The prediction head combines them, and a shared supervised loss updates both that head and the final encoder block. Source-linked records preserve the measurements used in each prediction.

The derivations and synthetic checks establish the construction under its stated assumptions. The raw-corpus preparation additionally shows that the selected segmentation implementation does not process every retained source without a further boundary rule. Detection yield and reviewer agreement remain unmeasured because independently assessed word-context outcomes are unavailable. The incomplete corpus evaluation cannot establish whether the statistical features improve classification over text-only or simpler numerical baselines. These are separate questions from the verified aggregation and training mechanics.

A small example shows why an unusual passage can escape the diagnostic. Use five count rows: (5, 1, 0), (6, 1, 0), (5, 2, 0), (6, 2, 0) and (0, 0, 1). The default count search selects four clusters. The unusual last passage becomes a singleton whose center equals itself. The third word then has zero residual distance everywhere and an unavailable CV, while the first two words both have CV about 1.224745. More generally, n observations split into n minus one nonempty groups leave one pair and otherwise singletons. For any coordinate on which that pair differs, only two equal absolute residuals remain, producing the same CV across those coordinates. A low or unavailable score therefore cannot certify that the source text is sound.

The fixed-reference conditions explain both the score's reproducibility and its limits. Rescaling every distance equally or repeating the whole distance sample leaves the score unchanged. Changing passage proportions, boundaries, feature geometry or fitted centers can change it. The word measurements remain in their original vocabulary coordinates even when SVD creates reduced classifier inputs. These conditions allow another investigator to reproduce the stated quantity without treating it as independent of how the corpus was constructed.

The behavioral profile serves learning and inspection. It can help direct attention to words and passages whose measured use differs from their group references. It cannot alone determine whether a use is incorrect. Different senses, rare but valid constructions and extraction errors may produce overlapping numerical patterns. Keeping the source occurrences, cluster identities, sample counts and local distances makes those competing explanations examinable.

## Conclusion

The paper establishes a coherent route from corpus observations to BERT adaptation. Original word coordinates support interpretable group-conditioned measurements, and a corpus-dependent search selects the group count. The full statistical profile, local importance and contextual encoder state meet at the same target occurrence. The training loss supplies an explicit gradient path into BERT's last block. This establishes a mathematically compatible, executable integration whose practical value remains an empirical question. Independent labels, controlled ablations and source-separated evaluation are needed to determine whether contextual-behavior statistics improve learning or reveal problematic word–context relationships.

## Appendix: Inputs for the worked examples

The following table gives the exact synthetic inputs used in the worked examples. Their reasoning appears beside the relevant equations in the main text. These small datasets make the calculations reproducible. They are not observations from a language-model benchmark.

**Table 4. Inputs for the reproducible numerical examples**

| Example | Exact input |
| --- | --- |
| Observation coordinates | Six rows: 1,1  /  2,1  /  1,2  /  5,4  /  6,4  /  5,5. Groups are rows 1 to 3 and 4 to 6. |
| Spanning tree | Edges 1 to 2, 1 to 3, 2 to 4, 4 to 5 and 4 to 6. Remove 2 to 4 for two components. |
| Bridge multigraph | AB twice, AC twice, AD, BD and CD once each. |
| Four cycle | Edges 1 to 2, 2 to 3, 3 to 4 and 4 to 1, with unit weights. |
| Binary incidence | Columns bank, river, loan, credit, flow. Rows 11000  /  11000  /  10100  /  10110  /  01001  /  00110. |
| Sparse equal positive weights | Twelve rows with two positive unit entries, or twelve rows with eight positive unit entries. |
| Group conditioned feature weights | First group 0.72, 0.63, 0.68, 0.70. Second group 0.05, 0.10, 0.06, 0.13. |
| Low rank collapse | Rows 10,0  /  0,1  /  0,2, retaining only the leading right singular direction. |
| Two key attention | Query 1,0. Keys 1,0 and 0,1. Values 1,0 and 0,1. Key dimension 2. |
| Long format example counts | Six passage rows over two words: 3,0  /  4,0  /  3,1  /  0,3  /  0,4  /  1,3. Both words occur in four passages. |

The scripts record their numerical-library versions and comparison tolerances. The algebra explains why an identity holds under its assumptions, while the numerical checks test the implementation on declared inputs. The document build checks keep the readable manuscript, equations and editable sources synchronized. These checks support reproduction at the scale actually examined.

## References

[1] Zellig S. Harris. 1954. Distributional Structure. Word 10, 146-162. [Source](https://doi.org/10.1080/00437956.1954.11659520)

[2] Hinrich Schütze. 1998. Automatic Word Sense Discrimination. Computational Linguistics 24, issue 1, 97-123. [Source](https://aclanthology.org/J98-1004/)

[3] Priyankar Bose, Satyaki Roy, Preetam Ghosh. 2021. A Comparative NLP-Based Study on the Current Trends and Future Directions in COVID-19 Research. IEEE Access 9, 78341-78355. [Source](https://doi.org/10.1109/ACCESS.2021.3082108)

[4] Ferdinand de Saussure. 1916. Cours de linguistique générale. Edited by Charles Bally and Albert Sechehaye, with Albert Riedlinger. Lausanne and Paris: Payot.

[5] Edward Sapir. 1921. Language: An Introduction to the Study of Speech. New York: Harcourt, Brace and Company. [Source](https://pure.mpg.de/pubman/item/item_2381135_2/component/file_2381134/Sapir_1921_language.pdf)

[6] Leonard Bloomfield. 1933. Language. New York: Henry Holt.

[7] Bronisław Malinowski. 1923. The Problem of Meaning in Primitive Languages. Supplement I to C. K. Ogden and I. A. Richards, The Meaning of Meaning, 296-336. London: Kegan Paul, Trench, Trubner.

[8] J. R. Firth. 1935. The Technique of Semantics. Transactions of the Philological Society 34, issue 1, 36-73. [Source](https://doi.org/10.1111/j.1467-968X.1935.tb01254.x)

[9] Zellig S. Harris. 1942. Morpheme Alternants in Linguistic Analysis. Language 18, issue 3, 169-180. [Source](https://doi.org/10.2307/409550)

[10] Zellig S. Harris. 1946. From Morpheme to Utterance. Language 22, issue 3, 161-183. [Source](https://doi.org/10.2307/410205)

[11] Zellig S. Harris. 1951. Methods in Structural Linguistics. Chicago: University of Chicago Press.

[12] Zellig S. Harris. 1952. Discourse Analysis. Language 28, issue 1, 1-30. [Source](https://doi.org/10.2307/409987)

[13] J. R. Firth. 1951. Modes of Meaning. Essays and Studies, new series 4, 118-149.

[14] J. R. Firth. 1957. A Synopsis of Linguistic Theory, 1930-1955. Studies in Linguistic Analysis, 1-32. Oxford: Philological Society. [Source](https://languagelog.ldc.upenn.edu/myl/Firth1957.pdf)

[15] Hinrich Schütze. 1992. Dimensions of Meaning. Proceedings of Supercomputing, 787-796. [Source](https://doi.org/10.1109/SUPERC.1992.236684)

[16] Hinrich Schütze. 1992. Word Space. Advances in Neural Information Processing Systems 5, 895-902. Conference 1992, proceedings 1993. [Source](https://papers.neurips.cc/paper/1992/hash/d86ea612dec96096c5e0fcc8dd42ab6d-Abstract.html)

[17] Marti A. Hearst. 1993. TextTiling: A Quantitative Approach to Discourse Segmentation. Technical Report UCB/S2K-93-24, University of California, Berkeley. [Source](https://people.ischool.berkeley.edu/~hearst/research/tiling.html)

[18] Marti A. Hearst, Christian Plaunt. 1993. Subtopic Structuring for Full-Length Document Access. Proceedings of SIGIR, 59-68. [Source](https://doi.org/10.1145/160688.160695)

[19] Marti A. Hearst. 1994. Multi-Paragraph Segmentation of Expository Text. 32nd Annual Meeting of the Association for Computational Linguistics, 9-16. [Source](https://aclanthology.org/P94-1002/)

[20] Marti A. Hearst. 1997. TextTiling: Segmenting Text into Multi-paragraph Subtopic Passages. Computational Linguistics 23, issue 1, 33-64. [Source](https://aclanthology.org/J97-1003/)

[21] Stefan Kaufmann. 1999. Cohesion and Collocation: Using Context Vectors in Text Segmentation. Proceedings of the 37th Annual Meeting of the Association for Computational Linguistics, 591–595. [Source](https://aclanthology.org/P99-1077/)

[22] Stefan Kaufmann. 2000. Second‐Order Cohesion. Computational Intelligence 16, issue 4, 511-524. [Source](https://doi.org/10.1111/0824-7935.00124)

[23] Freddy Y. Y. Choi. 2000. Advances in domain independent linear text segmentation. 1st Meeting of the North American Chapter of the Association for Computational Linguistics. [Source](https://aclanthology.org/A00-2004/)

[24] Masao Utiyama, Hitoshi Isahara. 2001. A Statistical Model for Domain-Independent Text Segmentation. Proceedings of the 39th Annual Meeting of the Association for Computational Linguistics, 499-506. [Source](https://aclanthology.org/P01-1064/)

[25] Manabu Okumura, Takeo Honda. 1994. Word Sense Disambiguation and Text Segmentation Based on Lexical Cohesion. COLING 1994 Volume 2: The 15th International Conference on Computational Linguistics. [Source](https://aclanthology.org/C94-2121/)

[26] Amruta Purandare, Ted Pedersen. 2004. Word Sense Discrimination by Clustering Contexts in Vector and Similarity Spaces. Proceedings of the Eighth Conference on Computational Natural Language Learning (CoNLL-2004) at HLT-NAACL 2004, 41-48. [Source](https://aclanthology.org/W04-2406/)

[27] Anagha Kulkarni, Ted Pedersen. 2005. SenseClusters: Unsupervised Clustering and Labeling of Similar Contexts. Proceedings of the ACL Interactive Poster and Demonstration Sessions, 105-108. [Source](https://aclanthology.org/P05-3027/)

[28] Jing Wang, Mohit Bansal, Kevin Gimpel, Brian D. Ziebart, Clement T. Yu. 2015. A Sense-Topic Model for Word Sense Induction with Unsupervised Data Enrichment. Transactions of the Association for Computational Linguistics 3, 59-71. [Source](https://aclanthology.org/Q15-1005/)

[29] G. Salton, A. Wong, C. S. Yang. 1975. A vector space model for automatic indexing. Communications of the ACM 18, issue 11, 613-620. [Source](https://doi.org/10.1145/361219.361220)

[30] Adrien-Marie Legendre. 1805. Nouvelles méthodes pour la détermination des orbites des comètes. Paris: Firmin Didot.

[31] Carl Friedrich Gauss. 1809. Theoria motus corporum coelestium in sectionibus conicis solem ambientium. Hamburg: Friedrich Perthes and Johann Heinrich Besser.

[32] Student. 1908. The Probable Error of a Mean. Biometrika 6, issue 1, 1-25. [Source](https://doi.org/10.1093/biomet/6.1.1)

[33] R. A. Fisher. 1918. The Correlation between Relatives on the Supposition of Mendelian Inheritance. Transactions of the Royal Society of Edinburgh 52, issue 2, 399-433. [Source](https://doi.org/10.1017/S0080456800012163)

[34] R. A. Fisher. 1921. Studies in crop variation. I. An examination of the yield of dressed grain from Broadbalk. The Journal of Agricultural Science 11, issue 2, 107-135. [Source](https://doi.org/10.1017/S0021859600003750)

[35] R. A. Fisher, W. A. Mackenzie. 1923. Studies in crop variation. II. The manurial response of different potato varieties. The Journal of Agricultural Science 13, issue 3, 311-320. [Source](https://doi.org/10.1017/S0021859600003592)

[36] R. A. Fisher. 1925. Statistical Methods for Research Workers. Edinburgh: Oliver and Boyd.

[37] National Institute of Standards and Technology. n.d.. Coefficient of Variation. Dataplot Reference Manual. [Source](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/coefvari.htm)

[38] Joe H. Ward. 1963. Hierarchical Grouping to Optimize an Objective Function. Journal of the American Statistical Association 58, issue 301, 236-244. [Source](https://doi.org/10.1080/01621459.1963.10500845)

[39] K. Florek, J. Łukaszewicz, J. Perkal, Hugo Steinhaus, S. Zubrzycki. 1951. Sur la liaison et la division des points d'un ensemble fini. Colloquium Mathematicum 2, issue 3-4, 282-285. [Source](https://doi.org/10.4064/cm-2-3-4-282-285)

[40] T. Caliński, J Harabasz. 1974. A dendrite method for cluster analysis. Communications in Statistics 3, issue 1, 1-27. [Source](https://doi.org/10.1080/03610927408827101)

[41] Leonhard Euler. 1741. Solutio problematis ad geometriam situs pertinentis. Commentarii academiae scientiarum Petropolitanae 8, 128-140, volume dated 1736. [Source](https://scholarlycommons.pacific.edu/euler-works/53/)

[42] Miroslav Fiedler. 1973. Algebraic connectivity of graphs. Czechoslovak Mathematical Journal 23, issue 2, 298-305. [Source](https://doi.org/10.21136/cmj.1973.101168)

[43] Gustav Kirchhoff. 1847. Ueber die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird. Annalen der Physik und Chemie 72 (cumulative volume 148), issue 12, 497–508. [Source](https://sites.math.rutgers.edu/~zeilberg/akherim/kirchoff1847.pdf)

[44] Paul Erdős, Alfréd Rényi. 1959. On Random Graphs I. Publicationes Mathematicae 6, 290-297. [Source](https://www.renyi.hu/~p_erdos/1959-11.pdf)

[45] Duncan J. Watts, Steven H. Strogatz. 1998. Collective dynamics of ‘small-world’ networks. Nature 393, issue 6684, 440-442. [Source](https://doi.org/10.1038/30918)

[46] Albert-László Barabási, Réka Albert. 1999. Emergence of Scaling in Random Networks. Science 286, issue 5439, 509-512. [Source](https://doi.org/10.1126/science.286.5439.509)

[47] M. Ross Quillian. 1967. Word concepts: A theory and simulation of some basic semantic capabilities. Behavioral Science 12, issue 5, 410-430. [Source](https://doi.org/10.1002/bs.3830120511)

[48] George A. Miller, Richard Beckwith, Christiane Fellbaum, Derek Gross, Katherine J. Miller. 1990. Introduction to WordNet: An On-line Lexical Database. International Journal of Lexicography 3, issue 4, 235-244. [Source](https://doi.org/10.1093/ijl/3.4.235)

[49] Dominic Widdows, Beate Dorow. 2002. A Graph Model for Unsupervised Lexical Acquisition. COLING 2002: The 19th International Conference on Computational Linguistics. [Source](https://aclanthology.org/C02-1114/)

[50] M. Girvan, M. E. J. Newman. 2002. Community structure in social and biological networks. Proceedings of the National Academy of Sciences 99, issue 12, 7821-7826. [Source](https://doi.org/10.1073/pnas.122653799)

[51] M. E. J. Newman, M. Girvan. 2004. Finding and evaluating community structure in networks. Physical Review E 69, 026113. [Source](https://arxiv.org/abs/cond-mat/0308217)

[52] Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre. 2008. Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment 2008, issue 10, P10008. [Source](https://doi.org/10.1088/1742-5468/2008/10/P10008)

[53] V. A. Traag, L. Waltman, N. J. van Eck. 2019. From Louvain to Leiden: guaranteeing well-connected communities. Scientific Reports 9, issue 1. [Source](https://doi.org/10.1038/s41598-019-41695-z)

[54] Santo Fortunato, Marc Barthélemy. 2007. Resolution limit in community detection. Proceedings of the National Academy of Sciences 104, issue 1, 36-41. [Source](https://doi.org/10.1073/pnas.0605965104)

[55] Roger Guimerà, Luís A Nunes Amaral. 2005. Cartography of complex networks: modules and universal roles. Journal of Statistical Mechanics: Theory and Experiment 2005, issue 02, P02001. [Source](https://doi.org/10.1088/1742-5468/2005/02/P02001)

[56] Eugenio Beltrami. 1873. Sulle funzioni bilineari. Giornale di Matematiche 11, 98-106. [Source](https://www-users.cse.umn.edu/~boley/publications/papers/Beltrami.pdf)

[57] Camille Jordan. 1874. Mémoire sur les formes bilinéaires. Journal de Mathématiques Pures et Appliquées, second series 19, 35-54. [Source](http://www.numdam.org/item/JMPA_1874_2_19__35_0/)

[58] G. W. Stewart. 1993. On the Early History of the Singular Value Decomposition. SIAM Review 35, issue 4, 551-566. [Source](https://doi.org/10.1137/1035134)

[59] G. Golub, W. Kahan. 1965. Calculating the Singular Values and Pseudo-Inverse of a Matrix. Journal of the Society for Industrial and Applied Mathematics Series B Numerical Analysis 2, issue 2, 205-224. [Source](https://doi.org/10.1137/0702016)

[60] G. H. Golub, C. Reinsch. 1970. Singular value decomposition and least squares solutions. Numerische Mathematik 14, issue 5, 403-420. [Source](https://doi.org/10.1007/BF02163027)

[61] Scott Deerwester, Susan T. Dumais, George W. Furnas, Thomas K. Landauer, Richard Harshman. 1990. Indexing by latent semantic analysis. Journal of the American Society for Information Science 41, issue 6, 391-407. [Source](https://doi.org/10.1002/%28SICI%291097-4571%28199009%2941:6%3C391::AID-ASI1%3E3.0.CO%3B2-9)

[62] Carl Eckart, Gale Young. 1936. The Approximation of One Matrix by Another of Lower Rank. Psychometrika 1, issue 3, 211-218. [Source](https://doi.org/10.1007/BF02288367)

[63] L. Mirsky. 1960. Symmetric Gauge Functions and Unitarily Invariant Norms. The Quarterly Journal of Mathematics 11, issue 1, 50-59. [Source](https://doi.org/10.1093/qmath/11.1.50)

[64] Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean. 2013. Efficient Estimation of Word Representations in Vector Space. arXiv:1301.3781. [Source](https://arxiv.org/abs/1301.3781)

[65] Jeffrey Pennington, Richard Socher, Christopher Manning. 2014. GloVe: Global Vectors for Word Representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532-1543. [Source](https://aclanthology.org/D14-1162/)

[66] David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams. 1986. Learning representations by back-propagating errors. Nature 323, issue 6088, 533-536. [Source](https://doi.org/10.1038/323533a0)

[67] Jeffrey L. Elman. 1990. Finding Structure in Time. Cognitive Science 14, issue 2, 179-211. [Source](https://doi.org/10.1207/s15516709cog1402_1)

[68] Sepp Hochreiter, Jürgen Schmidhuber. 1997. Long Short-Term Memory. Neural Computation 9, issue 8, 1735-1780. [Source](https://doi.org/10.1162/neco.1997.9.8.1735)

[69] Kyunghyun Cho, Bart van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio. 2014. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1724-1734. [Source](https://aclanthology.org/D14-1179/)

[70] Ilya Sutskever, Oriol Vinyals, Quoc V. Le. 2014. Sequence to Sequence Learning with Neural Networks. Advances in Neural Information Processing Systems 27. [Source](https://arxiv.org/abs/1409.3215)

[71] Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio. 2015. Neural Machine Translation by Jointly Learning to Align and Translate. International Conference on Learning Representations. Preprint 2014. [Source](https://arxiv.org/abs/1409.0473)

[72] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin. 2017. Attention Is All You Need. Advances in Neural Information Processing Systems 30. [Source](https://arxiv.org/abs/1706.03762)

[73] Thang Luong, Hieu Pham, Christopher D. Manning. 2015. Effective Approaches to Attention-based Neural Machine Translation. Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, 1412-1421. [Source](https://aclanthology.org/D15-1166/)

[74] Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, Rob Fergus. 2015. End-To-End Memory Networks. Advances in Neural Information Processing Systems 28. [Source](https://arxiv.org/abs/1503.08895)

[75] Paul Michel, Omer Levy, Graham Neubig. 2019. Are Sixteen Heads Really Better than One?. Advances in Neural Information Processing Systems 32. [Source](https://arxiv.org/abs/1905.10650)

[76] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 4171-4186. [Source](https://aclanthology.org/N19-1423/)

[77] Iz Beltagy, Matthew E. Peters, Arman Cohan. 2020. Longformer: The Long-Document Transformer. arXiv:2004.05150. [Source](https://arxiv.org/abs/2004.05150)

[78] Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer. 2018. Deep Contextualized Word Representations. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers), 2227-2237. [Source](https://aclanthology.org/N18-1202/)

[79] Jeremy Howard, Sebastian Ruder. 2018. Universal Language Model Fine-tuning for Text Classification. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 328-339. [Source](https://aclanthology.org/P18-1031/)

[80] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov. 2019. RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692. [Source](https://arxiv.org/abs/1907.11692)

[81] Luyao Huang, Chi Sun, Xipeng Qiu, Xuanjing Huang. 2019. GlossBERT: BERT for Word Sense Disambiguation with Gloss Knowledge. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 3509-3514. [Source](https://aclanthology.org/D19-1355/)

[82] Nils Reimers, Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 3982-3992. [Source](https://aclanthology.org/D19-1410/)

[83] Sarthak Jain, Byron C. Wallace. 2019. Attention is not Explanation. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 3543-3556. [Source](https://aclanthology.org/N19-1357/)

[84] Sarah Wiegreffe, Yuval Pinter. 2019. Attention is not not Explanation. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 11-20. [Source](https://aclanthology.org/D19-1002/)

[85] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly. 2019. Parameter-Efficient Transfer Learning for NLP. Proceedings of Machine Learning Research 97, 2790-2799. [Source](https://proceedings.mlr.press/v97/houlsby19a.html)

[86] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large Language Models. International Conference on Learning Representations. Preprint 2021. [Source](https://arxiv.org/abs/2106.09685)

[87] Yi Li, Chenguang Zhu, Julia Rubin, Marsha Chechik. 2018. Semantic Slicing of Software Version Histories. IEEE Transactions on Software Engineering 44, issue 2, 182-201. [Source](https://doi.org/10.1109/TSE.2017.2664824)

[88] Lev Pevzner, Marti A. Hearst. 2002. A Critique and Improvement of an Evaluation Metric for Text Segmentation. Computational Linguistics 28, issue 1, 19-36. [Source](https://aclanthology.org/J02-1002/)

[89] Karen Spärck Jones. 1972. A STATISTICAL INTERPRETATION OF TERM SPECIFICITY AND ITS APPLICATION IN RETRIEVAL. Journal of Documentation 28, issue 1, 11-21. [Source](https://doi.org/10.1108/eb026526)

[90] Gerard Salton, Christopher Buckley. 1988. Term-weighting approaches in automatic text retrieval. Information Processing & Management 24, issue 5, 513-523. [Source](https://doi.org/10.1016/0306-4573%2888%2990021-0)

[91] Catherine Blake. 2006. A Comparison of Document, Sentence, and Term Event Spaces. Proceedings of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the Association for Computational Linguistics, 601-608. [Source](https://aclanthology.org/P06-1076/)

[92] J. MacQueen. 1967. Some methods for classification and analysis of multivariate observations. Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability 1, 281-297. [Source](https://projecteuclid.org/ebooks/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fifth-Berkeley-Symposium-on-Mathematical-Statistics-and/chapter/Some-methods-for-classification-and-analysis-of-multivariate-observations/bsmsp/1200512992)

[93] Stuart P. Lloyd. 1982. Least Squares Quantization in PCM. IEEE Transactions on Information Theory 28, issue 2, 129-137. [Source](https://doi.org/10.1109/TIT.1982.1056489)

[94] J. W. Rudmin. 2010. Calculating the Exact Pooled Variance. arXiv:1007.1012. [Source](https://arxiv.org/abs/1007.1012)

[95] Philippe Pébay. 2008. Formulas for Robust, One-Pass Parallel Computation of Covariances and Arbitrary-Order Statistical Moments. Sandia National Laboratories, SAND2008-6212. [Source](https://digital.library.unt.edu/ark:/67531/metadc837537/m2/1/high_res_d/1028931.pdf)

[96] Patrik O. Hoyer. 2004. Non-negative Matrix Factorization with Sparseness Constraints. Journal of Machine Learning Research 5, 1457-1469. [Source](https://www.jmlr.org/papers/v5/hoyer04a.html)

[97] Ellen C. Gunderson, C. Clarine Anderson. 1980. Development and Validation of Methods for Sampling and Analysis of Workplace Toxic Substances. DHHS (NIOSH) Publication No. 80-133. [Source](https://stacks.cdc.gov/view/cdc/209393/cdc_209393_DS1.pdf)

[98] Ken Gu, Akshay Budhkar. 2021. Multimodal-Toolkit: A Package for Learning on Tabular and Text Data with Transformers. Proceedings of the Third Workshop on Multimodal Artificial Intelligence, 69-73. [Source](https://aclanthology.org/2021.maiworkshop-1.10/)

[99] Jindong Wang, Xixu Hu, Wenxin Hou, Hao Chen, Runkai Zheng, Yidong Wang, Linyi Yang, Haojun Huang, Wei Ye, Xiubo Geng, Binxing Jiao, Yue Zhang, Xing Xie. 2023. On the Robustness of ChatGPT: An Adversarial and Out-of-distribution Perspective. arXiv:2302.12095. [Source](https://arxiv.org/abs/2302.12095)

[100] Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger. 2017. On Calibration of Modern Neural Networks. Proceedings of Machine Learning Research 70, 1321-1330. [Source](https://proceedings.mlr.press/v70/guo17a.html)

[101] 20 Newsgroups. By-date corpus archive. Released source archive: https://ndownloader.figshare.com/files/5975967. SHA-256: 8f1b2514ca22a5ade8fbb9cfa5727df95fa587f4c87b786e15c759fa66d95610.
