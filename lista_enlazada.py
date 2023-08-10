from nodo import nodo
class lista_enlazada:
    def __init__(self):
        self.primero = None
    def add_at_front(self, dato):
        self.primero = nodo(dato=dato, sig=self.primero)
    def add_at_end(self, dato):
        if not self.primero:
            self.primero = nodo(dato=dato)
            return
        actual = self.primero
        while actual.sig:
            actual = actual.sig
        actual.sig = nodo(dato=dato)
    def is_empty(self):
        return self.primero == None
    def delete_node(self,key):
        actual = self.primero
        anterior = None
        while actual and actual.dato != key:
            anterior = actual
            actual = actual.sig
        if anterior is None:
            self.primero = actual.sig
        elif actual:
            anterior.sig = actual.sig
            actual.sig = None
    def get_last_node(self):
        temp = self.primero
        while(temp.sig is not None):
            temp = temp.sig
        return temp.dato
    def print_list(self):
        node = self.primero
        while node != None:
            print(node.dato, end=" => ")
            node = node.sig
    def delete_list(self):
        self.primero = None
