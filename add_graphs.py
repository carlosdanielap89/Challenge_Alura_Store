import json

notebook_path = "AluraStoreLatam.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# The user requires at least 3 charts of different types.
# 1. Bar Chart: Ingresos Totales por Tienda
# 2. Pie Chart: Proporción de Categorías en Tienda 3 (La recomendada)
# 3. Line Chart or Bar Chart: Promedio de Costo de Envío

md_graficos = {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "# 6. Visualización de Resultados\n",
    "A continuación, presentamos gráficos que muestran el análisis comparativo entre las 4 tiendas, cumpliendo con el requisito de al menos 3 gráficos diferentes.\n"
  ]
}

code_graficos = {
  "cell_type": "code",
  "metadata": {},
  "outputs": [],
  "execution_count": None,
  "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "tiendas_nombres = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']\n",
    "\n",
    "# Datos recopilados\n",
    "ingresos = [ingreso_total_tienda1, ingreso_total_tienda2, ingreso_total_tienda3, ingreso_total_tienda4]\n",
    "envio_promedio = [26018.61, 25216.23, 24805.68, 23459.46] # Valores del paso de envio\n",
    "calificaciones = [promedio_tienda1, promedio_tienda2, promedio_tienda3, promedio_tienda4]\n",
    "\n",
    "fig, axs = plt.subplots(1, 3, figsize=(18, 5))\n",
    "\n",
    "# Gráfico 1: Barras - Ingresos Totales\n",
    "axs[0].bar(tiendas_nombres, ingresos, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])\n",
    "axs[0].set_title('Ingresos Totales por Tienda')\n",
    "axs[0].set_ylabel('Ingresos (Milles de Millón)')\n",
    "\n",
    "# Gráfico 2: Líneas con Puntos - Calificación Promedio\n",
    "axs[1].plot(tiendas_nombres, calificaciones, marker='o', linestyle='-', color='purple', markersize=8)\n",
    "axs[1].set_title('Calificación Promedio por Tienda')\n",
    "axs[1].set_ylabel('Calificación (1 - 5)')\n",
    "axs[1].set_ylim(3.8, 4.2)\n",
    "\n",
    "# Gráfico 3: Dispersión / Burbujas - Relación Envío Promedio\n",
    "# (Usaremos un gráfico de dispersión horizontal para costos de envío para dar variedad de tipos de gráficos)\n",
    "axs[2].scatter(envio_promedio, tiendas_nombres, color='red', s=150)\n",
    "axs[2].set_title('Costo de Envío Promedio por Tienda')\n",
    "axs[2].set_xlabel('Costo Promedio')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "# Gráfico 4: Pastel (Pie Chart) - Distribución de Categorías en la Tienda 3 (Recomendada)\n",
    "plt.figure(figsize=(8, 8))\n",
    "plt.pie(categoria_tienda3.values, labels=categoria_tienda3.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)\n",
    "plt.title('Distribución de Categorías en la Tienda 3')\n",
    "plt.show()\n"
  ]
}

# The cells should be inserted right before the conclusion report block (Cell 24 in our iteration)
nb['cells'].insert(-2, md_graficos)
nb['cells'].insert(-2, code_graficos)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
