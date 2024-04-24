import pandas as pd

Ri = [0.02, 0.31, 0.70, 0.83, 0.50]

# Probabilidad
p = 0.03

# Crear un DataFrame que almacena los valores de ri y su comparación, y los imprime en forma de tabla acá bien bonito
df = pd.DataFrame(Ri, columns=['Ri'])

# fórmula para determinar si cada pieza es defectuosa
df['BE'] = df['Ri'].apply(lambda ri: 1 if ri > (1 - p) else 0)

# Contar el número de piezas defectuosas
defectuosas = df['BE'].sum()

# Imprimir el DataFrame y el número total de piezas defectuosas
print(df)
print(f"Número total de piezas defectuosas: {defectuosas}")

