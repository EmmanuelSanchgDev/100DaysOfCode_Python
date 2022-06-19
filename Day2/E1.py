# programa que pide dos digitos y devuelve la suma de ellos

# input() pide dos digitos al usuario y los guarda en la variable input_number como tipo string
input_number = input("Escribe dos digitos numericos\n")

# num1 guarda el caracter de la posicion[0] del string
# num1 es psado por la funcion int() que convertira el tipo de dato a number integer
# y lo re-guardara en la variable num1
num1 = input_number[0]
num1 = int( num1 )
# mismo proceso que con num1, pero num2 guarda el caracter de la posicion[1]
num2 = input_number[1]
num2 = int( num2 )
# sumara num1 y num2 (ya ambos son number integer)
suma = num1 + num2
# imprime la suma de los dos digitos
print(suma)
