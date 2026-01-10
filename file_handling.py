#Context manager - with
#Modos de apertura
#Modo   Descripción     Comportamiento al puntero   Crea archivo?
#'r'    Lectura         Al inicio.                  No
#'w'    Escritura       Al inicio                   Si
#'a'    Agregar         Al final                    Si
#'r+'   Leer y escribir Al inicio                   No
#'x'    Creación excl.  Al inicio.                  Si

#Mala práctica
# file = open('datos.txt', 'r')
# contenido = file.read()
# file.close()

#Buena práctica
# with open('datos.txt', 'r', encoding='utf-8') as file_cm:
#     contenido = file_cm.read()


with open('E:/data_F/flavors_of_cacao.csv', 'r') as file_cacao:
    for linea in file_cacao:
        continue
        # print(linea.strip())

def guardar_tareas():
    tareas = []
    print("Ingresa 3 tareas para hoy:")

    for i in range(3):
        tarea = input(f'Tarea {i+1}: ')
        tareas.append(tarea + "\n")

    #Usamos 'w' para crear o sobreescribir
    with open('E:/data_F/tareas.txt', 'w', encoding='utf-8') as archivo:
        archivo.writelines(tareas)

    print("Tareas guardadas exitosamente en tareas.txt")

# guardar_tareas()


import os

def crear_respaldo(origen, destino):
    #1 validar si el archivo existe
    if not os.path.exists(origen):
        print(f"Error: El archivo original '{origen}' no existe.")
        return None

    #2 validar si existe el destino para no sobreescribir sin permiso
    if os.path.exists(destino):
        respuesta = input(f"El archivo '{destino}' ya existe. ¿Sobreescribir? (s/n):")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            return None

    #3 proceso de copia
    try:
        with open(origen, 'r', encoding='utf-8') as f_origen:
            contenido = f_origen.read()

        with open(destino, 'w', encoding='utf-8') as f_destino:
            f_destino.writelines(contenido)

        print(f'Copia de seguridad creada en {destino}')
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')

crear_respaldo('E:/data_F/tareas.txt', 'E:/data/respaldo_tareas.txt')