from Celda import Celda
from random import randrange
import random

class Tablero:
    
    

    def __init__(self):
        self.tamanio = 8
        self.celdas = []
        self.crear_celdas()
        self.lista_barcos = []

    
    def crear_celdas(self):
        for num_fila in range(self.tamanio):
            self.celdas.append([])
            for num_columna in range(self.tamanio):
                self.celdas[num_fila].append(Celda())


        #for i in range(1,8):
            #print(self.celdas[i])
        #pr

    
    def disparar(self, x, y):
        print("----- EMPIEZA ATAQUE -----")
        resultado = self.celdas[x][y].ser_atacado()
        return resultado
    
    def poner_barcos(self, x, y):
        barco = self.celdas[x][y].barco_agregado()
#        print("x:%i,y:%i:"%(x,y))
#        print(self.celdas[x][y].ocupado)

    def celdaocupada(self, x, y):
        celda = self.celdas[x][y].ocupado
        if celda == True:
            return celda
        else:
            return False

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


        #print("Colocando OCHO barcos...")
        contador = 0
        while contador <= 7:
            randX = randrange(self.tamanio)
            randY = randrange(self.tamanio)

            if (randX, randY) in self.lista_barcos:
                continue
            
            self.poner_barcos(randX, randY)
            self.lista_barcos.append((randX,randY))
            contador+=1
            #print("x: ", randX," y: ", randY)
            
        for indexfila,fila in enumerate(self.celdas):
            for indexcelda,celda in enumerate(fila):
                if celda.ocupado:
                    print('Barco en:',indexfila, indexcelda)

        if generados != True:
            generados = True
            return generados
