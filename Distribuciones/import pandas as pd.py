import pandas as pd
import numpy as np

ri = [0.456, 0.967, 0.982, 0.134, 0.536]
rj = [0.231, 0.421, 0.853, 0.048, 0.675]

valor_minimo = 5
moda = 10
valor_maximo = 20

a = valor_minimo
b = valor_maximo
c = moda 

condicion = (c-a)/(b-a)

menor_igual = []
mayor = []

for i, j in zip(ri, rj):
    if j <= condicion:
        resultado = round((a + (c - a) * np.sqrt(i)), 4)
        # resultado = round(resultado, 4)
        menor_igual.append(resultado)
    else:
        menor_igual.append(np.nan)
    
    if j > condicion:
        resultado2 = round((b - ((b - c) * np.sqrt(1-i))), 4)
        # resultado2 = round(resultado2, 4)
        mayor.append(resultado2)
    else:
        mayor.append(np.nan)

c1 = "  Si rj <= " + str(round(condicion, 4))
c2 = "  Si rj > " + str(round(condicion, 4))

df = pd.DataFrame({
    "rj": rj,
    "ri": ri,
    c1: menor_igual,
    c2: mayor
})

df = df.replace(np.nan, '-')
df.index = df.index + 1

print(df)