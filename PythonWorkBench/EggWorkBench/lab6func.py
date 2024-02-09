def superior(funcion, lista):
    resultado = []
    for numero in lista:
        resultado.append(funcion(numero))
    return resultado

def calcularCubo(numero):
    return numero ** 3

lista = [2, 3, 4]
print(superior(calcularCubo, lista))