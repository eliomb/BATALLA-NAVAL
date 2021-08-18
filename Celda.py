class Celda:
    def __init__(self):
        self.barco = None
        self.atacada = False
    
    def ser_atacado(self):
        if self.barco != None:
            return True
        return False

    def barco_agregado(self):
        self.barco = True
    
    def remover_barco(self):
        self.barco = False
        