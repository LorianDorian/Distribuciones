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

    
    df = pd.DataFrame({
        "Variable": [variables], 
        "ri": [riList],
        "Resultados": [resultsList]
})

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

if __name__ == "__main__":
    main()
