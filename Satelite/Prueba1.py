import datapane as dp  # Importa la biblioteca Datapane para crear informes interactivos
import pandas as pd  # Importa la biblioteca pandas para la manipulación de datos

fichero_csv = "2024.02.24_1-1.csv"  # Ruta del archivo CSV a cargar

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(fichero_csv, encoding='latin1')  # Carga el archivo CSV en un DataFrame

# Filtrar los datos de los paquetes del 1 al 10
datos_uno_diez = df[
    df["Paquete"] <= 10]  # Filtra los datos del DataFrame donde el valor de "Paquete" es menor o igual a 10
unidades_uno_diez = datos_uno_diez["Paquete"].sum()  # Suma los valores de la columna "Paquete" filtrados anteriormentew
# Filtrar los datos de los paquetes de 11 a 20
datos_once_veinte = df[
    df["Paquete"] >= 11 & (df["Paquete"] <= 20)]  # Filtra los datos del DataFrame donde el valor de "Paquete" es mayor o igual a 11
unidades_once_veinte = datos_once_veinte[
    "Paquete"].sum()  # Suma los valores de la columna "Paquete" filtrados anteriormente

diferencia_uno_diez_once_veinte = unidades_uno_diez - unidades_once_veinte

# Crear el objeto BigNumber para la comparativa entre diciembre y noviembre
comparativa_paquetes = dp.BigNumber(
    # Crea un objeto BigNumber para representar la comparativa entre diciembre y noviembre
    heading="Paquetes totales (10 vs 20)",  # Encabezado del objeto BigNumber
    value=unidades_uno_diez,  # Valor total de los paquetes del 1 al 10
    change=diferencia_uno_diez_once_veinte,  # Cambio de unidades entre 1 y 20
    is_upward_change=unidades_uno_diez > unidades_once_veinte
    # Indica si hay un aumento en las unidades de diciembre respecto a las otras
)
report_primeros_veinte = dp.Report(comparativa_paquetes)  # Crea un informe de Datapane con el objeto BigNumber

data_table = dp.DataTable(
    df)  # Crea un objeto DataTable a partir del DataFrame para visualizar los datos en forma de tabla

report_visualizar = dp.Report(data_table)  # Crea un informe de Datapane para visualizar la tabla de datos

# Gráfico de líneas:
# Agrupa los datos por altitud y suma los metros para cada altitud
lineas1 = df.groupby('Paquete',
                     sort=False).sum()  # Agrupa los datos por altitud y suma los metros para cada altitud

# Crea un gráfico de líneas utilizando Matplotlib con los metros por altitud
grafico_matplot_lineas = lineas1.plot(y='Altitud_[m]',
                                      color='black')  # Se establece el color negro para las líneas

# Crea un objeto de gráfico de Datapane a partir del gráfico de líneas de Matplotlib
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas,
                                  responsive=False)  # Crea un objeto de gráfico de Datapane a partir del gráfico de líneas de Matplotlib

# Crea un informe de Datapane que contiene el gráfico de líneas
report = dp.Report(
    dp.Select(
        blocks=[
            comparativa_paquetes,  # Agrega el objeto BigNumber al informe
            grafico_datapane_lineas,  # Agrega el gráfico de líneas al informe
            report_visualizar  # Agrega la tabla de datos al informe
        ]
    )
)
# Guarda el informe en un archivo HTML y ábrelo en el navegador
report.save(path='Grafico.html', open=True)
