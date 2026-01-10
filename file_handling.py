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

