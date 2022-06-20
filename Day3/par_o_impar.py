# programa que nos dice si un numero es par o impar
num = int(input("ingresa un numero\n"))
# usamos el operador de modulo o residuo
resultado = num % 2

# si resultado es 0
if resultado == 0:
    print(f"{num} es un numero par")
# si resultado es cualquier cosa diverente a 0
else:
    print(f"{num} es un numero impar")