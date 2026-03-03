import json

notebook_path = "AluraStoreLatam.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

markdown_text = """# Extra: Análisis Geográfico de Ventas
En esta sección exploraremos la distribución de las ventas en función de su ubicación geográfica (latitud y longitud). Utilizaremos gráficos de dispersión y mapas de calor para identificar visualmente en qué regiones se concentra el mayor volumen de compras y analizar posibles patrones de rendimiento.
"""

new_md_cell = {
  "cell_type": "markdown",
  "metadata": {},
  "source": [line + "\n" for line in markdown_text.splitlines()]
}

code_text = """import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import folium
from folium.plugins import HeatMap

# Para el análisis, primero combinemos los datos de las tiendas para tener un panorama general, o analicemos cada una.
# Agregamos una columna para identificar de qué tienda proviene cada venta
tienda['Tienda'] = 'Tienda 1'
tienda2['Tienda'] = 'Tienda 2'
tienda3['Tienda'] = 'Tienda 3'
tienda4['Tienda'] = 'Tienda 4'

df_todas = pd.concat([tienda, tienda2, tienda3, tienda4])

# 1. Gráfico de dispersión (Scatter Plot) de las ventas (Longitud vs Latitud)
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df_todas, 
    x='lon', y='lat', 
    hue='Tienda', 
    alpha=0.6, 
    palette='Set1'
)
plt.title('Distribución Geográfica de Ventas por Tienda')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.show()

# 2. Análisis por lugar de compra (Ingresos)
ingresos_por_lugar = df_todas.groupby('Lugar de Compra')['Precio'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=ingresos_por_lugar.values, y=ingresos_por_lugar.index, palette='viridis')
plt.title('Top 10 Ciudades por Ingresos Totales')
plt.xlabel('Ingresos Totales')
plt.ylabel('Lugar de Compra')
plt.show()

# 3. Mapa Interactivo de Calor (Heatmap) usando Folium
# Centramos el mapa en Colombia aproximadamente (asumiendo que los datos son de Latam/Colombia por las coordenadas)
mapa = folium.Map(location=[4.5709, -74.2973], zoom_start=5)

# Preparamos los datos para el mapa de calor (limpiamos posibles NaN)
heat_data = df_todas[['lat', 'lon']].dropna().values.tolist()

# Añadimos el mapa de calor
HeatMap(heat_data, radius=15, blur=20).add_to(mapa)

# Mostramos el mapa
mapa
"""

new_code_cell = {
  "cell_type": "code",
  "metadata": {},
  "outputs": [],
  "execution_count": None,
  "source": [line + "\n" for line in code_text.splitlines()]
}

nb["cells"].append(new_md_cell)
nb["cells"].append(new_code_cell)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
