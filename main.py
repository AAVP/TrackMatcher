import pandas as pd
import sys
from musixmatch_api import *
from emotion_predictor import *
df = pd.read_csv("slim-2.csv")

terminado = False
while not terminado:
    print()
    print("SONGS & LYRICS")
    print("[1] Buscar")
    print("[2] Descubrir")
    print("[3] Salir del programa")
    menu_principal = int(input())
    if menu_principal == 1:
        print()
        print("[1] Buscar cancion")
        print("[2] Buscar recomendiación por género")
        submenu = int(input())
        if submenu == 1:
            print()
            print("Buscar canción por: ")
            print("[1] Título y Artista")
            print("[2] Letra")
            print("[3] Sentimientos de la canción (en desarrollo)")
            submenu_1 = int(input())
            if submenu_1 == 1:
                print()
                titulo = input("Título de la canción: ")
                artista = input("Artista: ")
                music_matcher(
                    {
                        'by_lyrics': False,
                        'track': titulo,
                        'artist': artista
                    }
                )
            elif submenu_1 == 2:
                print()
                titulo = input("Letra de la canción: ")
                artista = input("Escribe el nombre del artista. Si no te sabes el nombre del artista, escribe None: ")
                if artista != "None":
                    music_matcher(
                        {
                            'by_lyrics': True,
                            "artist": artista,
                            'lyrics': titulo
                        }
                    )
                else:
                    music_matcher(
                        {
                            'by_lyrics': True,
                            "artist": None,
                            'lyrics': titulo
                        }
                    )
            elif submenu_1 == 3:
                print()
                letra = input("Ingrese la letra que desea encontrar el sentimiento: ")
                for emotion, percentage in predict_emotion(letra).items():
                    print(f'{emotion}: {percentage}')
            else:
                print()
                print("Oops, ocurrió un error. Intenta nuevamente.")
        elif submenu == 2:
            print()
            genero = input("Escribe tu genero: ")
            recommendations_genre(
                {
                'top': '10',
                'genre': genero
                }
            )
    elif menu_principal == 2:
        print()
        print("Descubrir Top Charts de:")
        print("[1] Canciones")
        print("[2] Artistas")
        submenu_2 = int(input())
        x = input("País: ")
        print()
        print("[1] Top 100")
        print("[2] Top 25")
        print("[3] Top 10")
        top_charts = int(input())
        if top_charts == 1:
            top = "100"
        elif top_charts == 2:
            top = "25"
        elif top_charts == 3:
            top = "10"
        else:
            print()
            print("Oops, ocurrió un error. Intente nuevamente.")
        iso_3166 = df.drop("country-code", axis = 1)
        iso_3166.columns = ["Nombre", "Código"]
        iso_3166.set_index("Nombre", inplace=True)
        fila = iso_3166.loc[x]
        país = fila["Código"]
        if submenu_2 == 1:
            print()
            top_tracks(
                {
                    'top': top,
                    'country': país,
                }
            )
        elif submenu_2 == 2:
            print()
            top_artists(
            {
                'top': top,
                'country': país
            }
            )
        else:
            print()
            print("Oops, parece que ocurrió un error")
    elif menu_principal == 3:
        print()
        print("Gracias por utilizar SONGS & LYRICS")
        sys.exit()
    else:
        print()
        print("Oops, parece que ocurrió un error")