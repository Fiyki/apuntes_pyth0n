import datapane as dp  # Importa la biblioteca Datapane para la generación de informes
import pandas as pd  # Importa la biblioteca pandas para el manejo de datos

# Carga del archivo CSV
fichero_csv = "DI_U05_A02_PP_E_01.csv"
df = pd.read_csv(fichero_csv)  # Lee el archivo CSV y carga los datos en un DataFrame

# Gráfico de líneas
ventas_anuales = df.groupby(['Año'], sort=False).sum()  # Agrupa las ventas por año y suma
# Crea un gráfico de líneas utilizando Matplotlib con las unidades vendidas por año
grafico_matplot_lineas = ventas_anuales.plot(y='Ventas', color='black')  # Se establece el color negro para las líneas
# Crea un objeto de gráfico de Datapane a partir del gráfico de líneas de Matplotlib
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

# Gráfico de barras
ventas_2021 = df[df['Año'] == 2021]  # Filtra las ventas solo para el año 2021
ventas_region_2021 = ventas_2021.groupby(['Región']).sum()  # Agrupa las ventas por región y suma
grafico_matplotlib_barras = ventas_region_2021.plot.bar(y='Ventas', color='green')  # Crea el gráfico de barras al poner plot.bar
grafico_datapane_barras = dp.Plot(grafico_matplotlib_barras,
                                  responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Gráfico de sectores
ventas_tipo_producto = df.groupby(['Tipo de producto']).sum()  # Agrupa las ventas por tipo de producto y suma
grafico_sectores = ventas_tipo_producto.plot.pie(y='Ventas', legend=False, ylabel="",cmap='viridis')  # Crea el gráfico de sectores al poner el .plot.pie
grafico_datapane_sectores = dp.Plot(grafico_sectores,
                                    responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Creación de informe con selectores
report = dp.Report(
    grafico_datapane_lineas,  # Añade el gráfico de líneas al informe
    grafico_datapane_barras,  # Añade el gráfico de barras al informe
    grafico_datapane_sectores  # Añade el gráfico de sectores al informe
)

# Guarda el informe y lo abre en el navegador
report.save(path='Informe_Ventas.html', open=True)
