import datapane as dp
import pandas as pd

fichero_csv = "C:/Users/danmo/Downloads/DI_U05_A02_02.csv"  # Ruta del archivo
df = pd.read_csv(fichero_csv)  # cargammos el fichero en un Data frame

table = dp.Table(df)  # Creamos un objeto tabla con los datos del Dataframe
data_table = dp.DataTable(df)  # Creamos un objeto DataTable con los datos del Dataframe

# informe imprimir
report_imprimir = dp.Report(table)  # Creamos un informe que solo podemos visualizar al usar el table
report_imprimir.save( path="C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Imprimir_clase1.html",open=True)  # Guarda el informe en un fichero html y lo abre al iniciar el programa si queremos que solo lo genere el open= lo ponemos en false

# informe_filtrar
report_visualizar = dp.Report(data_table)  # Creamos un informe en el que podemos filtrar al usar el data_Table
report_visualizar.save(path="C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Visualizar_clase1.html",open=True)  # Guarda el informe en un fichero html y lo abre al iniciar el programa si queremos que solo lo genere el open= lo ponemos en false

# Informe completo
report = dp.Report(table, data_table)  # Creamos un informe que cree los 2 a la vez
report.save( path="C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Remix.html",open=True) # Guarda el informe en un fichero html y lo abre al iniciar el programa si queremos que solo lo genere el open= lo ponemos en false
