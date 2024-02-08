import os  # Importa el módulo os para interactuar con el sistema operativo
import datapane as dp  # Importa la biblioteca datapane como dp
import pandas as pd  # Importa la biblioteca pandas como pd

# Rutas de los archivos a guardar
ruta_imprimir = "C:/Users/danmo/OneDrive/Documentos/GitHub/apuntes_pyth0n/Tema  5/Imprimir_clase1.html"  # Ruta para guardar el archivo de impresión
ruta_visualizar = "C:/Users/danmo/OneDrive/Documentos/GitHub/apuntes_pyth0n/Tema  5/Visualizar_clase1.html"  # Ruta para guardar el archivo de visualización
ruta_remix = "C:/Users/danmo/OneDrive/Documentos/GitHub/apuntes_pyth0n/Tema  5/Remix.html"  # Ruta para guardar el archivo remix

# Ruta del archivo CSV
fichero_csv = "C:/Users/danmo/Downloads/DI_U05_A02_02.csv"  # Ruta del archivo CSV a cargar

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(fichero_csv)  # Carga el archivo CSV en un DataFrame

# Crear objetos tabla y DataTable
table = dp.Table(df)  # Crea un objeto tabla a partir del DataFrame
data_table = dp.DataTable(df)  # Crea un objeto DataTable a partir del DataFrame

# Crear informe para imprimir
report_imprimir = dp.Report(table)  # Crea un informe para imprimir con la tabla

# Crear informe para visualizar
report_visualizar = dp.Report(data_table)  # Crea un informe para visualizar con la DataTable

# Crear informe completo
report = dp.Report(table, data_table)  # Crea un informe completo con la tabla y la DataTable

# Verificar si los archivos ya existen y preguntar si se desean sobrescribir
if os.path.exists(ruta_imprimir):  # Verifica si el archivo de impresión ya existe
    respuesta = input("El archivo de impresión ya existe. ¿Deseas sobrescribirlo? (s/n): ")  # Pregunta al usuario si desea sobrescribirlo
    if respuesta.lower() == 's':  # Si la respuesta es 's', sobrescribe el archivo
        if os.path.exists(ruta_imprimir):
            os.remove(ruta_imprimir)  # Elimina el archivo existente antes de guardar el nuevo
        report_imprimir.save(path=ruta_imprimir, open=True)  # Guarda el informe de impresión
    else:
        print("El archivo de impresión no se ha sobrescrito.")  # Si la respuesta no es 's', informa al usuario que no se sobrescribió
else:
    report_imprimir.save(path=ruta_imprimir, open=True)  # Si el archivo no existe, guarda el informe de impresión

if os.path.exists(ruta_visualizar):  # Verifica si el archivo de visualización ya existe
    respuesta = input("El archivo de visualización ya existe. ¿Deseas sobrescribirlo? (s/n): ")  # Pregunta al usuario si desea sobrescribirlo
    if respuesta.lower() == 's':  # Si la respuesta es 's', sobrescribe el archivo
        if os.path.exists(ruta_visualizar):
            os.remove(ruta_visualizar)  # Elimina el archivo existente antes de guardar el nuevo
        report_visualizar.save(path=ruta_visualizar, open=True)  # Guarda el informe de visualización
    else:
        print("El archivo de visualización no se ha sobrescrito.")  # Si la respuesta no es 's', informa al usuario que no se sobrescribió
else:
    report_visualizar.save(path=ruta_visualizar, open=True)  # Si el archivo no existe, guarda el informe de visualización

if os.path.exists(ruta_remix):  # Verifica si el archivo remix ya existe
    respuesta = input("El archivo de remix ya existe. ¿Deseas sobrescribirlo? (s/n): ")  # Pregunta al usuario si desea sobrescribirlo
    if respuesta.lower() == 's':  # Si la respuesta es 's', sobrescribe el archivo
        if os.path.exists(ruta_remix):
            os.remove(ruta_remix)  # Elimina el archivo existente antes de guardar el nuevo
        report.save(path=ruta_remix, open=True)  # Guarda el informe completo
    else:
        print("El archivo de remix no se ha sobrescrito.")  # Si la respuesta no es 's', informa al usuario que no se sobrescribió
else:
    report.save(path=ruta_remix, open=True)  # Si el archivo no existe, guarda el informe completo
