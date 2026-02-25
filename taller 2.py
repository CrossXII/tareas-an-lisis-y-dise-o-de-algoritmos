# Imports-------------------------------------
import matplotlib.pyplot as plt

#--------------------------------------------- MODULO 1 ---------------------------------------------
#Ejercicio 1.1--------------------------------

plt.figure(figsize=(10,6))

plt.text(0.5, 0.9,
         r'Análisis Asintótico de $f(n)=7n^2+5n+2$',
         fontsize=18, ha='center')

plt.text(0.05, 0.75,
         r'1) Calculamos el límite dividiendo por el término de mayor grado:',
         fontsize=14)

plt.text(0.08, 0.68,
         r'$\lim_{n \to \infty} \frac{7n^2 + 5n + 2}{n^2}$',
         fontsize=18)

plt.text(0.05, 0.55,
         r'2) Separamos cada término:',
         fontsize=14)

plt.text(0.08, 0.48,
         r'$= \lim_{n \to \infty} \left(7 + \frac{5}{n} + \frac{2}{n^2}\right)$',
         fontsize=18)

plt.text(0.05, 0.38,
         r'3) Cuando $n \to \infty$, entonces:',
         fontsize=14)

plt.text(0.08, 0.31,
         r'$\frac{5}{n} \to 0 \quad y \quad \frac{2}{n^2} \to 0$',
         fontsize=16)

plt.text(0.05, 0.20,
         r'4) Por lo tanto:',
         fontsize=14)

plt.text(0.08, 0.13,
         r'$\lim_{n \to \infty} \frac{7n^2 + 5n + 2}{n^2} = 7$',
         fontsize=18)

plt.text(0.08, 0.05,
         r'$\Rightarrow f(n) \in \Theta(n^2) \subset O(n^2)$',
         fontsize=18)

plt.axis('off')
plt.tight_layout()
plt.show()

#Ejercicio 1.2---------------------------------

plt.figure(figsize=(10,6))

plt.text(0.5, 0.9,
         r'Comparación Asintótica entre $\ln(n)$ y $n$',
         fontsize=18, ha='center')

plt.text(0.05, 0.75,
         r'1) Analizamos el siguiente límite:',
         fontsize=14)

plt.text(0.08, 0.68,
         r'$\lim_{n \to \infty} \frac{\ln(n)}{n}$',
         fontsize=18)

plt.text(0.05, 0.55,
         r"2) Aplicamos regla de L'Hôpital (forma $\frac{\infty}{\infty}$):",
         fontsize=14)

plt.text(0.08, 0.48,
         r'$= \lim_{n \to \infty} \frac{\frac{1}{n}}{1}$',
         fontsize=18)

plt.text(0.05, 0.38,
         r'3) Simplificamos:',
         fontsize=14)

plt.text(0.08, 0.31,
         r'$= \lim_{n \to \infty} \frac{1}{n}$',
         fontsize=18)

plt.text(0.05, 0.20,
         r'4) Como $\frac{1}{n} \to 0$, entonces:',
         fontsize=14)

plt.text(0.08, 0.13,
         r'$\lim_{n \to \infty} \frac{\ln(n)}{n} = 0$',
         fontsize=18)

plt.text(0.08, 0.05,
         r'$\Rightarrow \ln(n) \in o(n) \subset O(n)$',
         fontsize=18)

plt.axis('off')
plt.tight_layout()
plt.show()

#Ejercicio 1.3---------------------------------
plt.figure(figsize=(10,6))

plt.text(0.5, 0.9, 
         r'Comparación Asintótica entre $n!$ y $2^n$', 
         fontsize=18, ha='center')

plt.text(0.05, 0.75,
         r'1) Analizamos el límite:',
         fontsize=14)

plt.text(0.08, 0.68,
         r'$\lim_{n \to \infty} \frac{n!}{2^n}$',
         fontsize=18)

plt.text(0.05, 0.55,
         r'2) Usamos la aproximación de Stirling:',
         fontsize=14)

plt.text(0.08, 0.48,
         r'$n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$',
         fontsize=16)

plt.text(0.05, 0.38,
         r'3) Sustituyendo en el límite:',
         fontsize=14)

plt.text(0.08, 0.31,
         r'$\frac{n!}{2^n} \approx \sqrt{2\pi n}\left(\frac{n}{2e}\right)^n$',
         fontsize=16)

plt.text(0.05, 0.20,
         r'4) Como $\left(\frac{n}{2e}\right)^n \to \infty$, entonces:',
         fontsize=14)

plt.text(0.08, 0.12,
         r'$\lim_{n \to \infty} \frac{n!}{2^n} = \infty$',
         fontsize=18)

plt.text(0.08, 0.05,
         r'$\Rightarrow n! \in \omega(2^n)$',
         fontsize=18)

plt.axis('off')
plt.show()

#---------------------------------------------- MODULO 2 ---------------------------------------------
#Ejercicio 2.1---------------------------------
def buscar_par_especifico(lista, objetivo):
    # Analiza este codigo
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] %2 == 0 and lista[i] == objetivo:
            return True, pasos
    return False, pasos
