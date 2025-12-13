#Uso de args
def calcular_total(base, *args):
    total_extras = sum(args)
    return base + total_extras

print(f"Total a pagar: ${calcular_total(100,10,5,20)}")


#Uso de valores de retorno
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