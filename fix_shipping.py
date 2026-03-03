import json

notebook_path = "AluraStoreLatam.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# The content to inject
code_calc = """# Calcular el envío promedio
envio_promedio_tienda1 = tienda['Costo de envío'].mean()
envio_promedio_tienda2 = tienda2['Costo de envío'].mean()
envio_promedio_tienda3 = tienda3['Costo de envío'].mean()
envio_promedio_tienda4 = tienda4['Costo de envío'].mean()
"""

code_print = """# Mostrar los resultados
print(f'Ingreso promedio de envío de la tienda 1 es de {envio_promedio_tienda1:.2f} pesos')
print(f'Ingreso promedio de envío de la tienda 2 es de {envio_promedio_tienda2:.2f} pesos')
print(f'Ingreso promedio de envío de la tienda 3 es de {envio_promedio_tienda3:.2f} pesos')
print(f'Ingreso promedio de envío de la tienda 4 es de {envio_promedio_tienda4:.2f} pesos')
"""

# Find the markdown cell with "5. Envío"
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = "".join(cell.get('source', []))
        if "5." in source and "Envío" in source:
            # Found it! Let's update the next two code cells
            # Check if there are code cells after it
            idx1 = i + 1
            idx2 = i + 2
            
            if len(nb['cells']) > idx1 and nb['cells'][idx1]['cell_type'] == 'code':
                nb['cells'][idx1]['source'] = [line + "\n" if not line.endswith("\n") else line for line in code_calc.splitlines()]
            else:
                nb['cells'].insert(idx1, {"cell_type": "code", "metadata": {}, "source": [line + "\n" for line in code_calc.splitlines()], "outputs": [], "execution_count": None})
                
            if len(nb['cells']) > idx2 and nb['cells'][idx2]['cell_type'] == 'code':
                 nb['cells'][idx2]['source'] = [line + "\n" if not line.endswith("\n") else line for line in code_print.splitlines()]
            else:
                 nb['cells'].insert(idx2, {"cell_type": "code", "metadata": {}, "source": [line + "\n" for line in code_print.splitlines()], "outputs": [], "execution_count": None})
            
            break

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
