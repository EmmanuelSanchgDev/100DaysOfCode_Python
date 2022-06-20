print("Bienvenido a la clinica Imss")
# pedimos los datos y los convertimos a tipo number
altura = input("Ingresa tu altura en mts")
altura_float = float(altura)
peso = input("Ingresa tu peso en kg")
peso_int = int(peso)

# se realiza el calculo que es peso / altura al cuadrado 
# pow() nos ayuda a exponenciar nuestra altura pow(valor, exponente)
result_imc = peso_int / pow(altura_float, 2)
# se limitan los decimales
result_imc = round(result_imc, 2)

# y solo imprime segun sea el caso del paciente
if result_imc > 35:
    print(f"tu imc es: {result_imc}, deverias cuidarte. eres clinicamente Obeso")
elif result_imc > 30:
    print(f"tu imc es: {result_imc}, bajale a lkas chimichangas. eres Obeso")
elif result_imc > 25:
    print(f"tu imc es: {result_imc}, bamos a correr!. tienes un ligero Sobrepeso")
elif result_imc > 18.5:
    print(f"tu imc es: {result_imc}, wow!. estas en tu peso ideal!!")
else:
    print(f"tu imc es: {result_imc}, ok hablemos. estas comiendo muy poco, por favor alimentate mejor")

