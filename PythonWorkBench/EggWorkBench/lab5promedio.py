cantidad = int(input("Ingrese la cantidad de argumentos: "))
listaDeNumeros = []
total = 0

for i in range(cantidad):
    listaDeNumeros.append(int(input("Ingrese un numero:")))

for i in range(cantidad):
    total += listaDeNumeros[i]

promedio = total / cantidad

print(f"El promedio de los valores ingresados es: {promedio}")
