import datapane as dp
import pandas as pd

# Definir el nombre del archivo CSV
archivo_csv = "DatosOrigen.csv"

try:
    # Leer el archivo CSV en un DataFrame
    datos = pd.read_csv(archivo_csv)

    # Crear el informe con Datapane
    informe = dp.Report(
        dp.Page(
            dp.Plot(datos.groupby('AnyoFacturacion')['Importe'].sum().plot(kind='bar'), name="VentasPorAnio"),
            dp.Text("Comparación con el primer año:", name="Informe"),
            dp.Table(pd.DataFrame({
                'Año': [2017, 2024],
                'Importe Total': [
                    datos[datos['AnyoFacturacion'] == 2017]['Importe'].sum(),
                    datos[datos['AnyoFacturacion'] == 2024]['Importe'].sum()
                ],
                'Comparación (%)': [
                    100,
                    (datos[datos['AnyoFacturacion'] == 2024]['Importe'].sum() /
                     datos[datos['AnyoFacturacion'] == 2017]['Importe'].sum() * 100 - 100)
                ]
            })),
        ),
        dp.Page(
            dp.Text("Importe total de ventas del año 2024 por tienda:"),
            dp.Table(datos[datos['AnyoFacturacion'] == 2024].groupby('Tienda')['Importe'].sum().reset_index())
        ),
        dp.Page(
            dp.Text("Tabla con los datos y filtrar:"),
            dp.DataTable(datos)
        ),
    )

    # Guardar el informe en un archivo HTML con enlace de descarga
    informe.save(path="Examen.html", open=True)

except FileNotFoundError:
    print(f"El archivo {archivo_csv} no se encontró.")
except Exception as e:
    print("Ocurrió un error:", str(e))
