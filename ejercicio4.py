from ejercicio2 import Comprador
from ejercicio3 import ListaEnlazada
from ejercicio3 import lista_compradores
from ejercicio1 import Articulos

import csv
#4.1

def lista_a_string(self):
        lista_strings = []
        for articulo in self.__articulos_comprados:
            articulo_str = f"{articulo.identificador}; \"{articulo.nombre}\"; \"{articulo.marca}\"; {articulo.precio:.2f}; {articulo.puntos}"
            lista_strings.append(articulo_str)
        return lista_strings
#4.2
def generar_archivos_csv(compradores):
    for comprador in compradores:
        nombre_archivo = f"{comprador.nombre}.csv"
        with open(nombre_archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Identificador", "Nombre", "Marca", "Precio", "Puntos"])
            for articulo in comprador.obtener_articulos_comprados():
                writer.writerow([articulo.identificador, articulo.nombre, articulo.marca, articulo.precio, articulo.puntos])
        print(f"Archivo {nombre_archivo} generado exitosamente.")

# Uso de la función para generar archivos CSV
generar_archivos_csv(lista_compradores)