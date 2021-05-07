"""
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
from DISClib.DataStructures import listiterator as it
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
    print("2- Datos interesantes")
    print("3- Caracterizar las reproducciones")
    print("4- Encontrar musica para festejar")
    print("5- Encontrar musica para estudiar")
    print("6- Estudiar los generos musicales")
    print("7- Indicar el genero musical mas escuchado en el tiempo")
    print("0- Salir")
    print("=======================================")

#===========================
#IMPLEMENTACION DEL CATALOGO
#===========================

def initCatalog():
    """
    Inicializa el catalogo de la musica
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


#===============================
#FUNCIONES DATOS DE LOS ARCHIVOS
#===============================

def artista_unico(catalog):
    """
    Da la cantidad de artistas unicos
    """
    artistasNoRepetidos = lt.newList('SINGLE_LINKED')
    iterator = it.newIterator(catalog['videosContext'])
    while it.hasNext(iterator):
        musica = it.next(iterator)
        if int(lt.isPresent(artistasNoRepetidos, musica['artist_id'])) == 0:
            lt.addLast(artistasNoRepetidos, musica['artist_id'])
    print("La cantidad de artistas unicos es: " +  str(lt.size(artistasNoRepetidos)))

def canciones_unicas(catalog):
    """
    Da la cantidad de canciones unicas
    """
    cancionesNoRepetidas = lt.newList('SINGLE_LINKED')
    iterator = it.newIterator(catalog['videosContext'])
    while it.hasNext(iterator):
        musica = it.next(iterator)
        if int(lt.isPresent(cancionesNoRepetidas, musica['track_id'])) == 0:
            lt.addLast(cancionesNoRepetidas, musica['track_id'])
    print("La cantidad de canciones unicas es: " +  str(lt.size(cancionesNoRepetidas)))

def losCincos(catalog):
    """
    Retorna los primeros 5 videos y los ultimos 5 videos
    """
    size = lt.size(catalog['videosContext'])
    i=0
    j=int(size)-5
    while i <= 4:
        musica = lt.getElement(catalog['videosContext'], i)
        print("\n=====================")
        print(musica) 
        print("\n=====================")
        i += 1
    
    while j <= (int(size)-1):
        musica = lt.getElement(catalog['videosContext'], j)
        print("\n=====================")
        print(musica) 
        print("\n=====================")
        j += 1

def desarrollo(catalog):
    """
    """
    print("La cantidad de eventos escuchados es: " + str(lt.size(catalog['videosContext'])))
    artista_unico(catalog)
    canciones_unicas(catalog)
    losCincos(catalog)


def organizar_req2(lista):
    print('Total of unique tracks in events: ', lt.size(lista))
    i = 1
    while i <= 5:
        track = lt.getElement(lista, i)
        print("Track", i, ':', track['track_id'], 'with energy of', track['energy'], 'and', 'danceability of', track['danceability'])
        i += 1

catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1: #Inicializa el catalogo y Mete los datos
        print("\nCargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
    if int(inputs[0]) == 2:
        print("\nCargando información de los archivos ....")
    elif int(inputs[0]) == 3:
        caracteristica = input('Inserte la característica: ')
        valor_min = input('Inserte el valor mínimo: ')
        valor_max = input('Inserte el valor máximo: ')
        respuesta = controller.carac_reproducciones(caracteristica, valor_min, valor_max, catalog)
        print("\nCargando información de los videos ....")
        print(caracteristica, 'is between', valor_min, 'and', valor_max)
        print('Total of reproduction: ',respuesta[0], 'Total of unique artists: ', respuesta[1])    
    elif int(inputs[0]) == 4:
        valor_minEnergy = input('Inserte el valor mínimo de Energy: ')
        valor_maxEnergy = input('Inserte el valor máximo de Energy: ')
        valor_minDanceability = input('Inserte el valor mínimo de Danceability: ')
        valor_maxDanceability = input('Inserte el valor máximo de Danceability: ')
        print("\nCargando información de los videos ....")
        respuesta = controller.requerimiento2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog)
        organizar_req2(respuesta)
    elif int(inputs[0]) == 5:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 6:
        print("\nCargando información de los videos ....")
    elif int(inputs[0]) == 7:
        print("\nCargando información de los videos ....")
    else:
        sys.exit(0)
sys.exit(0)
