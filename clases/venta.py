from datetime import datetime


class Venta:
    def __init__(self, cliente, lista_productos):
        self.cliente = cliente
        self.lista_productos = lista_productos
        self.fecha = datetime.now()
        self.total = self.calcular_total() # El total, es un metodo que vamos a crear luego y a ejecutar aca.
    
    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_productos)
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f'Venta registrada: {self.mostrar_info()}'
    
    def mostrar_info(self):
        productos = ", ".join([producto.nombre for producto in self.lista_productos])
        return f'Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}'