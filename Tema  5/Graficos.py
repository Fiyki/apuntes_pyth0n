import datapane as dp
import matplotlib.pyplot as plt
import pandas as pd

fichero_csv = "DI_U05_A02_02.csv"  # Ruta del archivo CSV a cargar

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(fichero_csv)  # Carga el archivo CSV en un DataFrame

# Gráfico de líneas
ventas_mes = df.groupby(['Mes'], sort=False).sum()  # Agrupar los datos por mes y sumar las unidades vendidas
grafico_lineas = ventas_mes.plot(y='Unidades', color="red")  # Crear el gráfico de líneas utilizando matplotlib
grafico_datapane_lineas = dp.Plot(grafico_lineas,
                                  responsive=False)  # Convertir el gráfico de matplotlib a un objeto Plot de Datapane

# Gráfico de barras
ventas_vendedor = df.groupby(['Nombre']).sum()  # Agrupar los datos por nombre del vendedor y sumar los importes
grafico_barras = ventas_vendedor.plot.bar(y='Importe (€)',
                                          color="yellow")  # Crear el gráfico de barras utilizando matplotlib
plt.tight_layout()  # Ajustar el diseño del gráfico para evitar que se corten las etiquetas
grafico_datapane_barras = dp.Plot(grafico_barras,
                                  responsive=False)  # Convertir el gráfico de matplotlib a un objeto Plot de Datapane

# Gráfico de sectores
grafico_sectores = ventas_vendedor.plot.pie(y='Unidades', legend=False, ylabel="",
                                            cmap='viridis')  # Crear el gráfico de sectores utilizando matplotlib
grafico_datapane_sectores = dp.Plot(grafico_sectores,
                                    responsive=False)  # Convertir el gráfico de matplotlib a un objeto Plot de Datapane

# Crear el informe que contiene los gráficos
report = dp.Report(
    dp.Group(
        grafico_datapane_lineas,
        grafico_datapane_barras,
        grafico_datapane_sectores,
        columns=2
    )
)
# Agrupar por Páginas
report = dp.Report(
    dp.Page(
        title="Página 1",
        blocks=[grafico_datapane_lineas, grafico_datapane_barras]
    ),
    dp.Page(
        title="Página 2",
        blocks=[grafico_datapane_sectores, grafico_datapane_lineas]
    ),
    dp.Page(
        title="Página 3",
        blocks=[grafico_datapane_barras, grafico_datapane_sectores]
    ),
)
