from Tablero import Tablero

class Juego:
    def __init__(self):
        self.unTablero = Tablero()
        self.generados = self.unTablero.barcos_aleatorios()
        self.barcos_hundidos = 0

        while self.barcos_hundidos <= 8:
            if self.generados == True:
                print("Elija coordenadas de disparo: ")
                x_del_barco = int(input("Dame un x: "))
                y_del_barco = int(input("Dame un y: "))
                ataque = self.unTablero.disparar(x_del_barco, y_del_barco)
                print("*****ATAQUE****** ", ataque)
                if ataque == True:
                    print("Hundiste a un barco!")
                    print("----- TERMINA ATAQUE -----")
                    self.barcos_hundidos += 1
                    ataque = None
                else:
                    print("le pifeaste")
                    print("----- TERMINA ATAQUE -----")
                    ataque = None
            else:
                print("ERROR: Los barcos no se generaron")
        
        if self.barcos_hundidos == 8:
            print("Todos los barcos enemigos fueron hundidos. Ganaste!")


if __name__=="__main__":

    print("\n\n--------------------------")
    print("BATALLA NAVAL")
    print("--------------------------\n")

    jugando = False

    v = input("'Y' para jugar: ")

    if v == "Y" or v == "y":
        print("Generando 8 barcos en el tablero enemigo...")
        unJuego = Juego()
        #x_del_barco = int(input("Dame un x: "))
        #y_del_barco = int(input("Dame un y: "))
        #unJuego = Juego(x_del_barco, y_del_barco)
    else:
        print("No existe esta opcion")



