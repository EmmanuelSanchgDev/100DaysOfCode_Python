input_edad = input("cual es tu edad?\n")

edad_int = int(input_edad)

dias = 365
semanas = 52
meses = 12
annios = 90

dias_restantes = (dias * annios) - (dias * edad_int)
semanas_restantes = (semanas * annios) - (semanas * edad_int)
meses_restantes = (meses * annios) - (meses * edad_int)
annios_restantes = annios - edad_int

mensaje = f"tequedan {dias_restantes} dias, {semanas_restantes} semanas, {meses_restantes} meses, {annios_restantes} años restantes"

print( mensaje )