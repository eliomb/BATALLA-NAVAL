from random import randrange
from Tablero import Tablero
from Celda import Celda

class Juego:
    def __init__(self):
        self.TuTablero = Tablero()
        self.TableroEnemigo = Tablero()
        self.barcosenemigos = self.TableroEnemigo.barcos_aleatorios()
        if self.barcosenemigos == True:
            print("Barcos enemigos colocados.")
        self.generados = False
        self.barcos_hundidos = 0
        self.lista_barcos_hundidos = []
        self.barcos_hundidos_aliados = 0
        self.ABC = "q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M ! · $ % & / ( ) = ¿ ^ * ¨ Ç _ : ; . , ç ´ + ¡ ' º"
        self.caracteres = self.ABC.split(" ")
        self.bar = False
        self.mal = False
        self.nx = 0
        self.ny = 0
    
        print("Para generar los barcos automaticamente presione 'A'")
        print("Para colocar los barcos individualmente presione 'B'")
        eleccion = input()

        if eleccion == "A":
            self.generados = self.TuTablero.barcos_aleatorios()
            print("Tus barcos fueron generados.")
        elif eleccion == "B":
            print("Elija una posicion")
            for i in range(8):
                self.bar = False
                x = input("Dame un x: ")
                y = input("Dame un y: ")
                while self.bar == False:
                    if x == self.nx and y == self.ny:
                        print("El casillero ya esta ocupado.")
                        x = str(input("Dame un x: "))
                        y = str(input("Dame un y: "))
                        self.bar = False
                    else:
                        self.bar = True
                    if str(x) in self.caracteres or str(y) in self.caracteres:
                        print("Solo puedes escribir numeros.")
                        x = str(input("Dame un x: "))
                        y = str(input("Dame un y: "))
                        self.bar = False
                    else:
                        self.bar = True
                    if int(x) < 0 or int(x) > 7 or int(y) < 0 or int(y) > 8:
                        print("Valores invalidos, las coordenadas son de 0 a 7!!!")
                        x = str(input("Dame un x: "))
                        y = str(input("Dame un y: "))
                        self.bar = False
                    else:
                        self.bar = True
                self.nx = int(x)
                self.ny = int(y)
                self.TuTablero.poner_barcos(int(x), int(y))
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
        while self.barcos_hundidos or self.barcos_hundidos_aliados <= 8:
            if self.generados == True:
                print("Elija coordenadas de disparo: ")
                x_del_barco = int(input("Dame un x: "))
                y_del_barco = int(input("Dame un y: "))
                ataque = self.TableroEnemigo.disparar(x_del_barco, y_del_barco)
                if ataque == True:
                    #self.lista_barcos_hundidos.append((x_del_barco,y_del_barco))
                    print("Hundiste a un barco!")
                    print("----- TERMINA ATAQUE -----")
                    self.barcos_hundidos += 1
                    ataque = None
                else:
                    print("No le diste!")
                    print("----- TERMINA ATAQUE -----")
                    ataque = None
                print("---- El enemigo esta atacando... ---")
                enY = randrange(1,8)
                enX = randrange(1,8)
                ataque2 = self.TuTablero.disparar(enX, enY)
                if ataque2 == True:
                    print("Un barco tuyo fue hundido.")
                    print("---- TERMINA EL ATAQUE ENEMIGO ----")
                    self.barcos_hundidos_aliados += 1
                    ataque2 = None
                else: 
                    print("Tiro al agua.")
                    print("---- TERMINA EL ATAQUE ENEMIGO ----")
                    ataque2 = None
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

