"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

# ==============================
# API del TAD Catalogo de Videos
# ==============================


def newCatalog():
    """ 
    Inicializa el analizador

    Crea una lista vacia para guardar todos los videos
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    catalog = {'videosInfo': None,
               'videosContext': None,
               'videosEtiquetas': None,
               'caraContenido': None}

    catalog['videosInfo'] = lt.newList('SINGLE_LINKED', compareIds)
    catalog['videosContext'] = lt.newList('SINGLE_LINKED', compareIds)
    catalog['videosEtiquetas'] = lt.newList('SINGLE_LINKED', compareIds)
    catalog['caraContenido'] = mp.newMap(30,
                                            maptype='PROBING',
                                            loadfactor=0.4)

    return catalog



# ==============================================
# Funciones para agregar informacion al catalogo
# ==============================================


def addVideoInfo(catalog, video):
    """
    agrega un video a la lista de videos
    """
    lt.addLast(catalog['videosInfo'], video)
 

def CrearLlaveContext(catalog):
    """
    """
    Lista = ['instrumentalness' , 'liveness' , 'speechiness' , 'danceability' , 'valence' , 'loudness' , 'tempo' , 'acousticness' , 'energy']
 
    for contenido in Lista:
        mp.put(catalog['caraContenido'], contenido, om.newMap('RBT'))

def addVideoContext(catalog, musica):
    """
    """
    lt.addLast(catalog['videosContext'], musica)
    musica = list(musica)
    if musica[0] != 'instrumentalness':

        #Instrumentalness
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'instrumentalness')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[0])
        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[0], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[0])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[0], ListaArtista)
        mp.put(catalog['caraContenido'], 'instrumentalness', RBTinstrumeltaness)

        #Liveness
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'liveness')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[1])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[1], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[1])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[1], ListaArtista)
        mp.put(catalog['caraContenido'], 'liveness', RBTinstrumeltaness)

        #Speechiness
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'speechiness')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[2])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[2], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[2])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[2], ListaArtista)
        mp.put(catalog['caraContenido'], 'speechiness', RBTinstrumeltaness)
 
        #Danceability
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'danceability')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[3])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[3], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[3])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[3], ListaArtista)
        mp.put(catalog['caraContenido'], 'danceability', RBTinstrumeltaness)

        #Valence
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'valence')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[4])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[4], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[4])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[4], ListaArtista)
        mp.put(catalog['caraContenido'], 'valence', RBTinstrumeltaness)

        #Acousticness
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'Acousticness')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[7])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[7], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[7])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[7], ListaArtista)
        mp.put(catalog['caraContenido'], 'Acousticness', RBTinstrumeltaness)

        #Energy
        RBTinstrumeltaness = mp.get(catalog['caraContenido'], 'Energy')
        EstaKey = mp.contains(RBTinstrumeltaness, musica[8])

        if not(EstaKey):
            ArtistList = lt.newList('SINGLE_LINKED')
            om.put(RBTinstrumeltaness, musica[8], ArtistList)
        ListaArtista = om.get(RBTinstrumeltaness, musica[8])
        lt.addLast(ListaArtista, musica[11])
        om.put(RBTinstrumeltaness, musica[8], ListaArtista)
        mp.put(catalog['caraContenido'], 'energy', RBTinstrumeltaness)


def addVideoEtiquetas(catalog, video):
    """
    """
    lt.addLast(catalog['videosEtiquetas'], video)


def addMapCaraContenido(catalog, video):
    """
    """
    


def updateDateIndex(map, video):
    """
    Se toma la fecha del video y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de video
    y se actualiza el indice de tipos de video.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de videos
    """
    occurreddate = video['created_at']
    videodate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, videodate.date())
    if entry is None:
        datentry = newDataEntry(video)
        om.put(map, videodate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, video)
    return map

def addDateIndex(datentry, video):
    """
    Actualiza un indice de tipo de videos.  Este indice tiene una lista
    de videos y una tabla de hash cuya llave es el tipo de video y
    el valor es una lista con los videos de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstvideos']
    lt.addLast(lst, video)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, video['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        entry = newOffenseEntry(video['OFFENSE_CODE_GROUP'], video)
        lt.addLast(entry['lstoffenses'], video)
        m.put(offenseIndex, video['OFFENSE_CODE_GROUP'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], video)
    return datentry

def newDataEntry(video):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstvideos': None}
    entry['offenseIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['lstvideos'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newOffenseEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = lt.newList('SINGLELINKED', compareOffenses)
    return ofentry




# Funciones para creacion de datos

# ==============================
# Funciones de consulta
# ==============================


def videosSize(analyzer):
    """
    Número de videos
    """
    return lt.size(analyzer['videos'])

def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['dateIndex'])

def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['dateIndex'])

def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['dateIndex'])

def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['dateIndex'])



# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de videos
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1


