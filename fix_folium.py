import json

notebook_path = "AluraStoreLatam.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Insert it at the very first position (cell 0), right after imports/markdown if possible.
# But it's safer to just inject it at the top.
pip_cell = {
  "cell_type": "code",
  "metadata": {},
  "outputs": [],
  "execution_count": None,
  "source": [
    "!pip install folium\n"
  ]
}

# The cell to install should be positioned exactly before the geographic analysis block
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = "".join(cell.get('source', []))
        if "Análisis Geográfico de Ventas" in source:
            # We found the geographic section, insert !pip install folium here
            nb['cells'].insert(i + 1, pip_cell)
            break

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
