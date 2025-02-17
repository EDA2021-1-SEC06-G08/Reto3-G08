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

import random
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
#====
#Menu
#====

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
    artistasNoRepetidos = lt.newList('ARRAY_LIST')
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
    cancionesNoRepetidas = lt.newList('ARRAY_LIST')
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
    Contiene las funciones auxiliares del desarrolllo parte 2
    """
    print("La cantidad de eventos escuchados es: " + str(lt.size(catalog['videosContext'])))
    artista_unico(catalog)
    canciones_unicas(catalog)
    losCincos(catalog)


#=========================
#Solucion de requerimiento
#=========================

#requerimiento 1

def requerimiento1(caracteristica, valor_min, valor_max, catalog):
    """
    LLama la funcion del requerimiento 1 del controller
    """
    return controller.carac_reproducciones(caracteristica, valor_min, valor_max, catalog)

#requerimiento 2

def requerimiento2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog):
    """
    LLama la funcion del requerimiento 2 del controller
    """
    return controller.requerimiento2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog)

def organizar_req2(lista):
    """
    Organiza el total y el valor de informacion de la musica
    """
    i = 1
    while i <= 5:
        intRandom = random.randint(0, int(lt.size(lista))-1)
        track = lt.getElement(lista, intRandom)
        print("Track" + ' ' + str(intRandom) + ' :' + ' ' + str(track['track_id']) + ' with energy of '
              + str(track['energy']) + ' and danceability of ' + str(track['danceability']))
        i += 1

#requerimiento 3

def requerimiento3(valor_minTempo, valor_maxTempo, valor_minInstrumentalness, valor_maxInstrumentalness, catalog):
    """
    LLama la funcion del requerimiento 3 del controller
    """
    return controller.requerimiento3(valor_minTempo, valor_maxTempo, valor_minInstrumentalness, valor_maxInstrumentalness, catalog)

def organizar_req3(lista):
    """
    Organiza el total y el valor de informacion de la musica
    """
    print('Total of unique tracks in events: ' + str(lt.size(lista[1])))
    i = 1
    while i <= 5:
        intRandom = random.randint(0, int(lt.size(lista[0]))-1)
        track = lt.getElement(lista[0], intRandom)
        print("Track" + ' ' + str(intRandom) + ' :' + ' ' + str(track['track_id']) + ' with tempo of '
              + str(track['tempo']) + ' and instrumentalness of ' + str(track['instrumentalness']))
        i += 1

#requerimiento 4

def requerimiento4NewGenero(tempomin, tempomax, catalog):
    """
    Da una tupla que contiene la cantidad de reproducciones para el genero y la lista con los autores
    """
    return controller.requerimiento4NewGenero(tempomin, tempomax, catalog)

def requerimiento4(catalog, generos):
    """
    Regresa en modo print la informacion
    """
    return controller.requerimiento4(catalog, generos)

#requerimiento 5

def requerimiento5(catalog, valor_minHora, valor_maxHora):
    """
    """
    return controller.requerimiento5(catalog, valor_minHora, valor_maxHora)

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
    elif int(inputs[0]) == 2: #Da los resultados de la parte 2 del desarrollo
        print("\nCargando información de los videos ....")
        desarrollo(catalog)
    elif int(inputs[0]) == 3: #requerimiento 1
        caracteristica = input('Inserte la característica: ')
        valor_min = input('Inserte el valor mínimo: ')
        valor_max = input('Inserte el valor máximo: ')
        print("\nCargando información de los videos ....")
        respuesta = requerimiento1(caracteristica, valor_min, valor_max, catalog)
        print(str(caracteristica) + ' ' + 'is between' + ' ' + str(valor_min) + ' ' + 'and' + ' ' + str(valor_max))
        print('Total of reproduction: ' + str(respuesta[0]) + ' ' + 'Total of unique artists: ' + str(respuesta[1]))
    elif int(inputs[0]) == 4: #requerimiento 2 
        valor_minEnergy = input('Inserte el valor mínimo de Energy: ')
        valor_maxEnergy = input('Inserte el valor máximo de Energy: ')
        valor_minDanceability = input('Inserte el valor mínimo de Danceability: ')
        valor_maxDanceability = input('Inserte el valor máximo de Danceability: ')
        print("\nCargando información de los videos ....")
        respuesta = requerimiento2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog)
        print('Total of unique tracks in events: ' + str(lt.size(respuesta[0])))
        organizar_req2(respuesta[1])

    elif int(inputs[0]) == 5: #requerimiento 3 
        valor_minTempo = input('Inserte el valor mínimo de Tempo: ')
        valor_maxTempo = input('Inserte el valor máximo de Tempo: ')
        valor_minInstrumentalness = input('Inserte el valor mínimo de Instrumentalness: ')
        valor_maxInstrumentalness = input('Inserte el valor máximo de Instrumentalness: ')
        print("\nCargando información de los videos ....")
        respuesta = requerimiento3(valor_minTempo, valor_maxTempo, valor_minInstrumentalness, valor_maxInstrumentalness, catalog)
        organizar_req3(respuesta)
       
    elif int(inputs[0]) == 6: #requerimiento 4
        while True:
            inputz = input("Introduzca 0 si quiere salir, 1 si quiere buscar un nuevo genero o 2 si quiere buscar algun genero existente: ")
            if int(inputz[0]) == 1:
                genero = input("Introduzca el genero: ")
                valor_min = input("Introduzca el tempo minimo: ")
                valor_max = input("Introduzca el tempo maximo: ")
                print("\nCargando información de los videos ....")
                respuesta = requerimiento4NewGenero(valor_min, valor_max, catalog)
                #respuesta = controller.requerimiento4NewGenero(valor_min, valor_max, catalog)
                print(str(genero) + ' is between ' + str(valor_min) + ' and ' + str(valor_max))
                print('Total of reproduction: ' + str(lt.size(respuesta[0])) + ' Total of unique artists: ' + str(lt.size(respuesta[1])))
                print('---------------  Some artists for ' + str(genero) + ' -----------')
                i = 0
                while i <= 9:
                    print('Artist ' + str(i) + ': ' + lt.getElement(respuesta[1], i))
                    i += 1
            
            elif int(inputz[0]) == 2:
                generos = input("Introduzca los generos pegados y separado por comas: ")
                print("\nCargando información de los videos ....")
                respuesta = controller.requerimiento4(catalog, generos)
                print(respuesta)
            else:
                sys.exit(0)

    elif int(inputs[0]) == 7:
        valor_minHora = input('Ingrese la fecha hh:mm:ss minima de busqueda: ')
        valor_maxHora = input('Ingrese la fecha hh:mm:ss maxima de busqueda: ')
        print("\nCargando información de los videos ....")
        requerimiento5(catalog, valor_minHora, valor_maxHora)
    else:
        sys.exit(0)
sys.exit(0)