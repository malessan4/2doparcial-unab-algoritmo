#1.1
class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_de_nacimiento, puntaje):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.puntaje = 0
        self.__articulos_comprados = [] #lista privada
        
    

#1.2    
class Articulos:
    def __init__(self, identificador, nombre, descripcion, marca, precio, puntos):
        if identificador <= 0:
            raise ValueError("El id debe ser mayor que 0")
        self.identificador = int(identificador)
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = float(precio)
        if puntos <= 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self.puntos = int(puntos)
