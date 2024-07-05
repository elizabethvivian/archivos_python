# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---
    
    with open("alturas.csv") as csvfile:
        # Leer todos los datos y almacenarlos en una 
        # lista de diccionarios
        personas = list(csv.DictReader(csvfile))
    suma_altura = 0
    cantidad_personas = 0
    
    #for i in range(len(personas)):
    #    if personas[i]["genero"] == genero:
    #       suma_altura += float(personas[i]["altura"])
    #      cantidad_personas += 1
    for persona in personas:
        if persona["genero"] == genero:
            suma_altura += float(persona["altura"])
            cantidad_personas += 1
    
    promedio = suma_altura / cantidad_personas
    
    print(f"Cantidad de personas de genero {genero}:{cantidad_personas}")
    print(f"Altura promedio del genero {genero}:{promedio}")  


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
