import os
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
        if self.primero is None:
            print("=====================================")
            print("Lista de grupos vacia")
            print("=====================================")
            return
        print("\n Total de grupos: ",self.contador_grupos)
        print("=====================================")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.grupo.el_grupo,"Cadena-grupo: ",actual.grupo.cadena_grupo)
            actual = actual.siguiente
        print("=====================================")
    def delete(self):
        self.primero = None
        self.contador_grupos =0
    def devolver_grupo(self):
        actual = self.primero
        buffer=""
        while actual != None:
            buffer+=str(actual.grupo.el_grupo)
            actual = actual.siguiente
        return buffer
    def generar_grafica_original(self):
        if self.primero is None:
            print("=====================================")
            print("Lista de grupos vacia")
            print("=====================================")
            return
        print("Generando grafica")
        f =open("aa.dot","w+")
        text ="""
        digraph G{"Grupos="""+str(self.contador_grupos)+""""->" """+"Matriz Reducida"+"""" bgcolor="#3990C4" style="filled"
        subgraph cluster_1 {fillcolor="blue:red" style="filled"
        node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
        a0 [ label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas = actual.grupo.el_grupo
        fila_iniciada = False
        while actual != None:
            if sentinela_de_filas != actual.grupo.el_grupo:
                sentinela_de_filas=actual.grupo.el_grupo
                fila_iniciada = False
                text+="""</TR>\n"""
            if fila_iniciada == False:
                fila_iniciada = True
                text+="""<TR>"""
                text+="""<TD border="3"  bgcolor="green" gradientangle="315">"""+"Grupo: "+str(actual.grupo.el_grupo)+"""</TD>\n"""
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.grupo.cadena_grupo)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.grupo.cadena_grupo)+"""</TD>\n"""
            actual = actual.siguiente
        text+="""</TR></TABLE>>];
            }
            }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng aa.dot -o matrizReducida.png')
        print("terminado")