from Tablero import Tablero

class Juego:
    def __init__(self, x, y):
        self.unTablero = Tablero()
        self.unTablero.poner_barcos(x, y)


if __name__=="__main__":

    print("\n\n--------------------------")
    print("BATALLA NAVAL")
    print("--------------------------\n")

    jugando = False

    v = input("'Y' para jugar: ")

    if v == "Y" or v == "y":
        x_del_barco = int(input("dame un x"))
        y_del_barco = int(input("dame un y"))
        unJuego = Juego(x_del_barco, y_del_barco)
    else:
        print("No existe esta opcion")



