numero1 = 0
numero2 = 1
numero3 = 0
listaNumeros = []
for i in range(20):
    listaNumeros.append(numero1)
    numero3 = numero1
    numero1 = numero2
    numero2 = numero1 + numero3
print(list(listaNumeros))