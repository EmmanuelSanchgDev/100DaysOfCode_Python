print("Bienvenid@ a elige tu Aventura\ntu mision es encontrar el tesoro")
paso1 = input("te encuentras a corralad@ y solo puedes ir a la izquierda o derecha\nque eliges? Iquierda o Derecha")
paso1_l = paso1.lower()

if (paso1_l == "d") or (paso1_l == "derecha"):
    print("te a alcanzado una fleta, estas Muert@")
elif (paso1_l == "i") or (paso1_l == "izquierda"):
    print("Haz logrado escapar hasta la orill de una isla, pero debes llegar a la isla vecina")
    paso2 = input("te atreves a crusar el mar Nadando o esperar un Barco?")
    paso2_l = paso2.lower()

    if (paso2_l == "n") or (paso2_l == "nadando"):
        print("una familia de tiburones te agradece tu donativo, estas Muert@")
    elif (paso2_l == "b") or (paso2_l == "barco"):
        print("lograste llegar a isla vecina sano y salvo")
        paso3 = input("buscando en la isla te haz encontrado con tres puertas Roja, Azul y Amarrilla\nCual eliges?")
        paso3_l = paso3.lower() 

        if (paso3_l == "r" or paso3_l == "roja") or (paso3_l == "a" or paso3_l == "azul"):
            print("la puerta que elegiste estaba llena de fuego, serpientes y una creatura extraña\nEstas Muert@")
        else:
            print("Felicidades haz encontrado el tesoro!!,\nahora solo debes averiguar como salir de esta isla...")
