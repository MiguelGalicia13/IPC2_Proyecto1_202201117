from nodos.nodo_grupo import nodo_grupo
class lista_grupos:
    def __init__(self):
        self.primero = None
        self.contador_grupos =0
    def add_grupo(self, grupo):
        if self.primero is None:
            self.primero = nodo_grupo(grupo=grupo)
            self.contador_grupos += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual.siguiente
        actual.siguiente = nodo_grupo(grupo=grupo)
        self.contador_grupos += 1
    def recorrer_e_imprimir(self):
        print("Total de grupos: ",self.contador_grupos)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print("Grupo: ",actual.grupo.el_grupo," Cadena grupo: ",actual.grupo.cadena_grupo)
            actual = actual.siguiente
        print("=====================================")