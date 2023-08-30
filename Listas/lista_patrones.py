from nodos.nodo_patron import nodo_patron
class lista_patrones:
    def __init__(self):
        self.primero = None
        self.contador_patrones =0
    def add_patron(self, patron):
        if self.primero is None:
            self.primero = nodo_patron(patron=patron)
            self.contador_patrones += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual.siguiente
        actual.siguiente = nodo_patron(patron=patron)
        self.contador_patrones += 1
    def recorrer_e_imprimir(self):
        print("Total de patrones: ",self.contador_patrones)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print("Tiempo: ",actual.patron.tiempo," Cadena Patron: ",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("=====================================")