"""
Ejercicio 1: Suma de un arreglo
Implementa un algoritmo que calcule la suma de los elementos de un arreglo utilizando Divide y 
Vencerás. Formula la recurrencia que describe su complejidad y resuélvela.
"""
from doctest import master


def suma_arreglo(A, inicio, fin):

    if inicio == fin:
        return A[inicio]

    medio = (inicio + fin) // 2  #<-- Esto solo calcula un numero (O1)

    suma_izq = suma_arreglo(A, inicio, medio)  #<-- Esto hace la llamada recursiva para la parte izquierda del arreglo T(n/2)
    suma_der = suma_arreglo(A, medio + 1, fin) #<-- Esto hace la llamada recursiva para la parte derecha del arreglo T(n/2)
    #eso nos da T(n/2) + T(n/2) = 2T(n/2)

    return suma_izq + suma_der   #<-- Esto suma los resultados de las partes izquierda y derecha del arreglo (O1)
"""
Recurrencia:
T(n) = 2T(n/2) + O(1)
Aplicamos el teorema maestro:
a = 2 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(1) (costo de combinar los resultados)
pero para ser mas entendible se combertira T(n) = 2T(n/2) + O(1) a T(n) = 2T(n/2) + 1
Comparando Alpha con log base b de a:
log base 2 de 2 = 1
Alpha = 1 > K = 0  
Entonces, según el teorema maestro, la solución es:
O(n)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 2: Búsqueda del máximo y mínimo
Diseña un algoritmo basado en Divide y Vencerás para encontrar el elemento máximo y mínimo de un 
arreglo. Analiza su complejidad y compárala con el enfoque iterativo.
"""
def max_min(A, inicio, fin):

    if inicio == fin:
        return A[inicio], A[inicio]  #<-- Si el arreglo tiene un solo elemento, ese elemento es tanto el máximo como el mínimo (O1)

    if fin == inicio + 1:            #<-- Si el arreglo tiene dos elementos, comparamos ambos para determinar cuál es el máximo y cuál es el mínimo (O1)
        if A[inicio] > A[fin]:
            return A[inicio], A[fin] 
        else:
            return A[fin], A[inicio]

    medio = (inicio + fin)//2   #<-- Esto solo calcula un numero (O1)

    max1, min1 = max_min(A, inicio, medio) #<-- Esto hace la llamada recursiva para la parte izquierda del arreglo T(n/2)
    max2, min2 = max_min(A, medio+1, fin)  #<-- Esto hace la llamada recursiva para la parte derecha del arreglo T(n/2)
    #eso nos da T(n/2) + T(n/2) = 2T(n/2)

    return max(max1,max2), min(min1,min2)  #<-- Esto combina los resultados de las partes izquierda y derecha del arreglo para determinar el máximo y mínimo general (O1)
"""
Recurrencia:
T(n) = 2T(n/2) + 1
Aplicamos el teorema maestro:
a = 2 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(1) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 2 de 2 = 1
Alpha = 1 > K = 0  
Entonces, según el teorema maestro, la solución es:
O(n)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 3: Multiplicación de enteros grandes
Dado dos números grandes representados como cadenas, implementa un algoritmo de Divide y 
Vencerás para multiplicarlos eficientemente (como el algoritmo de Karatsuba). Determina su 
complejidad.
"""
def karatsuba(x, y):

    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)  # <-- Caso base: si los números tienen un solo dígito, se multiplican directamente (O1)

    n = max(len(x), len(y))  
    mitad = n // 2  # <-- Solo calcula tamaños y posiciones (O1)

    a = x[:-mitad]  
    b = x[-mitad:]  
    c = y[:-mitad]  
    d = y[-mitad:]  # <-- Divide los números en dos partes (esto solo copia o separa cadenas, costo O(n))

    ac = karatsuba(a, c)  # <-- Multiplica las partes altas (llamada recursiva de tamaño n/2) → T(n/2)

    bd = karatsuba(b, d)  # <-- Multiplica las partes bajas (llamada recursiva de tamaño n/2) → T(n/2)

    ad_bc = karatsuba(str(int(a)+int(b)), str(int(c)+int(d))) - ac - bd  # <-- Tercera multiplicación recursiva usando (a+b)(c+d) → T(n/2)

    # hasta aquí tenemos
    # T(n/2) + T(n/2) + T(n/2) = 3T(n/2)

    resultado = ac * 10**(2*mitad) + ad_bc * 10**mitad + bd  # <-- Combinar resultados (sumas, restas y desplazamiento de dígitos) → O(n)

    return resultado
