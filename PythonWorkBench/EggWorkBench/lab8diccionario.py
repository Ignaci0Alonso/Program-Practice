paises = {
    "ar": "Argetina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}

while True:
    try:
        codigo = input("""Ingrese el codigo de pais:
    ar: Argetina,
    es: España,
    us: Estados Unidos,
    fr: Francia.
->""")
        print(paises[codigo])
        break
    except KeyError:
        print("""
              Codigo invalido.
              """)
    except:
        print("Error del sistema")




# prueba = False
# for clave, valor in paises.items():
#     if codigo == clave:
#         print(f"El codigo ingresado es del pais: {valor}")
#         prueba = True
# if prueba == False:
#         print("El codigo ingresado no existe.")
    