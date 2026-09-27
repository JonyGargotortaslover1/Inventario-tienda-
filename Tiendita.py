class InventarioTienda:
    def _init_(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben ser positivos.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                print("Producto actualizado correctamente.")
                return

        self.productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        print("Producto agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad > producto["cantidad"]:
                    print("No hay suficiente stock.")
                    return

                producto["cantidad"] -= cantidad
                print("Venta realizada correctamente.")
                return

        print("El producto no existe.")

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}")

        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print(
                f'Producto: {producto["nombre"]} | '
                f'Precio: ${producto["precio"]:.2f} | '
                f'Cantidad: {producto["cantidad"]}'
            )

    def producto_mas_caro(self):
        if not self.productos:
            print("El inventario está vacío.")
            return None

        producto = max(self.productos, key=lambda p: p["precio"])
        return producto["nombre"], producto["precio"]


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))

            if precio > 0:
                return precio

            print("El precio debe ser positivo.")
        except ValueError:
            print("Introduce un número válido.")


def leer_cantidad(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje))

            if cantidad > 0:
                return cantidad

            print("La cantidad debe ser positiva.")
        except ValueError:
            print("Introduce un número entero válido.")


def main():
    nombre = input("Nombre de la tienda: ").strip()

    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre de la tienda: ").strip()

    inventario = InventarioTienda(nombre)

    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_producto = input("Nombre del producto: ").strip()

            while not nombre_producto:
                print("El nombre no puede estar vacío.")
                nombre_producto = input("Nombre del producto: ").strip()

            precio = leer_precio()
            cantidad = leer_cantidad("Cantidad: ")

            inventario.agregar_producto(
                nombre_producto,
                precio,
                cantidad
            )

        elif opcion == "2":
            nombre_producto = input("Nombre del producto: ").strip()
            cantidad = leer_cantidad("Cantidad a vender: ")

            inventario.vender_producto(
                nombre_producto,
                cantidad
            )

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            resultado = inventario.producto_mas_caro()

            if resultado:
                nombre_producto, precio = resultado
                print(
                    f"Producto más caro: {nombre_producto} - ${precio:.2f}"
                )

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if _name_ == "_main_":
    main()
