print("Bienvenid@ a la montaña rusa mas genial!")
altura = input("por favor ingresa tu altura en mts\n")
altura_int = int(altura)
ticket = 0

if altura_int >= 120:
    edad = input("Genial tiene las altura exacta para subir a la montaña\nDime cual es tu edad?\n")
    edad_int = int(edad)

    if edad_int > 18:
        ticket += 12
        print(f"por la edad de {edad_int} años, el costo de tu Boleto sera de ${ticket} pesos")
    elif edad_int > 12:
        ticket += 7
        print(f"por la edad de {edad_int} años, el costo de tu Boleto sera de ${ticket} pesos")
    elif edad_int < 12:
        ticket += 5
        print(f"por la edad de {edad_int} años, el costo de tu Boleto sera de ${ticket} pesos")
    elif edad_int >= 45 and edad_int <= 55:
        print(f"todo estara bien tranquilo puedes pasar Gratis")

    quiere_photo = input("Deseas una fotografia con tu boleto? [Y/N]\n")
    if quiere_photo == "Y":
        ticket += 3
    
else:
    print("lo lamento, pero eres muy chico para subir a la montaña, suerte el proximo año")

print(f"de acuerdo el precio total de tu Boletos es de ${ticket} pesos")