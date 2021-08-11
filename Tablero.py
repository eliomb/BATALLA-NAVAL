class Tablero:
    
    def __init__(self):
        self.tamanio = 8
        self.celdas = []
        self.crear_celdas()
    
    def crear_celdas(self):
        for num_fila in range(self.tamanio):
            for num_columna in range(self.tamanio):
                unaCelda = Celda()
                self.celdas.append(unaCelda)
    
    def disparar(self, x, y):
        resultado = self.celdas[x][y].ser_atacado()
        return resultado
    
    def poner_barcos(self):
        barco = self.celdas[x][y].barco_agregado()
        