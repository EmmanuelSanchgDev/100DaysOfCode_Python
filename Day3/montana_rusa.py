# pide la altura y la convierte a integer
altura = input("Cual es tu altura? en cm\n")
altura_int = int(altura)

# condiciona si puede o no subir a la montaña rusa segun su estatura
if altura_int >= 120:
    # si es acto le pedira la edad y la convertira en integer para calcular el costo del ticket
    edad = input("cual es tu edad?\n")
    edad_int = int(edad)

    # si es mayor de 18 pagara $12
    if edad_int > 18:
        print("son $12 pesos para subir a la montaña rusa")
    # si es mayor de 12 y menor de 18 pagara $7
    elif edad_int >= 12:
        print("son $7 pesos para subir a la montaña rusa")
    # si es menor o igual de 18 pagara $7
    elif edad_int < 12:
        print("son $5 pesos para subir a la montaña rusa")
else:
    print("lo siento, eres muy chico para subir a la montaña rusa")