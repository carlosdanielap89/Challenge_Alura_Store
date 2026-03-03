import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar datos
url = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv'
url2 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv'
url3 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv'
url4 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv'

t1 = pd.read_csv(url)
t2 = pd.read_csv(url2)
t3 = pd.read_csv(url3)
t4 = pd.read_csv(url4)

tiendas_nombres = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
ingresos = [t1['Precio'].sum(), t2['Precio'].sum(), t3['Precio'].sum(), t4['Precio'].sum()]
calificaciones = [t1['Calificación'].mean(), t2['Calificación'].mean(), t3['Calificación'].mean(), t4['Calificación'].mean()]
envio = [t1['Costo de envío'].mean(), t2['Costo de envío'].mean(), t3['Costo de envío'].mean(), t4['Costo de envío'].mean()]

# 1. Gráfico de Ingresos
plt.figure(figsize=(8, 5))
plt.bar(tiendas_nombres, ingresos, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Ingresos Totales por Tienda')
plt.ylabel('Ingresos')
plt.tight_layout()
plt.savefig('ingresos.png')
plt.close()

# 2. Gráfico de Calificaciones
plt.figure(figsize=(8, 5))
plt.plot(tiendas_nombres, calificaciones, marker='o', linestyle='-', color='purple', markersize=8)
plt.title('Calificación Promedio por Tienda')
plt.ylabel('Calificación (1 - 5)')
plt.ylim(3.8, 4.2)
plt.tight_layout()
plt.savefig('calificaciones.png')
plt.close()

# 3. Gráfico de Categorías Tienda 3 (Pie Chart)
cats_t3 = t3['Categoría del Producto'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(cats_t3.values, labels=cats_t3.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribución de Categorías en la Tienda 3')
plt.tight_layout()
plt.savefig('categorias_t3.png')
plt.close()

print("Imágenes generadas exitosamente.")
