# personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
# with open("archivo.txt", "w") as file:
#     for nombre, edad in personas.items():
#         file.write(f"{nombre.lower()}-{edad}\n")
personas = {}
with open("archivo.txt", "r") as file:
    for linea in file:
        # EN UNA SOLA LINEA
        # persona[linea.strip().split("-")[0].capitalize()] = int(linea.strip().split("-")[1])

        # EN MULTIPLES LINEAS CON DESEMPAQUETAMIENTO
        nombreMin, edadStr = linea.strip().split("-")
        edad =  int(edadStr)
        nombre = nombreMin.capitalize()

        # EN MULRIPLES LINEAS EN LISTA
        # lista = linea.strip().split("-")
        # edad =  int(lista[1])
        # nombre = lista[0].capitalize()
        personas[nombre] = edad
print(personas)

    