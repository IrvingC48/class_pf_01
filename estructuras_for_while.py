# Caso de uso while: Validar número entre 1 y 10
#validador = False
while True:#validador == False:
    n = input("Introduce un número entre 1 y 10: ")
    if not(n.isdigit()):
        print("Entrada no válida. Intenta de nuevo.")
        continue
    else:
        n = int(n)
    #if n < 1 or n > 10:
    if 1 <= n <= 10:
        print(f'Número aceptado: {n}')
        break
 #       validador = True
    else:
        print("Fuera de rango. Intenta de nuevo.")