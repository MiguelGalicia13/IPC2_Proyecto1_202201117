from nodo_dato import nodo_dato
class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos =0
    def add_dato(self,dato):
        if self.primero is None:
            self.primero = nodo_dato(dato=dato)
            self.contador_datos += 1
            return
        else:
            aux = nodo_dato(dato=dato)
            if self.primero.dato.tiempo > aux.dato.tiempo:
                aux.siguiente = self.primero
                self.primero.anterior = aux
                self.primero = aux
                self.contador_datos += 1
                return
            else:
                actual = self.primero
                while actual.siguiente:
                    if actual.siguiente.dato.tiempo > aux.dato.tiempo:
                        break
                    actual = actual.siguiente
                aux.siguiente = actual.siguiente
                actual.siguiente = aux
                aux.anterior = actual
                if aux.siguiente:
                    aux.siguiente.anterior = aux
                actual.siguiente.anterior = aux
                self.contador_datos += 1
                return
    def recorrer(self):
        print("Total de datos: ",self.contador_datos)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print("Tiempo: ",actual.dato.tiempo," Amplitud: ",actual.dato.amplitud,"Medicion :",actual.dato.data)
            actual = actual.siguiente
        print("=====================================")