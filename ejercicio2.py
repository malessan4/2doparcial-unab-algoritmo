from ejercicio1 import Comprador
from ejercicio1 import Articulos


#2.1
class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_de_nacimiento, puntaje):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.puntaje = 0
        self.__articulos_comprados = [] #lista privada
        
    def comprar_articulo(self, articulo):
        self.__articulos_comprados.append(articulo) #se agrega a la lista privada
        self.sumar_puntos(articulo)

    def sumar_puntos(self, articulo):
        self.puntaje += articulo.puntos

    def restar_puntos(self, articulo):
        self.puntaje -= articulo.puntos
        
    def obtener_articulos_comprados(self):
        return self.__articulos_comprados
    
    def imprimir_articulos_comprados(self):
        for articulo in self.__articulos_comprados:
            print(f"ID: {articulo.identificador}, Nombre: {articulo.nombre}, Descripción: {articulo.descripcion}, Marca: {articulo.marca}, Precio: {articulo.precio}, Puntos: {articulo.puntos}") 
    
    def imprimir_puntaje(self):
        print(f"El puntaje total de {self.nombre} es de: {self.puntaje}")
#2.2        
    def encontrar_articulo(self, identificador_articulo):
        encontrado = False
        for articulo in self.__articulos_comprados:
            if articulo.identificador == identificador_articulo:
                print(f"Articulo encontrado : {articulo.nombre}")
                encontrado = True
        if not encontrado:
            print(f"Articulo no encontrado: {articulo.nombre}")
        return encontrado
#2.3   
    def eliminar_articulo(self, identificador_articulo):
        articulos_a_eliminar = [articulo for articulo in self.__articulos_comprados if articulo.id == identificador_articulo]
        if not articulos_a_eliminar:
            print("Articulo no encontrado en la lista.")
            return False
        
        for articulo in articulos_a_eliminar:
            self.__articulos_comprados.remove(articulo)
            self.restar_puntos(articulo)
            print(f"Articulo eliminado: {articulo.nombre}")
            
        return True
    

