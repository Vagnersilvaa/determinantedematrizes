def determinante_ordem_1(matriz):
    return matriz[0][0]

def determinante_ordem_2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def determinante_ordem_3(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    principal = a*e*i + b*f*g + c*d*h
    secundaria = c*e*g + b*d*i + a*f*h
    
    return principal - secundaria

matriz_ordem_1 = [[2]]
print("Determinante da matriz de ordem 1:", determinante_ordem_1(matriz_ordem_1))

matriz_ordem_2 = [[2, 5], [7, 3]]
print("Determinante da matriz de ordem 2:", determinante_ordem_2(matriz_ordem_2))

matriz_ordem_3 = [[1, 2, 3], [2, 5, 6], [2, 5, 8]]
print("Determinante da matriz de ordem 3:", determinante_ordem_3(matriz_ordem_3))
