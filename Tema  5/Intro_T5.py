import datapane as dp
import pandas as pd
import os

# Rutas de los archivos a guardar
ruta_imprimir = "C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Imprimir_clase1.html"
ruta_visualizar = "C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Visualizar_clase1.html"
ruta_remix = "C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema  5/Remix.html"

# Ruta del archivo CSV
fichero_csv = "C:/Users/danmo/Downloads/DI_U05_A02_02.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(fichero_csv)

# Crear objetos tabla y DataTable
table = dp.Table(df)
data_table = dp.DataTable(df)

# Crear informe para imprimir
report_imprimir = dp.Report(table)

# Crear informe para visualizar
report_visualizar = dp.Report(data_table)

# Crear informe completo
report = dp.Report(table, data_table)

# Verificar si los archivos ya existen y preguntar si se desean sobrescribir
if os.path.exists(ruta_imprimir):
    respuesta = input("El archivo de impresión ya existe. ¿Deseas sobrescribirlo? (s/n): ")
    if respuesta.lower() == 's':
        if os.path.exists(ruta_imprimir):
            os.remove(ruta_imprimir)  # Eliminar el archivo existente antes de guardar
        report_imprimir.save(path=ruta_imprimir, open=True)
    else:
        print("El archivo de impresión no se ha sobrescrito.")
else:
    report_imprimir.save(path=ruta_imprimir, open=True)

if os.path.exists(ruta_visualizar):
    respuesta = input("El archivo de visualización ya existe. ¿Deseas sobrescribirlo? (s/n): ")
    if respuesta.lower() == 's':
        if os.path.exists(ruta_visualizar):
            os.remove(ruta_visualizar)  # Eliminar el archivo existente antes de guardar
        report_visualizar.save(path=ruta_visualizar, open=True)
    else:
        print("El archivo de visualización no se ha sobrescrito.")
else:
    report_visualizar.save(path=ruta_visualizar, open=True)

if os.path.exists(ruta_remix):
    respuesta = input("El archivo de remix ya existe. ¿Deseas sobrescribirlo? (s/n): ")
    if respuesta.lower() == 's':
        if os.path.exists(ruta_remix):
            os.remove(ruta_remix)  # Eliminar el archivo existente antes de guardar
        report.save(path=ruta_remix, open=True)
    else:
        print("El archivo de remix no se ha sobrescrito.")
else:
    report.save(path=ruta_remix, open=True)
