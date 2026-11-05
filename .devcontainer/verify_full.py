"""Exercise the installed workspace without running the research pipeline."""
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

for module in ('numpy', 'scipy', 'sklearn', 'torch', 'transformers', 'chonky',
               'huggingface_hub', 'safetensors', 'nbformat', 'nbclient', 'ipykernel', 'fitz', 'PIL'):
    importlib.import_module(module)
    print(f'PASS import {module}', flush=True)

import numpy as np
from sklearn.cluster import KMeans
import torch
from transformers import BertConfig, BertModel
points = np.array([[0., 0.], [0., 1.], [10., 10.], [10., 11.]])
assert len(set(KMeans(n_clusters=2, n_init=2, random_state=1).fit_predict(points))) == 2
model = BertModel(BertConfig(vocab_size=20, hidden_size=16, num_hidden_layers=1,
                            num_attention_heads=2, intermediate_size=32))
assert model(torch.tensor([[1, 2, 3]])).last_hidden_state.shape == (1, 3, 16)
print('PASS numerical libraries and small local BERT forward pass', flush=True)

import nbformat
from nbclient import NotebookClient
notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('assert 2 + 2 == 4')])
NotebookClient(notebook, timeout=60, kernel_name='python3').execute()
print('PASS real Jupyter kernel execution', flush=True)

root = Path(__file__).resolve().parents[1]
figures = json.loads((root / 'Figures.ipynb').read_text())
namespace = {}
for identifier in ('failure-reporting', '59e3018f', 'c6820dfd', '8aa56d9d'):
    cell = next(c for c in figures['cells'] if c.get('id') == identifier)
    exec(compile(''.join(cell['source']), 'Figures.ipynb:' + identifier, 'exec'), namespace)
with tempfile.TemporaryDirectory() as directory:
    namespace['OUT'] = Path(directory)
    namespace['plt'] = namespace['configure_plotting']()
    figure, axes = namespace['plt'].subplots()
    axes.plot([0, 1], [0, 1])
    namespace['save'](figure, 'workspace_check')
    assert (Path(directory) / 'workspace_check.pdf').stat().st_size > 0
    assert (Path(directory) / 'workspace_check.png').stat().st_size > 0
print('PASS actual notebook figure export, XeLaTeX, fonts, PDF and PNG', flush=True)
subprocess.run([sys.executable, '-m', 'pip', 'check'], check=True)
print('PASS workspace verification', flush=True)
