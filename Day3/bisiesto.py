# calcular si un año es bisiesto
annio = input("ingresa el año a consultar si es Bisiesto\n")
annio_int = int(annio)

# si el resultado de dividir annio_int entre 4 es 0
if annio_int % 4 == 0:
    # revisa si podemos dividir annio_int entre 100 sin que el resultado sea 0
    # si se cumple sabemos que es bisiesto
    if annio_int % 100 != 0:
        print(f"{annio} es Bisiesto")
    # si el resultado es diferente a 0
    else:
        # revisamos si podemos dividir annio_int entre 400 dando como resultado 0
        if annio_int % 400 == 0:
            print(f"{annio} es Bisiesto")
        # si no es posible entonces no sera Bisiesto
        else:
            print(f"{annio} no es Bisiesto")
# si de entrada el resultado no es 0 en la primer division no es bisiesto
else:
    print(f"{annio} no es Bisiesto")