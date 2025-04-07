from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Gato, Perro
from clases.producto import Producto
from clases.venta import Venta


def registrar_mascota():
    tipo = input("Tipo de mascota (gato/perro): ").strip().lower()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salud = input("Salud: ")
    precio = input("Precio: ")

    if tipo == "perro":
        raza = input("Raza del perro: ")
        energia = input("Nivel de energia: ")
        mascota = Perro(nombre, edad, salud, precio, raza, energia)
    elif tipo == "gato":
        raza = input("Raza: ")
        independencia = input("Nivel de independencia: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido")
        return
    
    return mascota


# REGISTRAR EL CLIENTE

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Direccion del cliente: ")
    telefono = input("Telefono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

# REGISTRAR PRODUCTO

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad de productos: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

# REGISTRAR VENTA

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return
    
    productos = []

    while True:
        nombre_producto = input("Nombre del producto (Deje vacio para finalizar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")
    
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("Venta registrada con exito")
    else:
        print("No se han registrado productos para la venta")


def mostrar_menu():
    print("/n --- Menu de gestion de Patas Felices --- ")
    print("1. Registrar mascota")
    print("2. Registrar cliente")
    print("3. Registrar producto")
    print("4. Registrar venta")
    print("5. Mostrar informacion acerca de mascotas")
    print("6. Mostrar informacion acerca de clientes")
    print("7. Mostrar informacion acerca de productos")
    print("8. Generar alerta de inventario")
    print("9. Salir")


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada con exito!")
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado cn exito!")
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado con exito!")
        
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_info())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_info())
        
        elif opcion == "7":
            for producto in inventario.lista_productos:
                print(producto.mostrar_info())
        
        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el umbral minimo del inventario: "))
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == "9":
            print("Saliendo del sistema. Gracias por usar patas felices APP")
            break

        else:
            print("Opcion no valida. Intente nuevamente")


if __name__ == "__main__":
    main()