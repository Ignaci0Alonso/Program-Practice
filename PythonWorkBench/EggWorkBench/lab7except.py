def calcularSuma(num1, num2):
    return num1 + num2
def calcularResta(num1, num2):    
    return num1 - num2
def calcularDivision(num1, num2):
    return num1 / num2
def calcularMultiplicacion(num1, num2):
    return num1 * num2

def chequear_num(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error de ingreso. Debe ingresar un numero.")
while True:
    try:
        num1 = chequear_num("Ingrese el primer numero:")
        num2 = chequear_num("Ingrese el segundo numero:")
        print(f"""
          Los resultados de las operaciones son:
        Suma: {num1} + {num2} = {calcularSuma(num1,num2)}
        Resta: {num1} - {num2} = {calcularResta(num1,num2)}
        Multiplicación: {num1} * {num2} = {calcularMultiplicacion(num1,num2)}
        División: {num1} / {num2} = {calcularDivision(num1,num2)}
          """)
        break
    except ZeroDivisionError:
        print("No se puede dividir por '0'.")