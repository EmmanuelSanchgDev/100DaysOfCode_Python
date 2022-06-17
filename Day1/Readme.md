# Dia 1

- impresion -> se utiliza la funcion -print()-, agregando dentro de los parentecis lo que queremos imprimir, Pero esto que vamos a imprimir si es una cadena de texto(cualquier cosa que sean palabras escritas), debe ir encerrado por comillas("") pueden ser comillas simples('') o comillas dobles(""), pero siendo pares del mismo tipo(si comenzamos con ' debe terminar con ') [```print("Hola Mundo!")```](./print.py)

- depuracion -> la depuracion es arreglar codigo que no funciona, los errores pasaran, Siempre. y python nos dara pistas de donde esta el error, pero si por alguna rason no encontramos el error. siempre tenemos a Google que nos ayudara, solo debemos pegar el mensaje del error y buscar entre los resultados

- entrada -> se utiliza la funcion -input()-, agregando dentro de los parentecis una pista al usuario de lo que esperamos que ingrese, de nueva cuenta al ser una cadena de texto debe ir encerrada por comillas("") [```input("cual es tu nombre?")```](./input.py)

- comentarios -> podemos agregar comentarios a nuestro codigo con el simbolo # ```# esto es un comentario```, todo lo que este como comentario sera ignorado por lo que no afecta la ejecucion

- tambien podemos anidar funciones ```print("Hola " + input("Como te llamas?"))``` elresultado seria 1ro pregunta el nombre y despues lo saluda usando el nombre. [```# Hola emmanuel```](./anidando.py)

- manipulacion de cadenas -> funcion -len()-, la funcion len devuelve la longitud(cantidad de caracteres) de un string como un valor numerico ```print(len("jesus"))``` como resultado seria [```#5```](./len.py)

- variables -> una variable es una "caja" en la que podemos guardar valores, por ejemplo un input(), cuando pedimos una entrada se recibe pero no se puede acceder despues a ella, para ellos estan las variables en donde podemos almacenar el dato y usarlo mas adelante ```nombre = input("cual es tu nombre?")``` de este modo cuando necesite el nombre solo debo llamar la variable "nombre" ```print("Hola" + nombre)```, para guardar un valor en la variable se usa el operador '=' en medio de el nomrbe de variable y el valor [(nombre = valor)](./variables.py)

- una linea una accion -> en los ejemplos anteriores anidamos funciones y puede ser confuso entenderlo por ello podemos usar las variables para que cada linea realice una accion y sea mas facil de entender lo que esta pasando [```code```](./una_accion.py)

- Nombrar identificadores -> una buena practica al momento de darle nombre a nuestras variables es ser bastante descriptivo en lugar de colocar un "n = 'pedro'" mejor "nameUser = 'pedro'", un nombre de variable no puede tener espacios en blanco en su lugar usamos '_' "last_name_user = 'sanchez'" - otra cosa python diferencia entre mayusculas y minusculas

### [Projecto 1](./project1.py) | generador de nombres de bandas
te pide el nombre de tu ciudad y de tu mascota y las unde para formar un nombre para tu banda




los espacios(indentacion) en Python son muy importantes