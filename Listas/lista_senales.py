from nodos.nodo_senal import nodo_senal
import sys
import os
class lista_senales:
    def __init__(self):
        self.primero = None
        self.contador_senales =0
    def add_senal(self,senal):
        if self.primero is None:
            self.primero = nodo_senal(senal=senal)
            self.contador_senales += 1
            return
        else:
            aux = nodo_senal(senal=senal)
            if self.primero.senal.tiempo > aux.senal.tiempo:
                aux.siguiente = self.primero
                self.primero.anterior = aux
                self.primero = aux
                self.contador_senales += 1
                return
            else:
                actual = self.primero
                while actual.siguiente:
                    if actual.siguiente.senal.tiempo > aux.senal.tiempo:
                        break
                    actual = actual.siguiente
                aux.siguiente = actual.siguiente
                actual.siguiente = aux
                aux.anterior = actual
                if aux.siguiente:
                    aux.siguiente.anterior = aux
                actual.siguiente.anterior = aux
                self.contador_senales += 1
                return
    def recorrer(self):
        print("Total de senales: ",self.contador_senales)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print("Tiempo: ",actual.senal.tiempo," Amplitud: ",actual.senal.amplitud," Nombre: ",actual.senal.nombre)
            actual.senal.lista_datos.recorrer()
            print("Patrones de senal: ")
            actual.senal.lista_patrones.recorrer()
            actual = actual.siguiente
        print("=====================================") 
    def calcular_patrones(self,nombre):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre:
                actual.senal.lista_patrones_nivel=actual.senal.lista_patrones.devolver_patrones(actual.senal.lista_patrones_nivel)
                actual.senal.lista_patrones_nivel.recorrer_patron()
                lista_patrones_temporal=actual.senal.lista_patrones_nivel
                grupos_sin_analizar=lista_patrones_temporal.encontar_coincidencias()
                print(grupos_sin_analizar)
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito=="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_datos.devolver_cadena_grupo(buffer)
                        actual.senal.lista_grupos.add_grupo(cadena_grupo)
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer()
                return
            actual=actual.siguiente
            