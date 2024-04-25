import pandas as pd
import math
import numpy

#distribucion exponencial
# binomial
#triangular

def exponencial (riList, media):
    resultsList = []
    variables = []
    variable = 0
    for num in riList:
        result = -media * numpy.log(1- num)
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
