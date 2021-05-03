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
from DISClib.DataStructures import listiterator as it
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
    Lista = ['instrumentalness' , 'liveness' , 'speechiness' , 'danceability' , 'valence' ,
             'loudness' , 'tempo' , 'acousticness' , 'energy']
 
    for contenido in Lista:
        mp.put(catalog['caraContenido'], contenido, om.newMap('RBT'))

def addVideoContext(catalog, musica):
    """
    """
    lt.addLast(catalog['videosContext'], musica)
    #print(catalog['videosContext'])
    #Instrumentalness
    RBTinstrumentalnessEntry = mp.get(catalog['caraContenido'], 'instrumentalness')
    RBTinstrumentalness = me.getValue(RBTinstrumentalnessEntry)    
    print(RBTinstrumentalness)    
    EstaKey = om.contains(RBTinstrumentalness, musica['instrumentalness'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTinstrumentalness, musica['instrumentalness'], ArtistList)
        ListaArtistaEntry = om.get(RBTinstrumentalness, musica['instrumentalness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTinstrumentalness, musica['instrumentalness'], ListaArtista)
        listaEntry = om.get(RBTinstrumentalness, musica['instrumentalness'])
        lista = me.getValue(listaEntry)
        #print(lista)
        mp.put(catalog['caraContenido'], 'instrumentalness', RBTinstrumentalness)
    else:
        ListaArtistaEntry = om.get(RBTinstrumentalness, musica['instrumentalness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTinstrumentalness, musica['instrumentalness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'instrumentalness', RBTinstrumentalness)
        #print(ListaArtista)

    #Liveness
    RBTlivenessEntry = mp.get(catalog['caraContenido'], 'liveness')
    RBTliveness = me.getValue(RBTlivenessEntry)
    EstaKey = om.contains(RBTliveness, musica['liveness'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTliveness, musica['liveness'], ArtistList)
        ListaArtistaEntry = om.get(RBTliveness, musica['liveness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTliveness, musica['liveness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'liveness', RBTliveness)
    else:
        ListaArtistaEntry = om.get(RBTliveness, musica['liveness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTliveness, musica['liveness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'liveness', RBTliveness)

    #Speechiness
    RBTspeechinessEntry = mp.get(catalog['caraContenido'], 'speechiness')
    RBTspeechiness = me.getValue(RBTspeechinessEntry)
    EstaKey = om.contains(RBTspeechiness, musica['speechiness'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTspeechiness, musica['speechiness'], ArtistList)
        ListaArtistaEntry = om.get(RBTspeechiness, musica['speechiness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTspeechiness, musica['speechiness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'speechiness', RBTspeechiness)
    else:
        ListaArtistaEntry = om.get(RBTspeechiness, musica['speechiness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTspeechiness, musica['speechiness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'speechiness', RBTspeechiness)
 
    #Danceability
    RBTdanceabilityEntry = mp.get(catalog['caraContenido'], 'danceability')
    RBTdanceability = me.getValue(RBTdanceabilityEntry)
    EstaKey = om.contains(RBTdanceability, musica['danceability'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTdanceability, musica['danceability'], ArtistList)
        ListaArtistaEntry = om.get(RBTdanceability, musica['danceability'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTdanceability, musica['danceability'], ListaArtista)
        mp.put(catalog['caraContenido'], 'danceability', RBTdanceability)
    else:
        ListaArtistaEntry = om.get(RBTdanceability, musica['danceability'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTdanceability, musica['danceability'], ListaArtista)
        mp.put(catalog['caraContenido'], 'danceability', RBTdanceability)

    #Valence
    RBTvalenceEntry = mp.get(catalog['caraContenido'], 'valence')
    RBTvalence = me.getValue(RBTvalenceEntry)
    EstaKey = om.contains(RBTvalence, musica['valence'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTvalence, musica['valence'], ArtistList)
        ListaArtistaEntry = om.get(RBTvalence, musica['valence'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTvalence, musica['valence'], ListaArtista)
        mp.put(catalog['caraContenido'], 'valence', RBTvalence)
    else:
        ListaArtistaEntry = om.get(RBTvalence, musica['valence'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTvalence, musica['valence'], ListaArtista)
        mp.put(catalog['caraContenido'], 'valence', RBTvalence)

    #Acousticness
    RBTacousticnessEntry = mp.get(catalog['caraContenido'], 'acousticness')
    RBTacousticness = me.getValue(RBTacousticnessEntry)
    EstaKey = om.contains(RBTacousticness, musica['acousticness'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTacousticness, musica['acousticness'], ArtistList)
        ListaArtistaEntry = om.get(RBTacousticness, musica['acousticness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTacousticness, musica['acousticness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'acousticness', RBTacousticness)
    else:
        ListaArtistaEntry = om.get(RBTacousticness, musica['acousticness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTacousticness, musica['acousticness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'acousticness', RBTacousticness)

    #Energy
    RBTenergyEntry = mp.get(catalog['caraContenido'], 'energy')
    RBTenergy = me.getValue(RBTenergyEntry)
    EstaKey = om.contains(RBTenergy, musica['energy'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTenergy, musica['energy'], ArtistList)
        ListaArtistaEntry = om.get(RBTenergy, musica['energy'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTenergy, musica['energy'], ListaArtista)
        mp.put(catalog['caraContenido'], 'energy', RBTenergy)
    else:
        ListaArtistaEntry = om.get(RBTenergy, musica['energy'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTenergy, musica['energy'], ListaArtista)
        mp.put(catalog['caraContenido'], 'energy', RBTenergy)

    #Tempo
    RBTtempoEntry = mp.get(catalog['caraContenido'], 'tempo')
    RBTtempo = me.getValue(RBTtempoEntry)        
    EstaKey = om.contains(RBTtempo, musica['tempo'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTtempo, musica['tempo'], ArtistList)
        ListaArtistaEntry = om.get(RBTtempo, musica['tempo'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTtempo, musica['tempo'], ListaArtista)
        mp.put(catalog['caraContenido'], 'tempo', RBTtempo)
    else:
        ListaArtistaEntry = om.get(RBTtempo, musica['tempo'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTtempo, musica['tempo'], ListaArtista)
        mp.put(catalog['caraContenido'], 'tempo', RBTtempo)

    #Loudness
    RBTloudnessEntry = mp.get(catalog['caraContenido'], 'loudness')
    RBTloudness = me.getValue(RBTloudnessEntry)        
    EstaKey = om.contains(RBTloudness, musica['loudness'])

    if not(EstaKey):
        ArtistList = lt.newList('SINGLE_LINKED')
        om.put(RBTloudness, musica['loudness'], ArtistList)
        ListaArtistaEntry = om.get(RBTloudness, musica['loudness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTloudness, musica['loudness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'loudness', RBTloudness)
    else:
        ListaArtistaEntry = om.get(RBTloudness, musica['loudness'])
        ListaArtista = me.getValue(ListaArtistaEntry)
        lt.addLast(ListaArtista, musica)
        om.put(RBTloudness, musica['loudness'], ListaArtista)
        mp.put(catalog['caraContenido'], 'loudness', RBTloudness)


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

#requerimiento 1 
def carac_reproducciones(caracteristica, valor_min, valor_max, catalog):
    artistasRepetidos = lt.newList('ARRAY_LIST')
    artistasUnicos = set()
    entry = mp.get(catalog['caraContenido'], caracteristica)
    arbol = me.getValue(entry)
    lista_llaves = om.keys(arbol, valor_min, valor_max)
    lista_artistas = om.values(arbol, valor_min, valor_max)
    iterador = it.newIterator(lista_artistas)
    while it.hasNext(iterador):  
      artist_id = it.next(iterador)
      for elemento in artist_id['elements']:
          if elemento not in artistasRepetidos:
              lt.addLast(artistasRepetidos, elemento)
    iterador2 = it.newIterator(artistasRepetidos)
    while it.hasNext(iterador2):  
      artist_id2 = it.next(iterador2)
      if artist_id2 not in artistasUnicos:
          artistasUnicos.add(artist_id2)
    return lt.size(artistasRepetidos), len(artistasUnicos)


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


