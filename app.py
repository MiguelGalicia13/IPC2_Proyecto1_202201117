from tkinter import Tk
from lista_senales import lista_senales
from lista_datos import lista_datos
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from senal import senal
from dato import dato
def menu():
    global contador
    contador =0
    global root
    print("----------Menu----------")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo Salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar Grafica")
    print("6. inicializar sistema")
    print("7. salir")
    print("------------------------")
    lista_senales_temporal = lista_senales()
    while True:
        opcion=input("Ingrese una opcion: ")
        match opcion:
            case "1":
                print("")
                print("--------------------------------------------------------------")
                print("Cargando archivo")
                route = askopenfilename(filetypes=[("Archivo XML", "*.xml")])
                archivo = open(route, "r")
                archivo.close()
                #Parciar XMML
                tree = ET.parse(route)
                root = tree.getroot()
                print("Archivo cargado con exito")
                print("--------------------------------------------------------------")
                menu()
            case "2":
                print("Procesando archivo")
                print("--------------------------------------------------------------")
                if root is None:
                    print("Primero debes cargar un archivo.")
                    menu()
                else:
                    for senal_temporal in root.findall("senal"):
                        nombre_senal=senal_temporal.get("nombre")
                        tiempo_senal=senal_temporal.get("t")
                        amplitud_senal=senal_temporal.get("A")
                        lista_datos_temporal=lista_datos()
                        lista_patrones_temporal=lista_datos()
                        lista_reducida_temporal=lista_datos()
                        print("Analizando Señales")
                        for dato_senal in senal_temporal.findall("dato"):
                            tiempo_dato = dato_senal.get("t")
                            amplitud_dato = dato_senal.get("A")
                            data_dato = dato_senal.text
                            #? Nueva medicion
                            nuevo = dato(tiempo_dato,amplitud_dato,data_dato)
                            lista_datos_temporal.add_dato(nuevo)
                            if contador == 0:
                                print("Analizando Patrones y creando matriz reducida")
                            if data_dato !="0":
                                nuevo = dato(tiempo_dato,amplitud_dato,1)
                                lista_patrones_temporal.add_dato(nuevo)
                            else:
                                nuevo = dato(tiempo_dato,amplitud_dato,0)
                                lista_patrones_temporal.add_dato(nuevo)
                            contador +=1
                print("--------------------------------------------------------------")
                print("Procesamiento de archivo finalizado")
                print("--------------------------------------------------------------")
                print("")
                menu()
            case "3":
                menu()
            case "4":
                print("")
                print("--------------------------------------------------------------")
                print("                        Datos del Estudiante                 ")
                print("--------------------------------------------------------------")
                print("Miguel Ricardo Galicia Urrutia")
                print("202201117")
                print("Introduccion a la Programacion y Computacion 2 seccion \"A\"")
                print("Ingenieria en Ciencias y Sistemas")
                print("4to Semestre")
                print("")
                menu()
            case "5":
                
                menu()
            case "6":
                menu()
            case "7":
                print("Gracias por usar el programa")
                break
            case _:
                print("Opcion no valida")
                menu()
    

menu()
