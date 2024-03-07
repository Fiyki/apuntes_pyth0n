import datapane as dp  # Importa la biblioteca Datapane para la generación de informes
import pandas as pd  # Importa la biblioteca pandas para el manejo de datos

# Carga del archivo CSV
fichero_csv = "DatosOrigen.csv"
df = pd.read_csv(fichero_csv)  # Lee el archivo CSV y carga los datos en un DataFrame

# Gráfico de barras 1
ventas_2017 = df[df['AnyoFacturacion'] >= 2017]  # Filtra las ventas  para los  a partir del año 2017
ventas_2017 = ventas_2017.groupby(['AnyoFacturacion']).sum()  # Agrupa las ventas por año de facturación y suma
grafico_matplotlib_barras1 = ventas_2017.plot.bar(y='Importe', color='Yellow')  # Crea el gráfico de barras
grafico_datapane_barras1 = dp.Plot(grafico_matplotlib_barras1,
                                   responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Gráfico de líneas
ventas_2024 = df[df['AnyoFacturacion'] == 2024]  # Filtra las ventas solo para el año 2024
ventas_2024 = ventas_2024.groupby(['Tienda']).sum()  # Agrupa las ventas por tienda y suma
grafico_matplotlib_lineas = ventas_2024.plot(y='Importe', color='green')  # Crea el gráfico de líneas
grafico_datapane_lineas = dp.Plot(grafico_matplotlib_lineas,
                                  responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Gráfico de barras 2
ventas_2017_tienda = df[df['AnyoFacturacion'] == 2017]  # Filtra las ventas solo para el año 2017
ventas_2017_tienda = ventas_2017_tienda.groupby(['Tienda']).sum()  # Agrupa las ventas por tienda y suma
grafico_matplotlib_barras2 = ventas_2017_tienda.plot.bar(y='Importe', color='blue')  # Crea el gráfico de barras
grafico_datapane_barras2 = dp.Plot(grafico_matplotlib_barras2,
                                   responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Gráfico de barras 3
ventas_2017_producto = df[df['AnyoFacturacion'] >= 2017]  # Filtra las ventas desde el año 2017
ventas_2017_producto = ventas_2017_producto.groupby(['Producto']).sum()  # Agrupa las ventas por producto y suma
grafico_matplotlib_barras3 = ventas_2017_producto.plot.bar(y='Importe', color='red')  # Crea el gráfico de barras
grafico_datapane_barras3 = dp.Plot(grafico_matplotlib_barras3,
                                   responsive=False)  # Convierte el gráfico en un objeto Datapane Plot

# Creación de informe con selectores
report = dp.Report(
    grafico_datapane_barras1,
    grafico_datapane_lineas,
    grafico_datapane_barras2,
    grafico_datapane_barras3
)
# Guarda el informe y lo abre en el navegador
report.save(path='Informe_Ventas.html', open=True)
