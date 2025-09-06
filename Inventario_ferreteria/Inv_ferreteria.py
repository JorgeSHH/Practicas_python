
#Ejercicio: Sistema de Gestión de Inventario para una Ferretería

#crear un programa para gestionar el inventario de una pequeña ferretería. 
#El sistema debe permitir al usuario ver el inventario de productos y simular 
#la venta de artículos, actualizando las existencias.
#productos iniciales

# Puntos Clave del Ejercicio

#     Listas: Deberás usar una lista de Python para almacenar todos los productos de tu ferretería. La lista te permitirá agregar o eliminar productos, así como actualizar su información.

#     Tuplas: Cada producto en el inventario será una tupla con tres elementos: (nombre_del_producto, precio_por_unidad, cantidad_en_stock). Las tuplas son perfectas para este caso porque los datos de cada producto (su nombre, precio y cantidad) deben permanecer juntos. Ya que las tuplas son inmutables, para simular una venta y actualizar la cantidad, tendrás que crear una nueva tupla con la cantidad actualizada y reemplazar la antigua en la lista.

# Funcionalidades del Programa

#     Inventario Inicial: El programa debe comenzar con una lista predefinida de productos. Por ejemplo:

#         [('Martillo', 15.50, 20), ('Clavos (caja)', 5.75, 50), ('Destornillador', 12.00, 15), ('Cinta Métrica', 8.25, 30)]

#     Menú Principal: Presenta un menú con las siguientes opciones:

#             Ver inventario: Muestra una lista clara de todos los productos con su precio y cantidad disponible.

#             Registrar venta: Permite al usuario "comprar" un producto. Deberás pedir el nombre del producto y la cantidad deseada. Si hay suficientes unidades en stock, actualiza el inventario restando la cantidad vendida. Si no, informa al usuario que el producto no está disponible o que no hay suficientes unidades.

#             Salir: Termina el programa.

#     Bucle de Ejecución: El programa debe continuar mostrando el menú hasta que el usuario elija la opción "Salir".



inventario_fer = [("destornillador", 10, 20), ("martillo", 40, 20), 
              ("tenaza", 15.2, 20), ("Cautin", 10, 20), ("tuercas", 1.5, 200), 
              ('clavos', 5.75, 500)]


def ver_inventario(inventario):
    """
    Esta Funcion mostrara el inventario actual 
    """
    recorrido = len(inventario)

    print("    Producto|  precio  | cantidad")
    print("")

    for i in range(recorrido):
        print("- ", inventario[i][0], " | ", inventario[i][1], " | ", inventario[i][2])
        print("")

def registrar_venta(inventario):
    """
    Funcion que...
    """
    while True:
        nombre_producto = input("ingrese el nombre del producto:").lower()

        try:
            cantidad_producto = int(input("ingrese la cantidad a retirar"))
        except ValueError:
            print("Ingrese un numero o fromato valido")
            continue
        
        recorrido = len(inventario)

        for i in range(recorrido):
            if nombre_producto == inventario[i][0]:
                if cantidad_producto <= inventario[i][2]:
                    print("Gracias por su compra")
                    cantidad_actual = inventario[i][2] 
                    new_tupla_valor = ( inventario[i][0], inventario[i][1], (cantidad_actual - cantidad_producto))
                    inventario.pop(i)
                    inventario.append(new_tupla_valor)
                    print("Inventario actualizado...")
                    break
                else:
                    print("Lo sentimos, no hay dicha cantidad de produto")
                    break
            else:
                continue
        break
              

def menu_principal():
    """
    Funcion encargada de llamar a el menu principal y mostrar las opciones:

    1. Ver inventario
    2. Registrar venta
    3. Salir
    
    """
    while True:
        print("Menu Principal de la Ferreteria")
        print("1. Ver inventario")
        print("2. Registrar venta")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("ingrese el numero de la opcion escogida: "))
        except ValueError:
            print("")
            print("---------------------------------------")
            print("Escoja una opcion valida...")
            print("----------------------------------------")
            print("")
            continue
        
        if opcion == 1:
            #llamar a funcion de ver inventario
            ver_inventario(inventario_fer)
        elif opcion == 2:
            #llama a funcion de registrar venta
            registrar_venta(inventario_fer)
        elif opcion == 3:
            break
            

menu_principal()


