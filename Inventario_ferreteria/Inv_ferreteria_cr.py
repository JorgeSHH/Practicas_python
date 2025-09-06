inventario_fer = [("destornillador", 10, 20), ("martillo", 40, 20),
                  ("tenaza", 15.2, 20), ("cautin", 10, 20), ("tuercas", 1.5, 200),
                  ('clavos', 5.75, 500)]

def ver_inventario(inventario):
    """Muestra el inventario actual"""
    print("\n---------------- INVENTARIO ----------------")
    print("Producto         | Precio    | Cantidad")
    print("------------------------------------------")
    for nombre, precio, cantidad in inventario:
        print(f"{nombre:<15} | ${precio:<8.2f} | {cantidad:<8}")
    print("--------------------------------------------\n")

def registrar_venta(inventario):
    """Registra la venta de un producto y actualiza el inventario"""
    while True:
        nombre_producto = input("Ingrese el nombre del producto a vender (o 'salir'): ").lower()
        if nombre_producto == 'salir':
            break

        producto_encontrado = False
        for i, (nombre, precio, cantidad) in enumerate(inventario):
            if nombre == nombre_producto:
                producto_encontrado = True
                try:
                    cantidad_a_vender = int(input("Ingrese la cantidad a vender: "))
                except ValueError:
                    print("Por favor, ingrese una cantidad válida.")
                    continue

                if cantidad_a_vender > 0 and cantidad_a_vender <= cantidad:
                    print(f"Venta exitosa. Ha vendido {cantidad_a_vender} unidades de {nombre}.")
                    nueva_tupla = (nombre, precio, cantidad - cantidad_a_vender)
                    inventario[i] = nueva_tupla
                    print("Inventario actualizado.\n")
                    return # Salir de la funcion despues de una venta exitosa
                else:
                    print("Cantidad no válida o stock insuficiente. Intente de nuevo.\n")
                    break
        
        if not producto_encontrado:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario. Intente de nuevo.\n")

def menu_principal():
    """Muestra el menú principal y maneja la lógica del programa."""
    while True:
        print("---------- MENÚ PRINCIPAL ----------")
        print("1. Ver inventario")
        print("2. Registrar venta")
        print("3. Salir")
        print("-------------------------------------")

        try:
            opcion = int(input("Ingrese el número de la opción escogida: "))
            print()
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número del 1 al 3.\n")
            continue
        
        if opcion == 1:
            ver_inventario(inventario_fer)
        elif opcion == 2:
            registrar_venta(inventario_fer)
        elif opcion == 3:
            print("Saliendo del sistema. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.\n")

if __name__ == "__main__":
    menu_principal()