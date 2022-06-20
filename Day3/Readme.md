## Condicionales
    - una condicional ejecuta un codigo si se cumple cierta condicion
        la sintaxi seria la siguiente
        ```
            if condicon:
                codigo a ejecutar si se cumple la condicion
            else:
                codigo a ejecutar si no se cumple la condicion
        ```
    
    - podemos agregar mas de una condicion con elif (cuantas elif necesitemos)
        ```
            if condiconA:
                codigo
            elif condiconB:
                codigo
            elif condicionC:
                codigo
            else:
                codigo si ninguna de las anteriore se cumple
        ```
    
### operadores de comparacion
    - < -> menor que
    - <= -> menos o igual que
    - > -> mayor que
    - >= -> mayor o igual a que
    - == -> igual que
    - != -> diferente que

### operadores logicos
    - and -> devuelve true solo si todas las condiciones son verdaderas, o falso si minimo una de las codiciones es falsa
        ```
            if 12 > 10 and 10 < 12:
            print("hola mundo)
        ```
    - or -> devuelve verdadero si por lo menos una condicion es verdadera, o devuelve falso si ninguna de las condiciones es verdadera
        ```
            if 12 > 10 or 12 < 15:
                print("Hola mundo")
        ```
    - not -> invierte el valor Booleano si es False lo convierte en True, si es True lo convierte en False
        ```
            not 5 > 2 # devuelve falso (aunque si es verdad)
        ```
## lower()
    - nos permite anvertir todo un texto en minusculas
        ```
        hola = HolA
        print( hola.lower() ) # imprime -> hola
        ```
## upper()
    - nospermite convertir todo un texto en mayusculas
        ```
        hola = hola
        print( hola.upper() ) # imprime -> HOLA
        ```
## count()
    - devuelve la cantidad de veces que se repite un caracter en una cadena String
        ```
        name = "emmanuel"
        print( name.count("m") ) # imprime -> 2 (es sencible a mayus)
        ```
## escapar carateres
    - podemos escapar caracteres con \ si quremos que se interprete quizas un salto de linea \n o talvez un apostrofe you\'re