from Celda import Celda
from random import randrange
import random

class Tablero:
    
    

    def __init__(self):
        self.tamanio = 8
        self.celdas = [[]]
        self.crear_celdas()
    
    def crear_celdas(self):
        for num_fila in range(1, self.tamanio + 1):
            for num_columna in range(self.tamanio):
                celda = Celda()
                self.celdas[num_fila].append(celda)
    
    def disparar(self, x, y):
        resultado = self.celdas[x][y].ser_atacado()
        return resultado
    
    def poner_barcos(self, x, y):
        print("voy a poner un barco, estoy en tablero")
        print(self.celdas)
        barco = self.celdas[x][y].barco_agregado()
        return barco

    def limpiar_tablero(self):
        for num_fila in range(self.tamanio):
            for num_columna in range(self.tamanio):
                self.borrar_barcos

    def borrar_barcos(self, x, y):
        barco = self.celdas[x][y].remover_barcos()
        
    def barcos_aleatorios(self):
        randX = randrange(self.tamanio)
        randY = randrange(self.tamanio)
        for i in range(8):
            self.celdas[randX][randY].barco_agregado()