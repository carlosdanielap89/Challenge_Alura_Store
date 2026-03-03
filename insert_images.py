with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

images_section = '\n### 📊 Visualizaciones Generadas\n\n'
images_section += '| Ingresos Totales por Tienda | Calificación Promedio | Distribución (Tienda 3) |\n'
images_section += '|:---:|:---:|:---:|\n'
images_section += '| <img src="ingresos.png" width="300"> | <img src="calificaciones.png" width="300"> | <img src="categorias_t3.png" width="300"> |\n'

insert_marker = '## 📈 Insights y Hallazgos Principales'
parts = readme_content.split(insert_marker)

if len(parts) > 1:
    new_readme = parts[0] + insert_marker + '\n' + images_section + parts[1]
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    print('Imágenes añadidas al README con éxito')
else:
    print('No se encontró el marcador en el README.')
