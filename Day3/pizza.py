menu = "#1-pizza pequeña: $15\n#2-piza Mediana: $20\n#3-pizza Grande: $25"

print("Bienvenido a Pizza Python!!")
eleccion = input(f"que vas a pedir?[1,2 o 3]\n{menu}\n")

pizza = ""
precio = 0
ingredientes = ""
peperoni_extra_small = 2
peperoni_extra_medium_large = 3
queso_extra = 1
question_1 = "n"
question_2 = "n"
question_3 = "n"

if eleccion == "1":
    pizza = "pizza pequeña"
    precio = 15
    question_1 = input("deseas peperoni extra [y/n]")
    if question_1 == "y":
        precio += peperoni_extra_small
        ingredientes = " peperoni extra, "
elif eleccion == "2": 
    pizza = "pizza Mediana"
    precio = 20
    question_2 = input("deseas peperoni extra [y/n]")
elif eleccion == "3": 
    pizza = "pizza Grande"
    precio = 25
    question_2 = input("deseas peperoni extra [y/n]")

if question_2 == "y":
    precio += peperoni_extra_medium_large
    ingredientes += "peperoni extra, "

question_3 = input("deseas queso extra [y/n]")
if question_3 == "y":
    precio += queso_extra
    ingredientes += "queso extra, "

print(f"tu orden es una {pizza} con {ingredientes}el precio total seran ${precio}")