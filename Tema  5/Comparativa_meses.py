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

# Guardar el informe de la comparativa entre diciembre y noviembre
report_fin_año = dp.Report(comparativa_fin_año)
report_fin_año.save(path="Comparativa_fin_año.html", open=True)

# Filtrar los datos del mes de enero
datos_enero = df[df["Mes"] == "Enero"]
unidades_enero = datos_enero["Unidades"].sum()  # Sumar las unidades vendidas en enero

# Filtrar los datos del mes de febrero
datos_febrero = df[df["Mes"] == "Febrero"]
unidades_febrero = datos_febrero["Unidades"].sum()  # Sumar las unidades vendidas en febrero

# Calcular la diferencia entre las unidades vendidas en febrero y enero
diferencia_febrero_enero = unidades_febrero - unidades_enero

# Crear el objeto BigNumber para la comparativa entre enero y febrero
comparativa_principio_año = dp.BigNumber(
    heading="Unidades totales (Enero vs Febrero)",
    value=unidades_febrero,
    change=abs(diferencia_febrero_enero),
    is_upward_change=diferencia_febrero_enero > 0
)

# Guardar el informe de la comparativa entre enero y febrero
report_principio_año = dp.Report(comparativa_principio_año)
report_principio_año.save(path="Comparativa_principio_año.html", open=True)
