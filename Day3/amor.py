print("Bienvenid@ a la calculadora del amor")

nombre_el = input("Ingresa el Nombre de El\n")
nombre_ella = input("Ingresa el nombre de Ella\n")

nombre_el_lower = nombre_el.lower()
nombre_ella_lower = nombre_ella.lower()

true = 0
love = 0

true += nombre_el_lower.count("t")
true += nombre_el_lower.count("r")
true += nombre_el_lower.count("u")
true += nombre_el_lower.count("e")
true += nombre_ella_lower.count("t")
true += nombre_ella_lower.count("r")
true += nombre_ella_lower.count("u")
true += nombre_ella_lower.count("e")

love += nombre_el_lower.count("l")
love += nombre_el_lower.count("o")
love += nombre_el_lower.count("v")
love += nombre_el_lower.count("e")
love += nombre_ella_lower.count("l")
love += nombre_ella_lower.count("o")
love += nombre_ella_lower.count("v")
love += nombre_ella_lower.count("e")

score = str(true) + str(love)
score = int(score)

if (score <= 10) or (score >= 90):
    print(f"sus puntos son: {score}, van juntos. como la coca cola y las mentas.")
elif (score >= 40) and (score <= 50):
    print(f"sus puntos son: {score}, estan bien Juntos.")
else:
    print(f"sus puntos son: {score}")