from Barco import Barco

class Celda:
    def __init__(self):
        self.barco = Barco()
        self.atacada = False
        self.ocupado = False

    def ser_atacado(self):
        #print("Posicion atacada!")
        if self.ocupado == True:
            self.ocupado = False
            self.atacada = True
            return True
        else:
            return False

    def barco_agregado(self):
        self.ocupado = True
        print("Se coloco un barco")
    
    def remover_barco(self):
        self.ocupado = False
        print("Se borro un barco")