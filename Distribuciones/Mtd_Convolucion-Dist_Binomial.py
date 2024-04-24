import random

def es_defectuosa(ri, p):
    if ri < 1 - p:
        return 0  # pieza en buen estado
    else:
        return 1  # pieza defectuosa

def simular_inspeccion(N, p):
    piezas_defectuosas_por_lote = []
    for _ in range(N):
        ri = random.random()  # Generar un número aleatorio ri
        BE = es_defectuosa(ri, p)  # Determinar si la pieza es defectuosa
        piezas_defectuosas_por_lote.append(BE)
    return sum(piezas_defectuosas_por_lote)  # Devolver el total de piezas defectuosas en el lote

# Parámetros
N = 5  # Tamaño del lote
p = 0.03  # Probabilidad de que una pieza sea defectuosa

# Simulación de la inspección para varios lotes
num_lotes = 10  # Número de lotes a simular
for i in range(num_lotes):
    ri = random.random()  # Generar un número aleatorio ri para el lote
    num_piezas_defectuosas = simular_inspeccion(N, p)
    print(f"Lote {i+1}: Número de piezas defectuosas = {num_piezas_defectuosas}")
