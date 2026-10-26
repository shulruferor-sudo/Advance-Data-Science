import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
notebooks = {
    "project_notebooks/from_linguistic_context_to_semantic_structure/Proof.ipynb": ("failure-reporting", "dependencies"),
    "Figures.ipynb": ("failure-reporting", "dependencies", "figure-dependencies"),
}
for path, identifiers in notebooks.items():
    notebook = json.loads((root / path).read_text())
    namespace = {}
    for identifier in identifiers:
        cells = [cell for cell in notebook["cells"] if cell.get("id") == identifier]
        if len(cells) != 1:
            raise RuntimeError(f"{path}: expected one {identifier} cell")
        exec(compile("".join(cells[0]["source"]), f"{path}:{identifier}", "exec"), namespace)
print("Workspace dependencies are ready. Open a notebook and select the Python kernel.")
