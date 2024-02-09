numeros = [1,2,3,4,5]

while numeros : # while numeros:  es igual a len(numeros) > 0:
    print(numeros[0])
    del numeros[0]
print("No hay mas elementos") 
print(list(numeros))