
videojuegos = {}
registro_ventas = []

def agregar_videojuego(codigo, nombre,plataforma , precio, cantidad):
    if codigo in videojuegos:
        print("El código ya existe. No se puede agregar el videojuego.")
    else:        videojuegos[codigo] = {
            "nombre": nombre,
            "plataforma": plataforma,
            "precio": precio,
            "cantidad": cantidad
        }
    print("Videojuego agregado exitosamente.")
    
def mostrar_inventario():
    if not videojuegos:
        print("No hay videojuegos en el inventario.")
    else:
        print("\n=====Listado de Videojuegos=====")        
        for codigo, info in videojuegos.items():
            
            print(f"\nCódigo: {codigo},\nNombre: {info['nombre']},\nPlataforma: {info['plataforma']},\nPrecio: {info['precio']},\nCantidad: {info['cantidad']}\n")
            

def buscar_videojuego(codigo):
    if codigo in videojuegos:
        info = videojuegos[codigo]
        print("\n=====Información del Videojuego=====")
        print(f"\nCódigo: {codigo},\nNombre: {info['nombre']},\nPlataforma: {info['plataforma']},\nPrecio: {info['precio']},\nCantidad: {info['cantidad']}\n")
    else:
        print("Videojuego no encontrado.")
        

def actualizar_precio(codigo, nuevo_precio):
    if codigo in videojuegos:
        videojuegos[codigo]["precio"] = nuevo_precio
        print("Precio actualizado exitosamente.")
    else:
        print("Videojuego no encontrado.")
        

def registrar_venta(codigo, cantidad_vendida):
    if codigo in videojuegos:
        if videojuegos[codigo]["cantidad"] >= cantidad_vendida:
            videojuegos[codigo]["cantidad"] -= cantidad_vendida
            print("Factura:")
            print(f"Videojuego: {videojuegos[codigo]['nombre']}")
            print(f"Cantidad: {cantidad_vendida}")
            print(f"Total: ${videojuegos[codigo]['precio'] * cantidad_vendida:.2f}")
            venta = registro_ventas.append([codigo, videojuegos[codigo]['nombre'], cantidad_vendida, videojuegos[codigo]['precio'] * cantidad_vendida])
        else:
            print("No hay suficiente stock para registrar la venta.")
    else:
        print("Videojuego no encontrado.")
        

def mostrar_estadisticas():
    if videojuegos:
        total_videojuegos = len(videojuegos)
        valor_total_inventario = sum(info["precio"] * info["cantidad"] for info in videojuegos.values())
        videojuego_mas_caro = max(videojuegos.items(), key=lambda x: x[1]["precio"]) 
        videojuego_m_existente = max(videojuegos.items(), key=lambda x: x[1]["cantidad"])
        cantidad_total = sum(info["cantidad"] for info in videojuegos.values())
        prom_precio = valor_total_inventario / cantidad_total if cantidad_total > 0 else 0
        
        print("\n=====Estadísticas del Inventario=====")
        print(f"Total de videojuegos: {total_videojuegos}") 
        print(f"Valor total del inventario: ${valor_total_inventario:.2f}")
        print(f"Videojuego más caro: {videojuego_mas_caro[1]['nombre']} - ${videojuego_mas_caro[1]['precio']:.2f}")
        print(f"Videojuego con más stock: {videojuego_m_existente[1]['nombre']} - {videojuego_m_existente[1]['cantidad']} unidades")
        print(f"Precio promedio: ${prom_precio:.2f}")


def eliminar_videojuego(codigo):
    if codigo in videojuegos:
        del videojuegos[codigo]
        print(f"Videojuego [{codigo}] eliminado exitosamente.")
    else:
        print("Videojuego no encontrado.")
        
