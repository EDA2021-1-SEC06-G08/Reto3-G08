﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def printMenu():
    print("\n")
    print("=======================================")
    print("Bienvenido")
    print("1- Cargar información de la musica")
    print("2- Caracterizar las reproducciones")
    print("3- Encontrar musica para festejar")
    print("4- Encontrar musica para estudiar")
    print("5- Estudiar los generos musicales")
    print("6- Indicar el genero musical mas escuchado en el tiempo")
    print("0- Salir")
    print("=======================================")

def initCatalog():
    """
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nCargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        """
        print('Videos cargados: ' + str(controller.videosSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        """
    elif int(inputs[0]) == 2:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 3:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 4:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 5:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 6:
        print("\nCargando información de los videos ....")
    else:
        sys.exit(0)
sys.exit(0)
