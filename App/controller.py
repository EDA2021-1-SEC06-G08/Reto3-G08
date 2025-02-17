﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ===========================
# Inicializacion del catalogo
# ===========================


def initCatalog():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


# ================================
# FUNCIONES PARA LA CARGA DE DATOS
# ================================


def loadData(catalog):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    loadVideosContext(catalog)

def loadVideosInfo(catalog):
    """
    Carga los datos de user_track
    """
    videosfile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(videosfile))
    for video in input_file:
        model.addVideoInfo(catalog, video)

def loadVideosContext(catalog):
    """
    Carga los datos de context_content
    """
    videosfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(videosfile))
    model.CrearLlaveMusicaContext(catalog)
    model.CrearLlaveMusicaGenero(catalog)
    for musica in input_file:
        model.addMusicaContext(catalog, musica)
        model.addMapMusicaContext(catalog, musica)
        model.addMapMusicaGenero(catalog, musica)
        model.addMapMusicaFechas(catalog, musica)

def loadVideosEtiquetas(catalog):
    """
    Carga los datos de sentiment_values
    """
    videofile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(videofile))
    for video in input_file:
        model.addVideoEtiquetas(catalog, video)


# ========================
# Funciones para consultas
# ========================


#requerimiento 1

def carac_reproducciones(caracteristica, valor_min, valor_max, catalog):
    """
    Obtiene la informacion del requerimiento 1
    """
    return model.carac_reproducciones(caracteristica, valor_min, valor_max, catalog)
    

#requerimiento 2 

def requerimiento2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog):
    """
    Obtiene la informacion del requerimiento 2
    """

    return model.musica_req2(valor_minEnergy, valor_maxEnergy, valor_minDanceability, valor_maxDanceability, catalog)


#requerimiento 3

def requerimiento3(valor_minTempo, valor_maxTempo, valor_minInstrumentalness, valor_maxInstrumentalness, catalog):
    """
    Obtiene la informacion del requerimiento 3
    """

    return model.musica_req3(valor_minTempo, valor_maxTempo, valor_minInstrumentalness, valor_maxInstrumentalness, catalog)

#requerimiento 4

def requerimiento4NewGenero(tempomin, tempomax, catalog):
    """
    Da el resultado para un genero nuevo
    """
   
    return model.buscar_Newgenero(tempomin, tempomax, catalog)

def requerimiento4(catalog, generos):
    """
    Da el resultado para los generos existentes
    """
    

    return model.generos_existentes(catalog, generos)



#requerimiento 5
def requerimiento5(catalog, valor_minHora, valor_maxHora):
    return model.genero_escuchados(catalog, valor_minHora, valor_maxHora) 


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