def menu():
    while True:
        print("\n=====Menú de la Tienda de Videojuegos=====")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Mostrar registro de ventas")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            codigo = input("Ingrese el código del videojuego: ")
            if codigo in videojuegos:
                op = input("El código ya existe. ¿Desea agregar más unidades al videojuego existente? (s/n): ")
                if op.lower() == "s":
                    cantidad = int(input("Ingrese la nueva cantidad en stock del videojuego: "))
                    videojuegos[codigo]["cantidad"] += cantidad
                    print("Stock actualizado exitosamente.")
            else:
                nombre = input("Ingrese el nombre del videojuego: ")
                plataforma = input("Ingrese la plataforma del videojuego: ")
                precio = float(input("Ingrese el precio del videojuego: "))
                cantidad = int(input("Ingrese la cantidad en stock del videojuego: "))  
                agregar_videojuego(codigo, nombre, plataforma, precio, cantidad)
                

        elif opcion == "2":
            mostrar_inventario()
            
        elif opcion == "3":
            codigo = input("Ingrese el código del videojuego a buscar: ")
            buscar_videojuego(codigo)
            
        elif opcion == "4":
            codigo = input("Ingrese el código del videojuego para actualizar el precio: ")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo. Por favor, ingrese un valor válido.")
            else:
                actualizar_precio(codigo, nuevo_precio)

        elif opcion == "5":
            codigo = input("Ingrese el código del videojuego para registrar la venta: ")
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
            if cantidad_vendida < 0:
                print("La cantidad vendida no puede ser negativa. Por favor, ingrese un valor válido.")
            else:
                registrar_venta(codigo, cantidad_vendida)
                if codigo in videojuegos and videojuegos[codigo]["cantidad"] < 3:
                    print(f"Advertencia: El stock del videojuego [{codigo}] es bajo. Quedan {videojuegos[codigo]['cantidad']} unidades.")

        elif opcion == "6":
            mostrar_estadisticas()
            
        elif opcion == "7":
            codigo = input("Ingrese el código del videojuego a eliminar: ")
            eliminar_videojuego(codigo)
            
        elif opcion == "8":
            print(registro_ventas)
            
            
        elif opcion == "9":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()


=======
videojuegos = {}
registro_ventas = []

def input_upper(prompt):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("El campo no puede estar vacío. Intente de nuevo.")
            continue
        return valor.upper()


def input_float(prompt):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("El campo no puede estar vacío. Intente de nuevo.")
            continue
        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")


def input_int(prompt):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("El campo no puede estar vacío. Intente de nuevo.")
            continue
        try:
            return int(valor)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero válido.")


def agregar_videojuego(codigo, nombre,plataforma , precio, cantidad):
    if codigo in videojuegos:
        print("El código ya existe. No se puede agregar el videojuego.")
    else:        videojuegos[codigo] = {
            "nombre": nombre,
            "plataforma": plataforma,
            "precio": precio,
            "cantidad": cantidad
        }
    print("Videojuego agregado exitosamente.")
    
def mostrar_inventario():
    if not videojuegos:
        print("No hay videojuegos en el inventario.")
    else:
        print("\n=====Listado de Videojuegos=====")        
        for codigo, info in videojuegos.items():
            
            print(f"\nCódigo: {codigo},\nNombre: {info['nombre']},\nPlataforma: {info['plataforma']},\nPrecio: {info['precio']},\nCantidad: {info['cantidad']}\n")
            

def buscar_videojuego(codigo):
    if codigo in videojuegos:
        info = videojuegos[codigo]
        print("\n=====Información del Videojuego=====")
        print(f"\nCódigo: {codigo},\nNombre: {info['nombre']},\nPlataforma: {info['plataforma']},\nPrecio: {info['precio']},\nCantidad: {info['cantidad']}\n")
    else:
        print("Videojuego no encontrado.")
        

def actualizar_precio(codigo, nuevo_precio):
    if codigo in videojuegos:
        videojuegos[codigo]["precio"] = nuevo_precio
        print("Precio actualizado exitosamente.")
    else:
        print("Videojuego no encontrado.")
        

def registrar_venta(codigo, cantidad_vendida):
    if codigo in videojuegos:
        if videojuegos[codigo]["cantidad"] >= cantidad_vendida:
            videojuegos[codigo]["cantidad"] -= cantidad_vendida
            print("Factura:")
            print(f"Videojuego: {videojuegos[codigo]['nombre']}")
            print(f"Cantidad: {cantidad_vendida}")
            print(f"Total: ${videojuegos[codigo]['precio'] * cantidad_vendida:.2f}")
            venta = registro_ventas.append([codigo, videojuegos[codigo]['nombre'], cantidad_vendida, videojuegos[codigo]['precio'] * cantidad_vendida])
        else:
            print("No hay suficiente stock para registrar la venta.")
    else:
        print("Videojuego no encontrado.")
        

