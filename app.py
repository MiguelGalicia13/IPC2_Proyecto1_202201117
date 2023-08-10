from lista_enlazada import lista_enlazada
from tkinter import Tk
from tkinter.filedialog import askopenfilename

datos = lista_enlazada()
def menu():
    print("----------Menu----------")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo Salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar Grafica")
    print("6. inicializar sistema")
    print("7. salir")
    opcion=input("Ingrese una opcion: ")
    while True:
        match opcion:
            case "1":
                Tk().withdraw() #! Abre un explorador de Archivos
                #! Extensiones de archivos permitidas
                extensiones = [("Archivo XML", "*.xml")]
                #! Filtro para encontrar solo archivos con extension .XML
                filename = askopenfilename(filetypes=extensiones)
                if filename:
                    with open(filename, 'r') as archivo:
                        print("Archivo cargado con exito")
                menu()
            case "2":
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
                if(datos.is_empty()):
                    print("Lista vacia")
                    menu()
                else:
                    datos.delete_list()
                    print("Lista inicializada")
                menu()
            case "7":
                print("Gracias por usar el programa")
                break
            case _:
                print("Opcion no valida")
                menu()
        return False

menu()
