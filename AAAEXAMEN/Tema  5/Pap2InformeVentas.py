import datapane as dp
import pandas as pd

fichero_csv = "DI_U05_A02_PP_E_01.csv"
df = pd.read_csv(fichero_csv)

datos_2021 = df[df['Año'] == 2021]
unidades_2021 = datos_2021['Ventas'].sum()

datos_2020 = df[df['Año'] == 2020]
unidades_2020 = datos_2020['Ventas'].sum()

cambio_unidades = unidades_2021 - unidades_2020
is_upward_change = cambio_unidades >= 0

unidades = dp.BigNumber(
    heading='Informe de ventas',
    value=unidades_2021,
    change=cambio_unidades,
    is_upward_change=is_upward_change
)

titulo = dp.HTML('''
<p style="font-size:40px;text-align:center;color:#ffffff;background-color:#4d4d4d;">
    Informe de ventas
</p>''')
fichero = dp.Attachment(file='DI_U05_A02_02.csv')
texto = dp.Text('Puedes descargar el fichero.')

report = dp.Report(titulo, unidades, texto, fichero)
report.save(path="Informe.html", open=True)
