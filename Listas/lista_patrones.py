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
    def recorrer_patron(self):
        print("Total de patrones: ",self.contador_patrones)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print("Tiempo: ",actual.patron.tiempo," Cadena Patron: ",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("=====================================")
    def eliminar(self,tiempo):
        actual = self.primero
        anterior = None
        while actual and actual.patron.tiempo != tiempo:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
    def encontar_coincidencias(self):
        print("\n =====================================")
        print("\nBuscando coincidencias")
        while self.primero:
            actual = self.primero
            temporal_str=""
            temp_tiempo=""
            while actual:
                if actual.patron.cadena_patron==self.primero.patron.cadena_patron:
                    temp_tiempo+=str(actual.patron.tiempo)+","
                actual = actual.siguiente
            buffer=""
            for digito in temp_tiempo:
                if digito.isdigit():
                    buffer+=digito
                else:
                    if buffer!="":
                        self.eliminar(int(buffer))
                    else:
                        buffer=""
                        
            resultado +=temp_tiempo+"--"
        return resultado