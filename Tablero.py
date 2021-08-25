from Celda import Celda
from random import randrange
import random

class Tablero:
    
    

    def __init__(self):
        self.tamanio = 8
        self.celdas = [[0]*self.tamanio]*self.tamanio
        self.crear_celdas()
    
    def crear_celdas(self):
        for num_fila in range(self.tamanio):
            for num_columna in range(self.tamanio):
                celda = Celda()
                self.celdas[num_fila][num_columna] = celda

        for i in range(self.tamanio):
            print(self.celdas[i])
        #pr

    
    def disparar(self, x, y):
        print("----- EMPIEZA ATAQUE -----")
        resultado = self.celdas[x][y].ser_atacado()
        return resultado
    
    def poner_barcos(self, x, y):
        #barco = self.celdas[x][y].barco_agregado()
        self.celdas[x][y].ocupado = True
        print(self.celdas[x][y].ocupado)



    def limpiar_tablero(self):
        for num_fila in range(self.tamanio):
            for num_columna in range(self.tamanio):
                self.borrar_barcos(num_fila, num_columna)

    def borrar_barcos(self, x, y):
        if self.celdas[x][y] == Celda():
            barco = self.celdas[x][y].remover_barcos()
        else: 
            print("********** ERROR! Aqui no hay una celda. **********")
        
    def barcos_aleatorios(self):
        generados = False
        numX = None
        numY = None

        print("Colocando OCHO barcos...")
        for i in range(1, 8):
            randX = randrange(1, self.tamanio)
            randY = randrange(1, self.tamanio)
            if numY == randY or numX == randX:
                randX = randrange(1, self.tamanio)
                randY = randrange(1, self.tamanio)
            numX = randX
            numY = randY
            print("x: ", randX," y: ", randY)
            self.poner_barcos(randX, randY)
            
        if generados != True:
            generados = True
            return generados
        else:
            return