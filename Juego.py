from Tablero import Tablero
from Celda import Celda

class Juego:
    def __init__(self):
        self.TuTablero = Tablero()
        self.TableroEnemigo = Tablero()
        self.barcosenemigos = self.TableroEnemigo.barcos_aleatorios()
        self.generados = False
        self.barcos_hundidos = 0
        self.lista_barcos_hundidos = []
        self.bar = False
    
        print("Para generar los barcos automaticamente presione 'A'")
        print("Para colocar los barcos individualmente presione 'B'")
        eleccion = input()

        if eleccion == "A":
            self.generados = self.TuTablero.barcos_aleatorios()
        elif eleccion == "B":
            print("Elija una posicion")
            for i in range(8):
                x = int(input("Dame un x: "))
                y = int(input("Dame un y: "))
                while self.bar == False:
                    if self.TuTablero.celdaocupada(x, y) == True:
                        print("El casillero ya esta ocupado.")
                        x = int(input("Dame un x: "))
                        y = int(input("Dame un y: "))
                        self.bar = False
                    if x < 0 or x > 8 or y < 0 or y > 8:
                        print("Valores invalidos, las coordenadas son de 8x8!!!")
                        x = int(input("Dame un x: "))
                        y = int(input("Dame un y: "))
                        self.bar = False
                    else:
                        self.bar = True
                    
                self.TuTablero.poner_barcos(x, y)
                print(i)
            
            self.generados = True

        
        print("Para atacar al tablero enemigo presione R: ")
        print("Para limpiar el tablero y reiniciar el juego presione T:")
        eleccion2 = input()

        if eleccion2 == "R":
            self.ataque()
        elif eleccion2 == "T":
            self.TuTablero.limpiar_tablero
            print("Reiniciando..")
            self.__init__()



    def ataque(self):
        while self.barcos_hundidos <= 8:
            if self.generados == True:
                print("Elija coordenadas de disparo: ")
                x_del_barco = int(input("Dame un x: "))
                y_del_barco = int(input("Dame un y: "))
                ataque = self.TableroEnemigo.disparar(x_del_barco, y_del_barco)
                if ataque == True:
                    self.lista_barcos_hundidos.append((x_del_barco,y_del_barco))
                    print("Hundiste a un barco!")
                    print("----- TERMINA ATAQUE -----")
                    self.barcos_hundidos += 1
                    ataque = None
                else:
                    print("No le diste!")
                    print("----- TERMINA ATAQUE -----")
                    ataque = None
            else:
                print("ERROR: Los barcos no se generaron")
            if self.barcos_hundidos == 8:
                print("Todos los barcos enemigos fueron hundidos. Ganaste!")
                break
            print(self.barcos_hundidos)
           


if __name__=="__main__":

    print("\n\n--------------------------")
    print("BATALLA NAVAL")
    print("--------------------------\n")

    jugando = False

    #v = input("'Y' para jugar: ")

    # if v == "Y" or v == "y":
    #     print("Generando 8 barcos en el tablero enemigo...")
    unJuego = Juego()
    #     #x_del_barco = int(input("Dame un x: "))
    #     #y_del_barco = int(input("Dame un y: "))
    #     #unJuego = Juego(x_del_barco, y_del_barco)
    # else:
    #     print("No existe esta opcion")

