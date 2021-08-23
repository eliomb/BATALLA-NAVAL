from Barco import Barco

class Celda:
    def __init__(self):
        self.barco = Barco()
        self.atacada = None
        self.ocupado = None

    def ser_atacado(self):
        #print("Posicion atacada!")
        print("ANTES ", self.ocupado)
        if self.ocupado == True:
            self.ocupado = False
            print("DESPUES ", self.ocupado)
            return True

    def barco_agregado(self):
        self.ocupado = True
        #print("Se coloco un barco")
    
    def remover_barco(self):
        self.ocupado = False
        