"""
Recurrencia:
T(n) = 3T(n/2) + O(n)
Aplicamos el teorema maestro:
a = 3 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(1) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 2 de 3 ≈ 1.585
Alpha ≈ 1.585 > K = 1
Entonces, según el teorema maestro, la solución es:
O(n^1.585)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 4: Potenciación rápida
Utiliza Divide y Vencerás para calcular a^b en tiempo eficiente. Explica cómo este enfoque mejora el 
método ingenuo
"""
def potencia(a,n):

    if n==0:   #<-- Caso base: cualquier número elevado a la potencia de 0 es 1 (O1)
        return 1

    mitad = potencia(a,n//2)  #<-- Llamada recursiva para calcular a^(n/2) → T(n/2)

    if n%2==0:   #<-- Si n es par, entonces a^n = (a^(n/2))^2, lo que se calcula con una sola multiplicación adicional (O1)
        return mitad*mitad
    else:
        return a*mitad*mitad
"""
Recurrencia:
T(n) = T(n/2) + O(1)
Aplicamos el teorema maestro:
a = 1 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(1) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 2 de 1 = 0
Alpha = 0 < K = 1
Entonces, según el teorema maestro, la solución es:
O(n^0 log n) = O(log n)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 5: Ordenación con Merge Sort
Implementa el algoritmo Merge Sort para ordenar un arreglo. Escribe la recurrencia que lo define y 
resuélvela
"""
def merge_sort(A):

    if len(A) <= 1:
        return A  # <-- Caso base: si el arreglo tiene 1 elemento ya está ordenado (O1)
    
    medio = len(A) // 2  # <-- Solo calcula una posición en el arreglo (O1)

    izquierda = merge_sort(A[:medio])  # <-- Llamada recursiva para la mitad izquierda del arreglo T(n/2)
    derecha = merge_sort(A[medio:])  # <-- Llamada recursiva para la mitad derecha del arreglo T(n/2)
    # hasta aquí tenemos
    # T(n/2) + T(n/2) = 2T(n/2)

    return merge(izquierda, derecha)  # <-- Combina las dos mitades ordenadas recorriendo todos los elementos (O(n))


def merge(L, R):

    resultado = []
    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            resultado.append(L[i])
            i += 1
        else:
            resultado.append(R[j])
            j += 1   # <-- Recorre los elementos de ambas listas (O(n))

    resultado += L[i:]
    resultado += R[j:]   # <-- Copia los elementos restantes (O(n))

    return resultado
"""
Recurrencia:
T(n) = 2T(n/2) + O(n)
Aplicamos el teorema maestro:
a = 2 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(n) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 2 de 2 = 1
Alpha = 1 < K = 1 
Entonces, según el teorema maestro, la solución es:
O(n log n)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 6: Multiplicación de matrices con Strassen
Implementa el algoritmo de Strassen para multiplicación de matrices. Escribe su recurrencia y calcula 
su complejidad.
"""
def strassen(A, B):

    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]  # <-- Caso base: multiplicar dos números (O1)

    mitad = n // 2  # <-- Solo calcula el punto medio de la matriz (O1)

    # dividir matrices en 4 submatrices
    A11, A12, A21, A22 = dividir(A)
    B11, B12, B21, B22 = dividir(B)  # <-- dividir matrices en partes más pequeñas (O(n²))

    # 7 multiplicaciones recursivas
    M1 = strassen(A11 + A22, B11 + B22)  # T(n/2)
    M2 = strassen(A21 + A22, B11)        # T(n/2)
    M3 = strassen(A11, B12 - B22)        # T(n/2)
    M4 = strassen(A22, B21 - B11)        # T(n/2)
    M5 = strassen(A11 + A12, B22)        # T(n/2)
    M6 = strassen(A21 - A11, B11 + B12)  # T(n/2)
    M7 = strassen(A12 - A22, B21 + B22)  # T(n/2)

    # hasta aquí tenemos
    # T(n/2) + T(n/2) + T(n/2) + T(n/2) + T(n/2) + T(n/2) + T(n/2)
    # = 7T(n/2)

    # combinar resultados
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6 # <-- sumas y restas de matrices (O(n²))

    return combinar(C11, C12, C21, C22)
