# Importación de bibliotecas
import datapane as dp  # Importa la biblioteca Datapane para la generación de informes
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para la visualización de datos
import pandas as pd  # Importa la biblioteca pandas para el manejo de datos

# Nombre del archivo CSV que contiene los datos
fichero_csv = "DI_U05_A02_02.csv"

# Carga el archivo CSV en un DataFrame utilizando pandas
df = pd.read_csv(fichero_csv)

# Gráfico de líneas
## Agrupa los datos por mes y suma las ventas para cada mes
ventas_mes = df.groupby(['Mes'], sort=False).sum()
## Crea un gráfico de líneas utilizando Matplotlib con las unidades vendidas por mes
grafico_matplot_lineas = ventas_mes.plot(y='Unidades', color='black')
## Crea un objeto de gráfico de Datapane a partir del gráfico de líneas de Matplotlib
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

# Gráfico de barras
## Agrupa los datos por vendedor y suma las unidades vendidas y el importe para cada vendedor
ventas_vendedor = df.groupby(['Nombre']).sum()
## Crea un gráfico de barras utilizando Matplotlib con el importe total vendido por cada vendedor
grafico_matplotlib_barras = ventas_vendedor.plot.bar(y='Importe (€)', color='green')
## Ajusta el diseño del gráfico para evitar que se corten las etiquetas
plt.tight_layout()
## Crea un objeto de gráfico de Datapane a partir del gráfico de barras de Matplotlib
grafico_datapane_barras = dp.Plot(grafico_matplotlib_barras, responsive=False)

# Gráfico de sectores
grafico_sectores = ventas_vendedor.plot.pie(y='Unidades', legend=False, ylabel="", cmap='viridis')
## Crear el gráfico de sectores utilizando matplotlib
grafico_datapane_sectores = dp.Plot(grafico_sectores, responsive=False)
## Convertir el gráfico de matplotlib a un objeto Plot de Datapane

# Creación de informe con selectores
report = dp.Report(
    dp.Select(
        blocks=[
            grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores,
        ]
    )
)

# Guarda el informe en un archivo HTML y ábrelo en el navegador
report.save(path='Graficos.html', open=True)
