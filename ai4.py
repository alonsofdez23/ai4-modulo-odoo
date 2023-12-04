# Importamos las librerías a utilizar: Pandas y Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Definimos el tema para la librería matplotlib
matplotlib.style.use('ggplot')

# Definimos los colores a utilizar en las barras de la gráfica
colors = ["#026670", "#F4976C", "#687864"]

# Lista proporcionada en el enunciado de la actividad
data = [
    [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

# Creamos un diccionario a partir de la lista del enunciado
datadic = {
    'Year': data[0],
    'Month': data[1],
    'Value': data[2]
}

# Creamos un DataFrame de Pandas a partir del diccionario creado
df = pd.DataFrame(datadic)

# Utilizamos el método pivot de Pandas para reorganizar los datos. Se especifica
# que 'Year' será el indice (Eje X), 'Month' se utilizará para las columnas y 'Value'
# proporcionará los valores en la tabla pivotada
pivot_df = df.pivot(index = 'Year', columns = 'Month', values = 'Value')


# Utiliza el método .loc de Pandas para seleccionar todas las filas (:) y las columnas
# específicas 'Jan', 'Feb', y 'Mar' del DataFrame pivot_df.
# .plot.bar(): Crea un gráfico de barras a partir de los datos seleccionados.
# En este caso, las columnas 'Jan', 'Feb', y 'Mar' se visualizarán como barras.
# stacked=True: Indica que las barras deben ser apiladas en lugar de colocarse una al
# lado de la otra. Cada barra representa una suma acumulativa de los valores de las
# columnas seleccionadas.
# figsize=(10, 7): Establece las dimensiones de la figura en la que se visualizará el
# gráfico. En este caso, la figura tendrá un ancho de 10 unidades y una altura de 7 unidades.
pivot_df.loc[:, ['Jan', 'Feb', 'Mar']].plot.bar(stacked = True, color = colors, figsize = (10, 7))

# Finalmente, se utiliza plt.show() para mostrar el gráfico generado.
plt.show()