def mostrar_estadisticas():
    if videojuegos:
        total_videojuegos = len(videojuegos)
        valor_total_inventario = sum(info["precio"] * info["cantidad"] for info in videojuegos.values())
        videojuego_mas_caro = max(videojuegos.items(), key=lambda x: x[1]["precio"]) 
        videojuego_m_existente = max(videojuegos.items(), key=lambda x: x[1]["cantidad"])
        cantidad_total = sum(info["cantidad"] for info in videojuegos.values())
        prom_precio = valor_total_inventario / cantidad_total if cantidad_total > 0 else 0
        
        print("\n=====Estadísticas del Inventario=====")
        print(f"Total de videojuegos: {total_videojuegos}") 
        print(f"Valor total del inventario: ${valor_total_inventario:.2f}")
        print(f"Videojuego más caro: {videojuego_mas_caro[1]['nombre']} - ${videojuego_mas_caro[1]['precio']:.2f}")
        print(f"Videojuego con más stock: {videojuego_m_existente[1]['nombre']} - {videojuego_m_existente[1]['cantidad']} unidades")
        print(f"Precio promedio: ${prom_precio:.2f}")


def eliminar_videojuego(codigo):
    if codigo in videojuegos:
        del videojuegos[codigo]
        print(f"Videojuego [{codigo}] eliminado exitosamente.")
    else:
        print("Videojuego no encontrado.")
        
def menu():
    while True:
        print("\n=====Menú de la Tienda de Videojuegos=====")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Mostrar registro de ventas")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            codigo = input_upper("Ingrese el código del videojuego: ")
            if codigo in videojuegos:
                op = input("El código ya existe. ¿Desea agregar más unidades al videojuego existente? (s/n): ")
                if op.lower() == "s":
                    cantidad = input_int("Ingrese la nueva cantidad en stock del videojuego: ")
                    videojuegos[codigo]["cantidad"] += cantidad
                    print("Stock actualizado exitosamente.")
            else:
                nombre = input_upper("Ingrese el nombre del videojuego: ")
                plataforma = input_upper("Ingrese la plataforma del videojuego: ")
                precio = input_float("Ingrese el precio del videojuego: ")
                cantidad = input_int("Ingrese la cantidad en stock del videojuego: ")
                agregar_videojuego(codigo, nombre, plataforma, precio, cantidad)
                

        elif opcion == "2":
            mostrar_inventario()
            
        elif opcion == "3":
            codigo = input_upper("Ingrese el código del videojuego a buscar: ")
            buscar_videojuego(codigo)
            
        elif opcion == "4":
            codigo = input_upper("Ingrese el código del videojuego para actualizar el precio: ")
            nuevo_precio = input_float("Ingrese el nuevo precio: ")
            if nuevo_precio < 0:
                print("El precio no puede ser negativo. Por favor, ingrese un valor válido.")
            else:
                actualizar_precio(codigo, nuevo_precio)

        elif opcion == "5":
            codigo = input_upper("Ingrese el código del videojuego para registrar la venta: ")
            cantidad_vendida = input_int("Ingrese la cantidad vendida: ")
            if cantidad_vendida < 0:
                print("La cantidad vendida no puede ser negativa. Por favor, ingrese un valor válido.")
            else:
                registrar_venta(codigo, cantidad_vendida)
                if codigo in videojuegos and videojuegos[codigo]["cantidad"] < 3:
                    print(f"Advertencia: El stock del videojuego [{codigo}] es bajo. Quedan {videojuegos[codigo]['cantidad']} unidades.")

        elif opcion == "6":
            mostrar_estadisticas()
            
        elif opcion == "7":
            codigo = input_upper("Ingrese el código del videojuego a eliminar: ")
            eliminar_videojuego(codigo)
            
        elif opcion == "8":
            print(registro_ventas)
            
            
        elif opcion == "9":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()


