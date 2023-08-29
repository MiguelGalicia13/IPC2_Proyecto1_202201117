from nodo_dato import nodo_dato
import sys
import os
class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos =0
    def add_dato(self, dato):
        if self.primero is None:
            self.primero = nodo_dato(dato=dato)
            self.contador_datos += 1
            return
        else:
            aux = nodo_dato(dato=dato)
            if self.primero.dato.tiempo > aux.dato.tiempo or (self.primero.dato.tiempo == aux.dato.tiempo and self.primero.dato.amplitud_data > aux.dato.amplitud_data):
                aux.siguiente = self.primero
                self.primero.anterior = aux
                self.primero = aux
                self.contador_datos += 1
                return
            else:
                actual = self.primero
                while actual.siguiente:
                    if actual.siguiente.dato.tiempo > aux.dato.tiempo or (actual.siguiente.dato.tiempo == aux.dato.tiempo and actual.siguiente.dato.amplitud_data > aux.dato.amplitud_data):
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
            print("Tiempo: ",actual.dato.tiempo," Amplitud: ",actual.dato.amplitud_data,"Medicion :",actual.dato.data)
            actual = actual.siguiente
        print("=====================================")
    def delete (self):
        self.primero = None
        self.contador_datos =0
        
    def generar_grafica_original(self,nombre,tiempos_xml,apmplitud_xml):
        print("Generando grafica")
        f =open("bb.dot","w+")
        text ="""
        digraph G{"T="""+tiempos_xml+"""","A="""+apmplitud_xml+""""->" """+nombre+"""" bgcolor="#3990C4" style="filled"
        subgraph cluster_1 {fillcolor="blue:red" style="filled"
        node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
        a0 [ label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas = actual.dato.tiempo
        fila_iniciada = False
        while actual != None:
            if sentinela_de_filas != actual.dato.tiempo:
                print(sentinela_de_filas,actual.dato.tiempo,"hola")
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada = False
                text+="""</TR>\n"""
            if fila_iniciada == False:
                fila_iniciada = True
                text+="""<TR>"""
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.data+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.data+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
            }
            }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o grafoOriginal.png')
        print("terminado")
