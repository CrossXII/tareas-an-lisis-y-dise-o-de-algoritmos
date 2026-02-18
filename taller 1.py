#PARTE 1----------------------------------------------------------------------------------
# Ejercicio 1.1:
# Lista de 10 dígitos
#mi_lista = [14, 25, 33, 40, 58, 61, 79, 82, 97, 100]

#def procesar_datos(lista):
    #print(f"{'Número':<10} | {'Par/Impar':<10} | {'Último':<10} | {'Mayor vs 50'}")
    #print("-" * 50)
    
    # El bucle for hace que la complejidad sea O(n)
    # n = cantidad de elementos en la lista
    #for n in lista:
        
        # 1. Decidir si es par o impar
        # Es O(1) en tiempo: un solo cálculo de residuo por cada iteración.
        #tipo = "Par" if n % 2 == 0 else "Impar"
        
        # 2. Obtener el último dígito
        # Es O(1) en tiempo: operación aritmética directa.
        #ultimo_digito = n % 10
        
        # 3. Mayor entre el número actual (n) y una constante (50)
        # Es O(1) en tiempo: comparación lógica simple.
        #referencia = 50
        #mayor = n if n > referencia else referencia
        
        #print(f"{n:<10} | {tipo:<10} | {ultimo_digito:<10} | {mayor}")

# Ejecutar la función
#procesar_datos(mi_lista)

# --- Análisis de Complejidad ---
# Tiempo Extra: O(n). Si la lista crece al doble, el tiempo de ejecución crece al doble.
# Espacio Extra: O(1). No creamos estructuras nuevas que dependan del tamaño de la lista; 
# solo usamos las mismas variables temporales (tipo, ultimo_digito, mayor) en cada ciclo.

#Ejercicio 1.2:
#import math

#def busqueda_binaria(lista, objetivo):
    #izq = 0
    #der = len(lista) - 1
    #comparaciones = 0
    
    #while izq <= der:
        #comparaciones += 1
        #medio = (izq + der) // 2
        
        #if lista[medio] == objetivo:
            #return medio, comparaciones
        #elif lista[medio] < objetivo:
            #izq = medio + 1
        #else:
            #der = medio - 1
            
    #return -1, comparaciones

# Lista ordenada
#lista_ordenada = [1, 5, 9, 15, 22, 30, 45, 60, 75, 90]

# 1. Mejor caso (elemento en el centro: 22 o 30 en esta lista de 10)
#indice, comps = busqueda_binaria(lista_ordenada, 22)
#print(f"Mejor caso (22): Índice {indice}, Comparaciones: {comps}")

# 2. Peor caso (elemento no está)
#indice, comps = busqueda_binaria(lista_ordenada, 100)
#print(f"Peor caso (100): Índice {indice}, Comparaciones: {comps}")

# --- Análisis de Complejidad ---
# Tiempo (Peor Caso): O(\log n).Si la lista crece al doble (de 1,000 a 2,000 elementos), el tiempo de ejecución solo aumenta en una (1) comparación adicional. 
# Esto se debe a que en cada paso descartamos la mitad de los elementos restantes.
# Tiempo (Mejor Caso): O(1). Ocurre si el elemento buscado está exactamente en la posición del primer medio calculado. 
# Solo se realiza una comparación, independientemente de si la lista tiene 10 o 10 millones de elementos.
# Espacio Extra: O(1). Al igual que en tu ejemplo anterior, la implementación es iterativa. 
# No importa qué tan grande sea la lista, solo reservamos memoria para unas pocas variables de control (izq, der, medio, comparaciones). 
# No duplicamos la lista ni usamos recursividad que llene la pila de llamadas.
