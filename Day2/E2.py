# pedimos de entrada el peso y altura
input_peso = input("Ingresa tu peso\n")
input_altura = input("Ingresa tu altura en mts\n")

# convertimos los valores a tipo number float y los guardamos en nuevas variables
peso = float(input_peso)
altura = float(input_altura)
# se calcula yguarda el resultado de altura al cuadrado
altura_al_cuadrado = altura ** 2

# calculamos el imc
imc = peso / altura_al_cuadrado
# round(numero, numero de decimales) limita el numero de decimales
imc = round(imc, 2)
#convertimos imc a tipo string
imc_str = str(imc)
# imprimimos el resultado
print("tu IMC es: " + imc_str)
