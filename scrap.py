import requests
from bs4 import BeautifulSoup
import threading
import time

tiempo = time.time()
archivoMetacritic = "/Users/luiss/Desktop/Scrap/Metacritic.txt"
archivoPlayStation = "/Users/luiss/Desktop/Scrap/PlayStationStore.txt"


def extraerDatosMetacritic():
    url = 'https://www.metacritic.com/browse/games/release-date/available/pc/metascore'
    url1 = 'https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=1'
    url2 = 'https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=2'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    cont1 = 0
    cont = 0
    while (cont1<= 2):
        if(cont1 == 1):
            response = requests.get(url1, headers=user_agent)
            soup = BeautifulSoup(response.text, 'html.parser')
            cont = 0
        elif (cont1 == 2):
            response = requests.get(url2, headers=user_agent)
            soup = BeautifulSoup(response.text, 'html.parser')
            cont = 0
        else:
            response = requests.get(url, headers=user_agent)
            soup = BeautifulSoup(response.text, 'html.parser')

        archivo = open(archivoMetacritic, 'w')

        while (cont <= 99):
            print("\n\n***************Metacritic*****************")
            nombre = soup.find_all('a', class_=['title'])[cont].text
            print('JUEGO: ' + nombre)

            metascore = soup.find_all('div', class_=['clamp-score-wrap'])[cont].text
            print('\nMETASCORE: ' + metascore)

            archivo.write("Nombre del juego: " + nombre + "\nMetascore: " + metascore)
            cont += 1
        archivo.close()

        cont1 += 1



def extraerDatosPlayStationStore():
    url = 'https://store.playstation.com/es-cr/grid/STORE-MSF77008-NEWGAMESGRID/1'
    user_agent = {'User-agent': 'Google Chrome'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')

    archivo = open(archivoPlayStation, 'w')

    cont = 0
    while (cont <= 10):
        archivo.write("\n\n***************PlayStationStore*****************")
        print("\n\n***************PlayStationStore*****************")
        nombre = soup.find_all('div', class_=['grid-cell__title'])[cont].text
        print('JUEGO: ' + nombre)

        precio = soup.find_all('h3', class_=['price-display__price'])[cont].text
        print('\nPRECIO: ' + precio)

        archivo.write("\nNombre del juego: " + nombre + "\nPrecio: " + precio+"\n")
        cont += 1
    archivo.close()



def extraerDatosSteam():
    url = 'https://store.steampowered.com/games/'
    user_agent = {'User-agent': 'Google Chrome'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')

    cont = 0
    while (cont <= 31):
        print("\n\n***************Steam*****************")
        nombre = soup.find_all('div', class_=['tab_item_name'])[cont].text
        print("Nombre: "+nombre)

        precioRebajado = soup.find_all('div', class_=['discount_final_price'])[cont].text

        if (precioRebajado == "Free to Play"):
            print("Precio final: "+precioRebajado)
        else:
            precio = soup.find_all('div', class_=['discount_original_price'])[cont].text
            descuento = soup.find_all('div', class_=['discount_pct'])[cont].text
            print("Precio original: "+precio+" "+descuento+"\n"
                  "Precio final: "+precioRebajado)

        cont += 1



def extraerDatosU_Play():
    url = 'https://store.ubi.com/ofertas/juegos/?lang=es_CR'
    user_agent = {'User-agent': 'Google Chrome'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')

    nombre = soup.find_all('div', class_=['card-title'])[0].text
    print("Nombre: " + nombre)

    precio = soup.find_all('div', class_=['card-price'])[5].text
    print("Precio: " + precio)



"""
hilo1 = threading.Thread(target=extraerDatosMetacritic)
hilo2 = threading.Thread(target=extraerDatosPlayStationStore)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
"""
extraerDatosMetacritic()
#extraerDatosPlayStationStore()
#extraerDatosSteam()
#extraerDatosU_Play()

tiempoTranscurrido = time.time() - tiempo
print("Tiempo transcurrido "+ str(tiempoTranscurrido))
