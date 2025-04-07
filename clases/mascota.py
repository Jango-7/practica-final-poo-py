class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio
    
    def actualizar_info(self, edad=None, salud=None, precio=None):
        #En principio, cada item va a estar por default en None, pero si hay una actualizacion, esto va a cambiar a traves del siguiente if...
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio
    
    def mostrar_info(self):
        return f'Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}'

# CLASES QUE HEREDAN DE MASCOTA:

class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.energia = energia
    
    def mostrar_caracteristicas(self):
        return f'Raza: {self.raza}, Nivel de energia: {self.energia}'
    

class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia
    
    def mostrar_caracteristicas(self):
        return f'Raza: {self.raza}, Nivel de independencia: {self.independencia}'