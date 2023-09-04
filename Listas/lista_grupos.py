from nodos.nodo_grupo import nodo_grupo
from Modelos.grupo import grupo
class lista_grupos:
    def __init__(self):
        self.primero = None
        self.contador_grupos =0
    def add_grupo(self, coincidencias,cadena_grupo):
        if self.primero is None:
            self.primero = nodo_grupo(grupo=grupo(coincidencias,cadena_grupo))
            self.contador_grupos += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente = nodo_grupo(grupo=grupo(coincidencias,cadena_grupo))
        self.contador_grupos += 1
    def recorrer(self):
        print("\n Total de grupos: ",self.contador_grupos)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.grupo.el_grupo,"Cadena-grupo: ",actual.grupo.cadena_grupo)
            actual = actual.siguiente
        print("=====================================")
        