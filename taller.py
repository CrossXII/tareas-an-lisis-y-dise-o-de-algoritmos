import time
import csv
import openpyxl
import copy

datos = []
bubble_sort = []
insertion_sort = []
selection_sort = []

def  cargar_datos():
    global datos
    datos = []

    archivo = open("datos.txt", "r", encoding="utf-8")
    archivo.readline()

    for linea in archivo:
        partes = linea.strip().split(',')
        datos.append(partes)
    
    archivo.close()

    print("se han cargados:", len(datos), "datos")
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
def bubble_sort(datos):
    n = len(datos)
    for i in range(n):
        intercambiado = False

        for j in range(0, n-i-1):
            if datos[j][3] > datos[j+1][3]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
                intercambiado = True

        #si la bandera sigue en False, el arreglo ya está ordenado
        if not intercambiado:
            print(f"El arreglo ya está ordenado después de {i+1} iteraciones.")
            break

#------------------------------------------------------------------------------------------------
def insertion_sort(datos):

    for i in range(1, len(datos)):
        clave = datos[i]
        j = i - 1

        while j >= 0 and datos[j][3] > clave[3]:
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = clave
#------------------------------------------------------------------------------------------------
def selection_sort(datos):
    n = len(datos)

    for i in range(n):
        indice_minimo = i
        
        #encontramos el elemento mínimo en el arreglo no ordenado
        for j in range(i + 1, n):
            if datos[j][3] < datos[indice_minimo][3]:
                indice_minimo = j
        #guardamos el valor mínimo antes de desplazar los elementos
        valor_minimo = datos[indice_minimo]

        #desplazamos los elementos hacia la derecha para hacer espacio para el valor mínimo
        while indice_minimo > i:
            datos[indice_minimo] = datos[indice_minimo - 1]
            indice_minimo -= 1
        #colocamos el valor mínimo en su posición correcta
        datos[i] = valor_minimo

#------------------------------------------------------------------------------------------------
def exportar_excel(datos_ordenados, nombre_archivo):
    libro = openpyxl.Workbook()
    hoja = libro.active
    hoja.title = "Resultados de Ordenamiento"
    
    encabezados = ["ID", "Nombre", "Edad", "Puntaje evaluativo"]
    hoja.append(encabezados)

    for fila in datos_ordenados:
        hoja.append(fila)
    
    libro.save(nombre_archivo)
    print(f"Resultados exportados a {nombre_archivo} exitosamente.")

#------------------------------Menú principal------------------------------
while True:
    print("\n[1] Cargar datos")
    print("[2] Ordenar con Bubble Sort")
    print("[3] Ordenar con Insertion Sort")
    print("[4] Ordenar con Selection Sort")
    print("[5] Exportar resultados de Bubble Sort a Excel")
    print("[6] Exportar resultados de Insertion Sort a Excel")
    print("[7] Exportar resultados de Selection Sort a Excel")
    print("[8] Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cargar_datos()
    
    elif opcion == '2':
        datos_bubble = copy.deepcopy(datos)
        start_time = time.time()
        bubble_sort(datos_bubble)
        end_time = time.time()
        tiempo = end_time - start_time
        print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
        print("Complejidad:")
        print("Peor Caso Big O: O(n^2)")
        print("Caso Promedio Big Θ: Θ(n^2)")
        print("Mejor Caso Big Ω: Ω(n)")
    
    elif opcion == '3':
        datos_insertion = copy.deepcopy(datos)
        start_time = time.time()
        insertion_sort(datos_insertion)
        end_time = time.time()
        tiempo = end_time - start_time
        print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
        print("Complejidad:")
        print("Peor Caso Big O: O(n^2)")
        print("Caso Promedio Big Θ: Θ(n^2)")
        print("Mejor Caso Big Ω: Ω(n)")
    
    elif opcion == '4':
        datos_selection = copy.deepcopy(datos)
        start_time = time.time()
        selection_sort(datos_selection)
        end_time = time.time()
        tiempo = end_time - start_time
        print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
        print("Complejidad:")
        print("Peor Caso Big O: O(n^2)")
        print("Caso Promedio Big Θ: Θ(n^2)")
        print("Mejor Caso Big Ω: Ω(n)")
    
    elif opcion == '5':
        print("imprimir resltados de bubble sort.")
        exportar_excel(datos_bubble, "resultados_bubble_sort.xlsx")

    elif opcion == '6':
        print("imprimir resltados de insertion sort.")
        exportar_excel(datos_insertion, "resultados_insertion_sort.xlsx")

    elif opcion == '7':
        print("imprimir resltados de selection sort.")
        exportar_excel(datos_selection, "resultados_selection_sort.xlsx")

    elif opcion == '8':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
