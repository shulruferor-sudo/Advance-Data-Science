"""Check that Codespaces can open and execute Jupyter notebooks."""
import importlib
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    ROOT / "projects" / "Bureau of Statistics" / "Assignment_Solution.ipynb",
    ROOT / "projects" / "LaBSE" / "labse_english_hebrew_only.ipynb",
    ROOT / "projects" / "LaBSE" / "labse_he_en_colab_validation.ipynb",
    ROOT / "projects" / "from_linguistic_context_to_semantic_structure" / "Proof.ipynb",
]

def main():
    for name in ("numpy", "pandas", "scipy", "sklearn", "matplotlib",
                 "openpyxl", "plotly", "ipykernel", "nbformat", "nbclient"):
        importlib.import_module(name)

    for path in NOTEBOOKS:
        if not path.is_file():
            raise FileNotFoundError(f"Missing notebook: {path.relative_to(ROOT)}")
        document = nbformat.read(path, as_version=4)
        if not document.cells or not any(cell.cell_type == "code" for cell in document.cells):
            raise ValueError(f"Notebook has no executable cells: {path.name}")
        print(f"PASS notebook: {path.relative_to(ROOT)}", flush=True)

    small = nbformat.v4.new_notebook(cells=[
        nbformat.v4.new_code_cell("import numpy as np, pandas as pd; assert np.array([1, 2]).sum() == 3")
    ])
    NotebookClient(small, timeout=60, kernel_name="advance-data-science").execute()
    print("PASS Jupyter kernel execution", flush=True)
    print("PASS Codespaces environment", flush=True)

if __name__ == "__main__":
    main()
