total_cuenta = input("Ingrese el total de la cuenta en pesos:")
if not(total_cuenta.isdigit()) or not(total_cuenta > 0):
    print("Error: Debe ingresar un número positivo para el total de la cuenta.")
    exit()

def solicitar_propina():
    porcentaje_propina = input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15 para 15%):")
    if (porcentaje_propina<0) or (porcentaje_propina>100):
        porcentaje_propina = solicitar_propina()
    return porcentaje_propina

porcentaje_propina = solicitar_propina()

propina = (total_cuenta * porcentaje_propina) / 100
total_a_pagar = total_cuenta + propina