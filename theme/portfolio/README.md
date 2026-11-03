# Portfolio

Use this theme for presentations, notebooks, dashboards, websites and reports, including the Bureau of Statistics interview assignment. The serif headings, sans-serif body, paper background and original illustrations come from Or Shulrufer’s portfolio.

| Element | Source value | Use |
| --- | --- | --- |
| Paper | `#F8F7F1` | Page or slide background |
| Ink | `#253D31` | Body text and chart labels |
| Forest green | `#234737` | Headings and primary marks |
| Muted green | `#59695F` | Captions and secondary labels |
| Rule | `#DCE0D4` | Dividers and light gridlines |
| Sage | `#E9EDE2` | Subtle fills |

The first six colors in the token file are copied from the site stylesheet. The separately named series colors extend the palette for charts. Pair colors with direct labels, marker shapes or line styles when readers must distinguish multiple series.

For HTML, link `portfolio.css` and apply the `portfolio` class to the body or a container. Keep `assets/` next to the stylesheet. It contains the original illustrations, identity artwork, four font files and the source font license. Use the research wireframe on a cover or divider and keep data plots clear of decoration.

For slides, use P052 for headings and Nimbus Sans for body text. Set the background, text and divider colors from the table. Use Noto Serif Hebrew and Noto Sans Hebrew for Hebrew text where the source fonts lack glyphs. The language fallback belongs to the same theme.

From the repository root, apply the notebook presets as follows.

```python
import json
from pathlib import Path
import matplotlib.pyplot as plt
import plotly.graph_objects as go

theme = Path("theme/portfolio")
plt.style.use(theme / "portfolio.mplstyle")
template = go.layout.Template(json.loads((theme / "plotly.json").read_text()))
fig = go.Figure(layout={"template": template})
```

Source files were copied from the saved portfolio site, version 54, commit `b8a31042b7fe5e7084e7ef8a2eec160cc5dd1718`. The original paths are `dist/styles.css` and `dist/assets/`. The CSS component rules and notebook presets adapt those assets for reuse. [Portfolio](https://or-shulrufer-portfolio.shulruferor.chatgpt.site/)
