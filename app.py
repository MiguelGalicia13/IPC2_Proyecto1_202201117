from tkinter import Tk
from Listas.lista_senales import lista_senales
from Listas.lista_datos import lista_datos
from Listas.lista_patrones import lista_patrones
from Listas.lista_grupos import lista_grupos
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from Modelos.senal import senal
from Modelos.dato import dato
lista_datos_temporal=lista_datos()
lista_binaria_temporal=lista_datos()
lista_senales_temporal = lista_senales()
lista_patrones_temporal=lista_patrones()
lista_grupos_temporal=lista_grupos()
archivo = None
contador = 0
route = None
root = None
nombre_senal = None
tiempo_senal = None
amplitud_senal = None
def menu():
    global route
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
    print("------------------------ \n")
    while True:
        opcion=input("Ingrese una opcion: \n")
        match opcion:
            case "1":
                print(" \n --------------------------------------------------------------")
                print("Cargando archivo")
                global archivo
                global route
                global root
                archivo = None  # Reinicializa la variable archivo
                route = askopenfilename(filetypes=[("Archivo XML", "*.xml")])
                archivo = open(route, "r")
                archivo.close()
                # Parciar XMML
                tree = ET.parse(route)
                root = tree.getroot()
                print("Archivo cargado con exito ")
                print("-------------------------------------------------------------- \n")
                menu()
            case "2":
                global nombre_senal
                global tiempo_senal
                global amplitud_senal
                print("Procesando archivo \n")
                print("--------------------------------------------------------------")
                if archivo is None:
                    print("Primero debes cargar un archivo.")
                    menu()
                else:
                    for senal_temporal in root.findall("senal"):
                        nombre_senal=senal_temporal.get("nombre")
                        tiempo_senal=senal_temporal.get("t")
                        amplitud_senal=senal_temporal.get("A")
                        print("Analizando Señales")
                        for dato_senal in senal_temporal.findall("dato"):
                            tiempo_dato = dato_senal.get("t")
                            amplitud_dato = dato_senal.get("A")
                            data_dato = dato_senal.text
                            #? Nueva medicion
                            nuevo = dato(int(tiempo_dato),amplitud_dato,data_dato)
                            lista_datos_temporal.add_dato(nuevo)
                            if contador == 0:
                                print("Analizando Patrones y creando matriz reducida")
                            if data_dato !="0": 
                                nuevo = dato(int(tiempo_dato),amplitud_dato,1)
                                lista_binaria_temporal.add_dato(nuevo)
                            else:
                                nuevo = dato(int(tiempo_dato),amplitud_dato,0)
                                lista_binaria_temporal.add_dato(nuevo)
                            contador +=1
                        lista_senales_temporal.add_senal(senal(nombre_senal,
                                                            tiempo_senal,
                                                            amplitud_senal,
                                                            lista_datos_temporal,
                                                            lista_binaria_temporal,
                                                            lista_grupos_temporal,
                                                            lista_patrones_temporal))
                        lista_datos_temporal.recorrer()
                        lista_binaria_temporal.recorrer()
                        
                    
                print("--------------------------------------------------------------")
                print("Procesamiento de archivo finalizado")
                print("--------------------------------------------------------------\n")
                
                menu()
            case "3":
                lista_senales_temporal.calcular_patrones(nombre_senal)
                menu()
            case "4":
                print(" \n --------------------------------------------------------------")
                print("                        Datos del Estudiante                 ")
                print("--------------------------------------------------------------")
                print("Miguel Ricardo Galicia Urrutia")
                print("202201117")
                print("Introduccion a la Programacion y Computacion 2 seccion \"A\"")
                print("Ingenieria en Ciencias y Sistemas")
                print("4to Semestre \n")
                menu()
            case "5":
                lista_datos_temporal.generar_grafica_original(nombre_senal,tiempo_senal,amplitud_senal)
                menu()
            case "6":
                print("\n --------------------------------------------------------------")
                print("Inicializando sistema")
                lista_datos_temporal.delete()
                lista_datos_temporal.recorrer()
                print("Sistema inicializado con exito")
                print("------------------------------------------------------------------ \n")
                menu()
            case "7":
                print("Gracias por usar el programa \n")
                return False
                
            case _:
                print("Opcion no valida")
                menu()
        break
    
    
menu()
print("------------------------")
print("Ejecucion finalizada")
print("------------------------")
