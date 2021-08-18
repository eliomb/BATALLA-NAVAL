from Celda import Celda
import random

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
    
    def poner_barcos(self, x, y):
        barco = self.celdas[x][y].barco_agregado()

    def limpiar_tablero(self):
        for num_fila in range(self.tamanio):
            for num_columna in range(self.tamanio):
                self.borrar_barcos

    def borrar_barcos(self, x, y):
        barco = self.celdas[x][y].remover_barcos()
        