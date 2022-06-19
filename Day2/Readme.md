## Tipos de datos
    - String -> cadenas de texto encerradas entre comillas(simple y dobles respectivamente)
     - Sup-strings -> podemos ectraer caracteres de una cadena de texto, por su posicion con [] colocando la posicion que deceamos contando desde 0 ``` str_index = "hola"[3] ``` nos devolvera 'a'
    - Number -> literalmente son numeros (enteros o flotantes)
    =Boolean -> es un tipo logico que solo tiene True o False (verdadero o falso)

    -podemos comprovar el tipo de dato que tiene una variable con la funcion
     ``` type(variable) ```

## Convirtiendo tipos de datos
    - podemos comvertir un tipo de dato en otro por ejemplo [number -> string]
        - ``` new_string = str(variable) ``` covierte la variable en un tipo string
        - ``` new_numbre_integer = int(variable) ``` covierte la variable a un tipo entero(numero sin decimales)
        - ``` new_number_float = float(variable) ``` covierte la variable a un tipo flotante(numero con decimales)
        - ```  ```

## operaciones matematicas
    - suma ``` 5 + 6 ```
    - resta ``` 5 - 6 ```
    - multiplicacion ``` 5 * 6 ```
    - division ``` 5 / 6 ``` la divicion devuelve un tipo float aunque sea numero entero
        - // si por algun motivo no deceamos los decimales de una divion podemos usar este operador y en el resultado omitira los decimales dandonos un tipo int
    - exponenciar ``` 2 ** 2  ```
        - las operaciones matematicas respetan el orden de precedencia
    - round() -> esta funcion nos permite limitar la cantidad de decimales que tendra un numero flotante colocando el numero(o variable) y colocando la cantidad de decimales que queremos separandolas por una ',' ejem: ``` round(1.123456, 2) ```, si no colocamos una cantidad de decimales lo redondeara
        ``` 
            num_float = 12.12345645912
            print( num_float ) # imprime 12.12345645912
            print( round(num_float, 2) ) # imprime 12.12
            print( round(num_float) ) # imprime 12
         ```
    - += es lo mismo a  ``` num1 = num1 + num1```
    - -= es lo mismo a  ``` num1 = num1 - num1```
    - *= es lo mismo a  ``` num1 = num1 * num1```
    - /= es lo mismo a  ``` num1 = num1 / num1```

## f-string (cadena f)
    - podemos concatenar en un print() convierte nuestras variables en string automatocamente
      ```
        print(f"Hola {name}")
      ```