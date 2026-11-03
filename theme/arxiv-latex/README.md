# LaTeX for arXiv papers

Use this theme to prepare an arXiv manuscript and its figures. It reproduces the article typography and figure colors used in Or Shulrufer’s *From Linguistic Context to Semantic Structure*. It is the author's manuscript style. The archive documents the technical submission requirements separately. [arXiv TeX submission guide](https://info.arxiv.org/help/submit_tex.html)

Copy `main.tex` and `orpaper.sty` into the manuscript directory. Replace the example title, author and body, and run `xelatex main.tex` twice. Include the style file and all figures the manuscript references when packaging the sources. The article uses US letter, 10-point Latin Modern Roman, Latin Modern Math, one-inch margins, unnumbered headings and bold caption labels.

For Python figures, run `plt.style.use("theme/arxiv-latex/paper.mplstyle")` from the repository root. The style uses 10-point serif text, a white background and the source figure palette. The TeX color names in `orpaper.sty` reproduce the blue, teal, gray, pale fill, orange and edge colors of the manuscript’s diagram code. The separate three-group palette reproduces the colors from the geometric cluster figure. Use it with different markers when group membership must survive grayscale printing.

Sources at the repository revision used to extract this theme are the [manuscript preamble](https://github.com/shulruferor-sudo/Advance-Data-Science/blob/59425d57330c015de97f8d555bb403c33158974d/PDF_Creation/Projects_LaTeX/From_Linguistic_Context_to_Semantic_Structure.tex) and [figure-generation notebook](https://github.com/shulruferor-sudo/Advance-Data-Science/blob/59425d57330c015de97f8d555bb403c33158974d/Figures.ipynb).
