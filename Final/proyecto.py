from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth # type: ignore
import spotipy # type: ignore

client_id = "01f2938c5262491da9b4ccfc11aea077"
client_secret = "978c8f2e99f84ad99a7f9f13ac59a3fa"
sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id, client_secret))

def dif(a:str, u:str)-> list:
    b = sp.search(a, limit=10)
    lista = list(map(lambda x: [0, x["name"]], b["tracks"]["items"]))
    
    response = sp.artist_top_tracks(u)
    lista += list(map(lambda x: [1, x["name"]], response["tracks"]))
    return lista

if __name__ == '__main__':
    urn = 'spotify:artist:2nszmSgqreHSdJA3zWPyrW'
    c1 = set()
    c2 = set()
    lista2 = dif('Luis Miguel', urn)
    c1 = {x[1] for x in filter(lambda x: x[0] == 0, lista2)}
    c2 = {x[1] for x in filter(lambda x: x[0] != 0, lista2)}
    # print(c1)
    # print(c2)
    c3 = c2.symmetric_difference(c2.intersection(c1))
    print(c3)