## ordem
from Estruturas import *
from time import sleep

class Ordem:
    def Comum_pref(fila_x,fila_y):
        tam = fila_y.size() + fila_x.size()

        for c in range(tam):
            if fila_y.size() >= 2:
                print(fila_y.remove())
                sleep(0.5)
                print(fila_y.remove())
                sleep(0.5)
            elif fila_y.size() == 1:
                print(fila_y.remove())  
                sleep(0.5)
            if fila_x.isEmpty() == True:
                return 0
            else:
                print(fila_x.remove())
                sleep(0.5)
            if fila_x.isEmpty() == True:
                for i in range(fila_y.size()):
                    print(fila_y.remove())
                    sleep(0.5)
            if fila_y.isEmpty() == True:
                for i in range(fila_y.size()):
                    print(fila_y.remove())
                    sleep(0.5)

    def emergencia(lista,pilha):
        for c in sorted(lista):
            pilha.push(c)
        while pilha.isEmpty() == False:
            print(pilha.pop())
            sleep(0.5)


