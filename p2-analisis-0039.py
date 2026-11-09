# Importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos Inmuebles Caleb Dorado NC = 0039")

inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}

df = pd.DataFrame(inmuebles)
print(df)

print(" +-+-+-+ Agrupar por una sola columna Metros Cuadrados +-+-+-+ ")
agrupado = df.groupby('Metros_Cuadrados')
print(agrupado)

# Habitaciones por cantidad de metros cuadrados
print(" +-+-+-+ Habitaciones por cantidad de metros cuadrados +-+-+-+")
print(agrupado['Habitaciones'].mean())
# Precios por cantidad de metros cuadrados (USD)
print(" +-+-+-+ Precio (miles de USD) por cantidad de metros cuadrados +-+-+-+")
print(agrupado['Precio_Miles_USD'].max())

print(" +-+ Caleb -+-+ Segunda Parte +-+- 0039 +-+")
print("Agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Habitaciones'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")

print("Agrega columnas al DataFrame")
print("Columna Team --> Equipo")
df['Equipo'] = ['A', 'B', 'A', 'B', 'A', 'B']
agrupado_multiple = df.groupby(['Metros_Cuadrados', 'Equipo'])['Habitaciones'].mean()
print(agrupado_multiple)