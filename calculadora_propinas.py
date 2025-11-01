#Se solicitan datos al usuario, y se validan los siguientes puntos:
#El total de la cuenta debe ser un número positivo.
#El porcentaje de propina debe estar entre 0 y 100.

total_cuenta = int(input("Ingrese el total de la cuenta en pesos:"))
if not(total_cuenta > 0):
    print("Error: Debe ingresar un número positivo para el total de la cuenta.")
    exit()

def solicitar_propina():
    porcentaje_propina = int(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15 para 15%):"))
    if (porcentaje_propina<0) or (porcentaje_propina>100):
        porcentaje_propina = solicitar_propina()
    return porcentaje_propina


#Se calcula el porcentaje de propina y el total a pagar
porcentaje_propina = solicitar_propina()

propina = (total_cuenta * porcentaje_propina) / 100
total_a_pagar = total_cuenta + propina

# Salida de datos: Se muestra la propina y el total a pagar
print(f'El monto de la propina es : ${propina} pesos')
print(f'Total a pagar (incluyendo propina): ${total_a_pagar} pesos')
print("Gracias por su generosidad!")
exit()