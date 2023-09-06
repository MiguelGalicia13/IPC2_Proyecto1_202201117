from nodos.nodo_senal import nodo_senal
import sys
import os
from Modelos.grupo import grupo
import xml.etree.ElementTree as ET
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
        actual = self.primero
        if actual is None:
            print("=====================================")
            print("Lista de señales vacia")
            print("=====================================")
            return
        print("Nombre: ",actual.senal.nombre)
        print("Total de senales: ",self.contador_senales)
        print("=====================================")
        while actual != None:
            print("Tiempo: ",actual.senal.tiempo," Amplitud: ",actual.senal.amplitud," Nombre: ",actual.senal.nombre)
            actual.senal.lista_datos.recorrer()
            print("Patrones de senal: ")
            actual.senal.lista_patrones.recorrer()
            actual = actual.siguiente
        print("=====================================") 
    def delete_senal(self):
        actual = self.primero
        actual.senal.lista_datos.delete()
        self.primero = None
        self.contador_senales =0
        
    def calcular_patrones(self,nombre):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre:
                actual.senal.lista_patrones_nivel=actual.senal.lista_patrones.devolver_patrones(actual.senal.lista_patrones_nivel)
                actual.senal.lista_patrones_nivel.recorrer_patron()
                lista_patrones_temporal=actual.senal.lista_patrones_nivel
                grupos_sin_analizar=lista_patrones_temporal.encontar_coincidencias()
                print("Coincidencias: \n",grupos_sin_analizar)
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito=="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_datos.devolver_cadena_grupo(buffer)
                        actual.senal.lista_grupos.add_grupo(buffer,cadena_grupo)
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer()
            actual=actual.siguiente

    def escribir_archivo(self):
        print("=====================================")
        actual = self.primero
        grupos_usados=""
        contador_grupos=1
        print("Generando archivo")
        mis_senales = ET.Element("senalesRducidas") 
        lista_senales = ET.SubElement(mis_senales, "listaSenales", nombre="Lista de senales", A=actual.senal.amplitud)
        while actual != None:
            grupo = ET.SubElement(lista_senales, "grupo ",g=contador_grupos)
            tiempo=ET.SubElement(grupo,"tiempo")
            tiempo.text=actual.senal.lista_grupos.devolver_grupo()
            buffer1=""
            for grupo in tiempo.text:
                if grupo.isdigit() or grupo==",":
                    buffer1+=grupo+","
                elif grupo=="-" and buffer1!="":
                    cadenas=actual.senal.lista_datos.devolver_cadena_grupo(buffer1)
                    grupos_usados+=buffer1
                    buffer1=""
                else:
                    buffer1=""
                    
            actual_lista_patrones = actual.senal.lista_patrones.primero
            lista_patrones=ET.SubElement(tiempo,"listaPatrones")
            while actual_lista_patrones != None:
                patron = ET.SubElement(lista_patrones, "patron")
                buffer=""
                print(grupos_usados)
                """patrones_temporal=actual.senal.lista_datos.devolver_cadena_grupo(grupos_usados)
                for pat in patrones_temporal:
                    if pat.isdigit() or pat==",":
                        buffer+=pat+","
                    elif pat=="-" and buffer!="":
                        ET.SubElement(patron,"tiempo").text=buffer
                    else:
                        buffer=""
                        """
                actual_lista_patrones = actual_lista_patrones.siguiente
                
            actual = actual.siguiente
        my_data=ET.tostring(mis_senales)
        my_data=str(my_data)
        self.xml_arreglado(mis_senales)
        arbol_xml=ET.ElementTree(mis_senales)
        arbol_xml.write("./IPC2_Proyecto1_202201117/Reportes/salida.xml",encoding="UTF-8",xml_declaration=True)
        
    def xml_arreglado(self, element, indent='  '):
        # Inicializar una cola con el elemento raíz y nivel de anidación 0
        queue = [(0, element)]  # (level, element)
        # Bucle principal: continúa mientras haya elementos en la cola
        while queue:
        # Extraer nivel y elemento actual de la cola
            level, element = queue.pop(0)
            # Crear tuplas para cada hijo con nivel incrementado
            children = [(level + 1, child) for child in list(element)]
            # Agregar saltos de línea e indentación al inicio del elemento actual
            if children:
                element.text = '\n' + indent * (level + 1)
                # Agregar saltos de línea e indentación al final del elemento actual
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                # Si este es el último elemento del nivel actual, reducir la indentación
                element.tail = '\n' + indent * (level - 1)
            # Insertar las tuplas de hijos al principio de la cola
            queue[0:0] = children
        