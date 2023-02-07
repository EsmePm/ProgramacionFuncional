from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

# Ambiente virutal
# operaciones sobre conjuntos
# Generadores
# list comprenhensions
# dictionary comprenhensions
# set comprenhensions
# Iteradores
# iterables de transfomración y reducción 
# pipelines
# MyPy
# Type Hint
# Inmutabilidad
# Funciones Lambda
# Cierrres
# fuctor aplication
# monada

client_id = "01f2938c5262491da9b4ccfc11aea077"
client_secret = "978c8f2e99f84ad99a7f9f13ac59a3fa"
sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id, client_secret))

def generador(genre:str)->list:
    result = sp.search(q = 'genre' + genre, limit = 20)
    aux = []
    for i in range(len(result["tracks"]["items"])):
        aux.append(result["tracks"]["items"][i]["name"])
    return aux
    
if __name__ == '__main__':
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id, client_secret))
    generos= ["Banda", "Rock", "Electronica"]
    canciones = []
    for i in generos:
        canciones.append(generador(i))
    final= tuple(zip(generos, canciones))
    print(final)


# def dif(a:str, u:str):
#     b = sp.search(a, limit=10)
#     for i in range(len(b["tracks"]["items"])):
#         yield [0, (b["tracks"]["items"][i]["name"])]
    
#     response = sp.artist_top_tracks(u)
#     for track in response['tracks']:
#         yield [1, (track['name'])]

# urn = 'spotify:artist:2nszmSgqreHSdJA3zWPyrW'
# c1 = set()
# c2 = set()  
# for i in dif('Luis Miguel', urn):
#     if i[0] == 0:
#         c1.add(i[1])
#     else:
#         c2.add(i[1])
# # print(c1)
# # print(c2)
# c3 = c2.symmetric_difference(c2.intersection(c1))
# print(c3)