#Caso de uso: Algoritmo de Optimización de Rutas
#Simular la búsqueda de "tesoros" en diferentes puntos de una ruta, optimizando la búsqueda 
# al parar cuando encuentra un tesoro de alto valor.

#Reglas del algoritmo:
#1. Se utilizan una lista de tuplas, donde cada tupla representa un punto de la ruta (coordenada, valor_tesoro).
#2. Ciclo anidado:
#   - El ciclo for exterior itera sobre las diferentes rutas a explorar.
#   - El ciclo for interior itera sobre cada punto de la ruta actual.
#3. if, else: Determina si el valor del tesoro es suficiente para detener la búsqueda (valor >= 100).
#4. break: Si se encuentra un tesoro con un valor suficientemente alto (>= 100), se utiliza break
#   para detener inmediatamente  la exploración de esa ruta.
#5. continue: Si el punto de la ruta actual no es accesible (valor_tesoro == 0).

rutas_exploracion = [
    #Ruta 1
    [("A1", 50), ("A2", 90), ("A3", 160), ("A4", 20)],
    #Ruta 2
    [("B1", 10), ("B2", 0), ("B3", 40), ("B4", 75)],
    #Ruta 3
    [("C1", 10), ("C2", 20), ("C3", 30), ("C4", 88)],
    #Ruta 4
    [("D1", 150), ("D2", 10), ("D3",20 )],
]

valor_objetivo = 100 # El valor mínimo para detener la búsqueda

print("-- Iniciando el optimizador de búsqueda de tesoros --")
print(f'El valor mínimo para optimizar la búsqueda es: {valor_objetivo}\n')

