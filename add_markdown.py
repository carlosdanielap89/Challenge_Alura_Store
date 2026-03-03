import json

notebook_path = "AluraStoreLatam.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

markdown_text = """# Informe Final: Decisión Estratégica
**Objetivo del Informe:**
Presentar un análisis comparativo de cuatro tiendas para determinar cuál es la mejor opción de venta para el Sr. Juan, basado en métricas clave de rendimiento.

## 1. Análisis de las Tiendas

### Tienda 1
*   **Ingresos Totales:** $1,150,880,400 (La de mayores ingresos).
*   **Costo de Envío Promedio:** $26,018 (El más alto, lo cual puede afectar el margen si lo cubre el vendedor o disuadir clientes).
*   **Calificación Promedio:** 3.97 (La más baja).
*   **Categoría Más/Menos Vendida:** Muebles (465) / Artículos para el hogar (171).
*   **Producto Más/Menos Vendido:** Microondas (60) / Celular ABXY (33).

### Tienda 2
*   **Ingresos Totales:** $1,116,343,500
*   **Costo de Envío Promedio:** $25,216
*   **Calificación Promedio:** 4.03
*   **Categoría Más/Menos Vendida:** Muebles (442) / Artículos para el hogar (181).
*   **Producto Más/Menos Vendido:** Iniciando en programación (65) / Juego de mesa (32).

### Tienda 3
*   **Ingresos Totales:** $1,098,019,600
*   **Costo de Envío Promedio:** $24,805
*   **Calificación Promedio:** 4.04 (La mejor calificación promedio, indicando altos niveles de satisfacción).
*   **Categoría Más/Menos Vendida:** Muebles (499) / Artículos para el hogar (177).
*   **Producto Más/Menos Vendido:** Kit de bancas (57) / Bloques de construcción (35).

### Tienda 4
*   **Ingresos Totales:** $1,038,375,700 (Los ingresos más bajos).
*   **Costo de Envío Promedio:** $23,459 (El costo de envío más bajo, una ventaja competitiva fuerte).
*   **Calificación Promedio:** 3.99
*   **Categoría Más/Menos Vendida:** Muebles (480) / Instrumentos musicales (170).
*   **Producto Más/Menos Vendido:** Cama box (62) / Guitarra eléctrica (33).

## Conclusión y Recomendación

Tras analizar todas las métricas, **se recomienda al Sr. Juan vender en la Tienda 3**.

**Justificación:**
1. Aunque la Tienda 1 es la que más vende, su alta tasa de costos de envío y la baja calificación (3.97) indican un entorno donde retener compradores y mantener rentabilidad a largo plazo es más difícil. 
2. La **Tienda 3** es el escenario más balanceado. Tiene la calificación promedio más alta (4.04), representando un público objetivo satisfecho.
3. Se mantiene competitiva en ingresos totales, que son altamente significativos (1.09 billones de pesos).
4. El costo de envío promedio de la Tienda 3 es más competitivo que el de las dos primeras, representando una ventaja crucial para los compradores y los márgenes de los vendedores.

En conclusión, la Tienda 3 ofrece al Sr. Juan el mejor entorno al balancear rentabilidad sostenida con una demostrada base de clientes leales y altamente satisfechos.
"""

new_cell = {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    line + "\n" if not line.endswith("\n") else line for line in markdown_text.splitlines()
  ]
}

nb["cells"].append(new_cell)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
