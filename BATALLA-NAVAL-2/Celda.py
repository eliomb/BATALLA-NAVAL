from Barco import Barco

class Celda:
    def __init__(self):
        self.barco = Barco()
        self.atacada = False
        self.ocupado = False

    def ser_atacado(self):
        #print("Posicion atacada!")
        print("ANTES ", self.ocupado)
        if self.ocupado == True:
            self.ocupado = False
            self.atacada = True
            print("DESPUES ", self.ocupado)
            return True
        else:
            return False

    def barco_agregado(self):
        self.ocupado = True
        print("Se coloco un barco")
    
    def remover_barco(self):
        self.ocupado = False
        