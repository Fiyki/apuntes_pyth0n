import datapane as dp
import pandas as pd

fichero_csv = "DI_U05_A02_02.csv"  # Ruta del archivo CSV a cargar

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(fichero_csv)  # Carga el archivo CSV en un DataFrame

# Filtrar los datos del mes de diciembre
datos_diciembre = df[df["Mes"] == "Diciembre"]
unidades_diciembre = datos_diciembre["Unidades"].sum()  # Sumar las unidades vendidas en diciembre

# Filtrar los datos del mes de noviembre
datos_noviembre = df[df["Mes"] == "Noviembre"]
unidades_noviembre = datos_noviembre["Unidades"].sum()  # Sumar las unidades vendidas en noviembre

# Calcular la diferencia entre las unidades vendidas en diciembre y noviembre
diferencia_diciembre_noviembre = unidades_diciembre - unidades_noviembre

# Crear el objeto BigNumber para la comparativa entre diciembre y noviembre
comparativa_fin_año = dp.BigNumber(
    heading="Unidades totales (Diciembre vs Noviembre)",
    value=unidades_diciembre,
    change=diferencia_diciembre_noviembre,  # Agregar la diferencia directamente aquí
    is_upward_change=unidades_diciembre > unidades_noviembre
)



# Guardar el informe de las comparativas en un solo archivo HTML
report = dp.Report(comparativa_fin_año)
report.save(path="comparativa_año.html", open=True)
