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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ===========================
# Inicializacion del catalogo
# ===========================


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# =================================================
# Funciones para la carga de datos y almacenamiento
# de datos en los modelos
# =================================================

def loadData(analyzer, videosfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    videosfile = cf.data_dir + videosfile
    input_file = csv.DictReader(open(videosfile, encoding="utf-8"),
                                delimiter=",")
    for video in input_file:
        model.addVideo(analyzer, video)
    return analyzer

# ========================
# Funciones para consultas
# ========================


def videosSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.videosSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
