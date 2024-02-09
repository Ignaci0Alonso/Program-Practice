largo = int(input("Ingrese el tamaño de la colección de datos: "))
for i in range(largo):
    numero = int(input("Ingrese un numero: "))
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")    
    elif numero % 5 == 0:    
        print("Buzz")
    else:
        print(i)
        