"""
Recurrencia:
T(n) = 7T(n/2) + O(n²)
Aplicamos el teorema maestro:
a = 7 (número de subproblemas)
b = 2 (factor de reducción del tamaño del problema)
K = O(n²) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 2 de 7 ≈ 2.807
Alpha ≈ 2.807 > K = 2
Entonces, según el teorema maestro, la solución es:
O(n^2.807)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio 7: Búsqueda en una matriz ordenada
Dada una matriz n * n donde cada fila y cada columna están ordenadas ascendentemente, diseña un 
algoritmo basado en Divide y Vencerás para encontrar un número en la matriz en tiempo 
subcuadrático.
"""
def buscar_matriz(M, x):

    n = len(M)  # <-- obtiene el tamaño de la matriz (O1)

    fila = 0  
    col = n - 1  # <-- empieza en la esquina superior derecha (O1)

    while fila < n and col >= 0:  # <-- este ciclo puede ejecutarse como máximo n+n veces

        if M[fila][col] == x:
            return True  # <-- si encontramos el número terminamos (O1)

        elif M[fila][col] > x:
            col -= 1  # <-- nos movemos una columna a la izquierda (O1)

        else:
            fila += 1  # <-- nos movemos una fila hacia abajo (O1)

    return False
"""
Recurrencia:
T(n) = O(n) (en el peor caso, recorremos una fila y una columna completas)
Aplicamos el teorema maestro:
a = 0 (no hay subproblemas recursivos)
b = 1 (no hay reducción del tamaño del problema)
K = O(n) (costo de la búsqueda lineal)
Comparando Alpha con log base b de a:
log base 1 de 0 no está definido, pero podemos considerar que Alpha = 0
Alpha = 0 < K = 1
Entonces, según el teorema maestro, la solución es:
O(n)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Ejercicio Big Θ
Diga que hace el siguiente algoritmo y determine su coste en función de n.
"""
int misteri (int n){
    int f = 1;
    for (int i = 2; i <= n; ++i)f*=i;
    return f;
}
"""
El algoritmo calcula el factorial de n (n!). 
El costo de este algoritmo es O(n) porque realiza una multiplicación para cada número desde 2 hasta n, 
lo que da un total de n-1 multiplicaciones. 
Por lo tanto, la complejidad temporal es lineal con respecto a n.

para reforzar el análisis, podemos escribir la recurrencia de este algoritmo como:
T(n) = T(n-1) + O(1) para n > 1
T(1) = O(1)
Aplicando el teorema maestro a esta recurrencia:
a = 1 (número de subproblemas)
b = 1 (factor de reducción del tamaño del problema)
Alpha = 0 (ya que T(n-1) es T(n) con n reducido en 1)
K = O(1) (costo de combinar los resultados)
Comparando Alpha con log base b de a:
log base 1 de 1 = 0
Alpha = 0 < K = 1
Entonces, según el teorema maestro, la solución es:
O(n)
"""