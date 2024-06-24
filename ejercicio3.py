from ejercicio1 import Articulos
from ejercicio2 import Comprador

#3.4
# creacion de Nodo y Lista Enlazada
class Nodo:
    def __init__(self, articulo):
        self.articulo = articulo
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_al_final(self, articulo):
        nuevo_nodo = Nodo(articulo)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
#metodo para ver si hay dos articulos con los mismo puntos    
def hay_dos_articulos_con_mismo_puntaje(lista_enlazada):
    if lista_enlazada.esta_vacia():
        return False
    puntajes_vistos = set()
    actual = lista_enlazada.cabeza
    while actual:
        puntaje_actual = actual.articulo.puntos
        if puntaje_actual in puntajes_vistos:
            return True
        puntajes_vistos.add(puntaje_actual)
        actual = actual.siguiente
    return False
    
lista_enlazada_articulos = ListaEnlazada()

#3.1
#Compradores
juan = Comprador("Juan Perez", "Av.Corrientes 1234", "1536690663", "31-01-1992", 0)
marcos = Comprador("Marcos Testuri", "Av.Brown 7644", "1524678946", "04-03-1992", 0)
osvaldo = Comprador("Osvaldo Niz", "Av.Policastro 434", "1567197439", "12-05-1960", 0)
teresa = Comprador("Teresa Naranjo", "Av.Juncal 2779", "42398000", "13-09-1980", 0)
milagros = Comprador("Milagros Peña", "Garibaldi 234", "1546731597", "10-02-1978", 0)
karina = Comprador("Karina Rubin", "Av.Belgrano 51234", "1549743566", "28-12-1995", 0)


#Articulos
bizcocho = Articulos(1, "bizcocho", "bocadillos salados de grasa", "Don Satur", 750.5, 20)
manteca = Articulos(2, "manteca", "es una emulsión del batido, amasado y lavado de grasas lácteas y agua", "La Paulina", 2000.0, 35)
leche = Articulos(3, "leche", "leche de vaca contenta", "Armonia", 2500.5, 42)
medialunas = Articulos(4, "medialunas", "una masa hojaldrada fermentada típicamente francesa", "Del Abuelo", 3500.0, 65)
cafe = Articulos(5, "cafe", "Hay cafe cafe", "La Morenita", 5550.5, 80)
canoncito = Articulos(6, "canoncito", "son una variedad de facturas y bizcochos hechas con masa de hojaldre horneada rellena de dulce de leche", "La Romana", 750.5, 10)


#Modo prueba
juan.comprar_articulo(bizcocho)
marcos.comprar_articulo(medialunas)
osvaldo.comprar_articulo(cafe)
milagros.comprar_articulo(leche)
teresa.comprar_articulo(leche)
teresa.comprar_articulo(manteca)
karina.comprar_articulo(canoncito)

#3.2
#creo la lista de compradores
lista_compradores = [juan, marcos, osvaldo, teresa, milagros, karina]

#3.3
#para ordenar la lista compradores
def ordenar_compradores_por_puntaje(compradores):
    n = len(compradores)
    for i in range(n):
        for j in range(0, n-i-1):
            if compradores[j].puntaje < compradores[j+1].puntaje:
                compradores[j], compradores[j+1] = compradores[j+1], compradores[j]


ordenar_compradores_por_puntaje(lista_compradores)


for comprador in lista_compradores:
    print(f"Nombre: {comprador.nombre}, Puntaje: {comprador.puntaje}")


lista_enlazada_articulos.insertar_al_final(bizcocho)
lista_enlazada_articulos.insertar_al_final(manteca)
lista_enlazada_articulos.insertar_al_final(leche)
lista_enlazada_articulos.insertar_al_final(medialunas)
lista_enlazada_articulos.insertar_al_final(cafe)
lista_enlazada_articulos.insertar_al_final(canoncito)


# Se verifica si hay dos artículos con la misma cantidad de puntos en la lista enlazada
hay_mismo_puntaje = hay_dos_articulos_con_mismo_puntaje(lista_enlazada_articulos)

if hay_mismo_puntaje:
    print("Hay dos artículos con la misma cantidad de puntos.")
else:
    print("No hay dos artículos con la misma cantidad de puntos.")


""" banco de pruebas
juan.imprimir_articulos_comprados()
juan.imprimir_puntaje()

marcos.imprimir_articulos_comprados()
marcos.imprimir_puntaje()

osvaldo.imprimir_articulos_comprados()
osvaldo.imprimir_puntaje()

milagros.imprimir_articulos_comprados()
milagros.imprimir_puntaje()

teresa.imprimir_articulos_comprados()
teresa.imprimir_puntaje()

karina.imprimir_articulos_comprados()
karina.imprimir_puntaje()
"""

