import pandas as pd
import math
import numpy as np

#distribucion exponencial
# binomial
#triangular

def exponencial (riList, media):
    resultsList = []
    variables = []
    variable = 0
    for num in riList:
        result = -media * np.log(1- num)
        resultsList.append(result)
        variables.append(variable)
        variable = variable + 1

    for i in variables:
        print(f"Variable {i}    Ri = {riList[i]}  Resultado:   {resultsList[i]}")

def binomial(riList, probabilidad):
        Ri = riList

        # Probabilidad
        p = probabilidad

        # Crear un DataFrame que almacena los valores de ri y su comparación, y los imprime en forma de tabla acá bien bonito
        df = pd.DataFrame(Ri, columns=['Ri'])

        # fórmula para determinar si cada pieza es defectuosa
        df['BE'] = df['Ri'].apply(lambda ri: 1 if ri > (1 - p) else 0)

        # Contar el número de piezas defectuosas
        defectuosas = df['BE'].sum()

        # Imprimir el DataFrame y el número total de piezas defectuosas
        print(df)
        print(f"Número total de piezas defectuosas: {defectuosas}")

def triangular(riLista, rjLista, valor_minimo, moda, valor_maximo):

    ri = riLista
    rj = rjLista

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


def main(): 

        print("Elige un metodo: ")
        print("1. Exponencial   2.Triangular    3.Binomial")
        metodoSeleccionado = int(input())

        if metodoSeleccionado == 1: 
            listaRi = []
            print("ingresa la cantidad de numeros ri")
            cantidadRi = int(input())

            print("Ingrsa uno por uno los numeros")
            num = 1
            while num <= cantidadRi: 
                listaRi.append(float(input(num)))
                num = num +1
            print("Ingresa la media")
            media = float(input())

            exponencial(listaRi, media)

        if metodoSeleccionado == 2: 
            listaRi = []
            listaRj = []
            min = 0
            max = 0
            moda = 0
            print("ingresa la cantidad de numeros ri y rj")
            cantidadR = int(input())
            print("Ingresa los numeros de ri")
            num = 1
            while num <= cantidadR: 
                 listaRi.append(float(input(num)))
                 num = num +1
            print("Ingresa los numeros de rj")
            nume = 1
            while nume <= cantidadR: 
                 listaRj.append(float(input(num)))
                 nume = nume +1
            
            print("Ingresa la moda")
            moda = float(input())
            print("Ingresa el maximo")
            max = float(input())
            print("Ingresa el minimo")
            min = float(input())

            triangular(listaRi, listaRj, min, moda, max)

        
        if metodoSeleccionado == 3:
             listaRi = []
             print("ingresa la cantidad de numeros ri")
             cantidadRi = int(input())
             print("Ingrsa uno por uno los numeros")
             num = 1
             while num <= cantidadRi: 
                listaRi.append(float(input(num)))
                num = num +1
             print("Ingresa la probabilidad")
             probabilidad = float(input())

             binomial(listaRi, probabilidad)
             

if __name__ == "__main__":
    main()
