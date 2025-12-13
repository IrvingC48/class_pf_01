#Uso de args
#Sumar un precio base más cualquier cantidad de costos extras
def calcular_total(base, *args):
    total_extras = sum(args)
    return base + total_extras

print(f"Total a pagar: ${calcular_total(100,10,5,20)}")


#Uso de valores de retorno
#Devolver máximo, mínimo y promedio en una sola llamada.
def analizar_lista(numeros):
    if not numeros:
        return None #Protección contra listas vacías

    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)

    #Devolucion en una tupla
    return mayor, menor, promedio

#Desestructuración de la tupla retornada
res_mayor, res_menor, res_promedio = analizar_lista([10, 8, 9, 5])
print(f'Mayor: {res_mayor}, Menor: {res_menor}, Promedio: {res_promedio}')


#Uso de recursividad
#Cuenta regresiva que imprime ¡Despegue! al llegar a cero.
def cuenta_regresiva(n):
    #Caso base
    if n <= 0:
        print("¡Despegue!")
    #Caso recursivo: Se llama a sí misma con n-1
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(10)