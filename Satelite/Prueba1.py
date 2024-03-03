import datapane as dp
import pandas as pd

fichero_csv = "2024.02.24_1-1.csv"
df = pd.read_csv(fichero_csv)

datos_uno_diez = df[df["Paquete"] <= 10]
unidades_uno_diez = datos_uno_diez["Paquete"].sum()

datos_once_veinte = df[(df["Paquete"] >= 11) & (df["Paquete"] <= 20)]
unidades_once_veinte = datos_once_veinte["Paquete"].sum()

diferencia_uno_diez_once_veinte = unidades_uno_diez - unidades_once_veinte

comparativa_paquetes = dp.BigNumber(
    heading="Paquetes totales (10 vs 20)",
    value=unidades_uno_diez,
    change=diferencia_uno_diez_once_veinte,
    is_upward_change=unidades_uno_diez > unidades_once_veinte
)

report_primeros_veinte = dp.Report(comparativa_paquetes)

data_table = dp.DataTable(df)

report_visualizar = dp.Report(data_table)

lineas1 = df.groupby('Paquete', sort=False).sum()
grafico_matplot_lineas = lineas1.plot(y='Altitud', color='black')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

lineas2 = df.groupby('Paquete', sort=False).sum()
grafico_matplot_lineas2 = lineas2.plot(y='Temperatura', color='blue')
grafico_datapane_lineas2 = dp.Plot(grafico_matplot_lineas2, responsive=False)

# Crea y guarda el informe del primer gráfico de líneas
report_grafico = dp.Report(
    dp.Select(
        blocks=[
            comparativa_paquetes,
            grafico_datapane_lineas,grafico_datapane_lineas2,
            report_visualizar
        ]
    )
)
report_grafico.save(path='Grafico1.html', open=True)

