import pandas as pd
url = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv'
url2 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv'
url3 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv'
url4 = 'https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv'
t1 = pd.read_csv(url)
t2 = pd.read_csv(url2)
t3 = pd.read_csv(url3)
t4 = pd.read_csv(url4)
tiendas = [t1, t2, t3, t4]
for i, t in enumerate(tiendas, 1):
    print(f'Tienda {i}:')
    print(f'Ingresos Totales: {t["Precio"].sum()}')
    print(f'Costo de Envio Promedio: {t["Costo de envío"].mean()}')
    print(f'Calificacion Promedio: {t["Calificación"].mean()}')
    cats = t["Categoría del Producto"].value_counts()
    print(f'Cat Mas Vendida: {cats.index[0]} ({cats.iloc[0]})')
    print(f'Cat Menos Vendida: {cats.index[-1]} ({cats.iloc[-1]})')
    prods = t["Producto"].value_counts()
    print(f'Prod Mas Vendido: {prods.index[0]} ({prods.iloc[0]})')
    print(f'Prod Menos Vendido: {prods.index[-1]} ({prods.iloc[-1]})')
    print()
