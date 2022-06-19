print("bienvenido a la calculadora de propinas")
# pide los datos
total = input("cual es el total de tu factura?\n")
personas = input("en cuantas personas deseas dividir tu factura?\n")
propina = input("cuanto deseas dejar de propina? 10, 12 o 15\n")
# convierte los datos a number
propina_int = int(propina)
personas_int = int(personas)
total_float = float(total)
# realiza los calculos para sumar el porcentaje a la factura
total_propina = ( (propina_int / 100) * total_float ) + total_float
# divide la cuenta entre las personas
pago_fracionado = total_propina / personas_int
# limitalos decimales
pago_fracionado = round(pago_fracionado, 2)
# imprime
print( f"el pago por persona es: {pago_fracionado}" )