"""El algoritmo recorre la lista elemento por elemento utilizando un ciclo for. 
En cada iteración incrementa un contador de pasos y verifica si el elemento actual es par y además es igual al valor objetivo. 
Si ambas condiciones se cumplen, el algoritmo termina inmediatamente retornando True junto con el número de pasos realizados. 
Si el elemento no se encuentra, el ciclo finaliza después de recorrer toda la lista y retorna False.

El mejor caso ocurre cuando el primer elemento de la lista cumple la condición. Por ejemplo, si lista = [8, 3, 5, 7] y objetivo = 8, 
el algoritmo solo realiza una iteración y termina inmediatamente. En este caso, el número de operaciones es constante, por lo tanto la complejidad 
en el mejor caso es O(1).

El peor caso ocurre cuando el elemento no está en la lista o se encuentra en la última posición. 
Por ejemplo, si lista = [1, 3, 5, 7, 10] y objetivo = 10, el algoritmo debe recorrer todos los elementos antes de encontrarlo. 
En este escenario realiza n iteraciones, donde n es el tamaño de la lista. Por lo tanto, la complejidad en el peor caso es O(n).

En el caso promedio, si el elemento está distribuido aleatoriamente dentro de la lista, el algoritmo recorrerá aproximadamente la mitad 
de los elementos antes de encontrarlo. Sin embargo, en notación Big O se eliminan constantes como n/2, por lo que la complejidad promedio también 
se considera O(n).

En conclusión, aunque el algoritmo puede terminar rápidamente en el mejor caso, su complejidad asintótica está determinada por el peor escenario.
Por ello, la notación Big O del algoritmo es O(n), ya que el número de operaciones crece de manera proporcional al tamaño de la lista."""

#Ejercicio 2.2---------------------------------
def algoritmo_misterioso(n):
    #Analiza el crecimiento de 'i'
    i = 1
    operaciones = 0
    while i < n:
        operaciones += 1
        i = i * 2
        return operaciones
"""Este algoritmo inicializa la variable i en 1 y entra en un ciclo while que se ejecuta mientras i sea menor que n. 
En cada iteración, incrementa el contador operaciones y duplica el valor de i (es decir, i = i * 2). 
Sin embargo, el return operaciones está dentro del while, lo que provoca que el ciclo termine después de la primera iteración.

Debido a esto, el comportamiento real del algoritmo es diferente al esperado:
Si n es mayor que 1, el ciclo entra una sola vez y retorna inmediatamente.
Si n es menor o igual a 1, el ciclo nunca se ejecuta y la función no retorna nada explícitamente (retorna None).

Mejor Caso:
Ocurre cuando n <= 1, ya que el ciclo while no se ejecuta ninguna vez. En este caso no se realizan iteraciones. La complejidad es O(1).

Peor Caso:
Si n > 1, el ciclo entra una sola vez debido al return interno y termina inmediatamente. Por lo tanto, 
también realiza un número constante de operaciones. La complejidad es O(1).

Conclusión con el código actual:
Debido a que el return está dentro del ciclo, el algoritmo siempre realiza como máximo una iteración. 
Por lo tanto, su complejidad temporal es O(1)."""

#----------------------------------------------- MODULO 3 ---------------------------------------------
#Ejercicio 3.1---------------------------------
#RETO A:
def interseccion_ingenua(lista1, lista2):
    resultado = []
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                if elemento1 not in resultado:
                    resultado.append(elemento1)
    return resultado
"""EXPLICACIÓN:
Se recorre cada elemento de lista1.
Por cada elemento, se recorre completamente lista2.
Si coinciden, se agrega al resultado.

Si lista1 tiene n elementos y lista2 tiene m elementos, el algoritmo realiza aproximadamente:
n × m comparaciones.

Si ambas listas tienen tamaño n:
Complejidad → O(n²)."""

#RETO B:
def interseccion_set(lista1, lista2):
    conjunto2 = set(lista2)
    resultado = []
    for elemento in lista1:
        if elemento in conjunto2:
            resultado.append(elemento)
    return resultado
"""EXPLICACIÓN:
Convertimos lista2 en un set.
La operación elemento in conjunto2 tiene complejidad promedio O(1).
Luego recorreos lista1 una sola vez.

Si ambas listas tienen tamaño n:
Convertir a set - O(n)
Recorrer lista1 - O(n)
Complejidad total - O(n)"""

#RETO C:
"""Por qué la versión con set es más rápida?

En el Módulo 1 vimos que:
Una búsqueda en una lista es O(n) porque puede necesitar recorrer todos los elementos.
Una búsqueda en un set es O(1) en promedio, porque Python implementa los sets usando tablas hash.

En la versión ingenua:
Por cada elemento de la primera lista, recorremos completamente la segunda.
Eso produce crecimiento cuadrático → O(n²).

En la versión con set:
Solo recorremos una lista.
Las búsquedas son constantes. 
El crecimiento es lineal - O(n)."""

#Ejercicio 3.2---------------------------------
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

"""Esta implementación tiene complejidad O(2^n) porque cada llamada genera dos nuevas llamadas recursivas, 
formando un árbol que crece de manera exponencial.

Muchos valores se recalculan varias veces, lo que provoca una gran cantidad de trabajo repetido.

Por ejemplo, al calcular fibonacci se vuelve a calcular fibonacci más de una vez. A medida que n crece, 
el número de llamadas aumenta aproximadamente como 2^n.

Si n = 50, el número de llamadas es extremadamente grande (del orden de millones o incluso más), 
lo que hace que el programa tarde demasiado tiempo y consuma muchos recursos. Por eso la computadora puede parecer que se bloquea.

Conclusión:
La versión recursiva simple de Fibonacci tiene crecimiento exponencial O(2^n) y no es eficiente para valores grandes de n."""