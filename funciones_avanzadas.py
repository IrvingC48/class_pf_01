#Uso de args
def calcular_total(base, *args):
    total_extras = sum(args)
    return base + total_extras

print(f"Total a pagar: ${calcular_total(100,10,5,20)}")