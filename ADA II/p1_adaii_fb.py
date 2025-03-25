import math
from helpers.procesar_pruebas import procesar_pruebas as pp

# Función para calcular el conflicto interno
def conflicto_interno(RS: list[list, int]) -> int:
    return sum([sa[0]*(sa[1] - sa[2])**2 for sa in RS[0]]) / sum([sa[0] for sa in RS[0]])

# Función para calcular el esfuerzo
def esfuerzo(RS: list[list, int], E: list[int]) -> int:
    return sum([math.ceil(abs(sa[1]-sa[2]) * sa[3] * E[index]) for (index, sa) in  enumerate(RS[0])])

# Función que calcula el conflicto luego de aplicar la estrategia E
def conflicto_modificado(RS, E):
    grupos = RS[0]
    num = 0
    den = 0
    for i, sa in enumerate(grupos):
        n_i, o1, o2, _ = sa
        # Quedan (n_i - e_i) agentes en el grupo
        n_rest = n_i - E[i]
        den += n_rest
        num += n_rest * (o1 - o2)**2
    # Evitar división por cero (se debe asegurar que no se remueven todos los agentes)
    return num/den if den > 0 else 0


def ModCI_fb(RS):
    grupos = RS[0]
    R_max = RS[1]
    n = len(grupos)
    mejor_estrategia = None
    mejor_ci = float('inf')
    mejor_esfuerzo = None

    # Función recursiva para enumerar combinaciones de e_i en cada grupo.
    def backtrack(i: int, current_E: list[int]):
        nonlocal mejor_estrategia, mejor_ci, mejor_esfuerzo
        if i == n:
            esfuerzo_total = esfuerzo(RS, current_E)
            if esfuerzo_total <= R_max:
                conf = conflicto_modificado(RS, current_E)
                # Actualizar si se mejora
                if conf < mejor_ci:
                    mejor_ci = conf
                    mejor_estrategia = current_E.copy()
                    mejor_esfuerzo = esfuerzo_total
            return
        
        n_i: int = grupos[i][0]
        for e in range(n_i + 1):
            current_E.append(e)
            backtrack(i+1, current_E)
            current_E.pop()
    
    backtrack(0, [])
    return mejor_estrategia, mejor_ci, mejor_esfuerzo

# Casos de prueba

RS: list[list, int] = [[[3,-100,50,0.5], [1,100,80,0.1], [1,-10,0,0.5]], 80]
RS2: list[list, int] = [[[3, -100, 100, 0.8], [2, 100, 80, 0.5], [4, -10,10,0.5]], 400]
RS3: list[list, int] = [[[5, -6, -94, 0.062], [6, -84, -7, 0.378], [1, -52, 33, 0.073], [4, 77, -47, 0.626], [4, -75, 75, 0.718]], 4044]
RS4: list[list, int] = [[[9,-96,12,0.951], [9,-79,47,0.993], [8,16,-63,0.994], [3,-12,92,0.087], [3,-64,-50,0.884], [1,-54,-33,0.216], [2,-10,-77,0.344], [7,34,-58,0.05], [7,21,24,0.451], [3,-82,-55,0.955]], 64]

prueba1 = pp("./pruebas/Prueba1.txt")
prueba2 = pp("./pruebas/Prueba2.txt")
prueba3 = pp("./pruebas/Prueba3.txt")
prueba7 = pp("./pruebas/Prueba7.txt")

print("----- Fuerza Bruta -----")
E_fb, conf_fb, cost_fb = ModCI_fb(prueba7)
print("Estrategia:", E_fb)
print("Conflicto modificado:", conf_fb)
print("Esfuerzo:", cost_fb)




