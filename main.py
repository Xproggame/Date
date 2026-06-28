import random
from io import text_encoding
from random import *
import codecs

ran = Random()

while True:
    fichier = input("Quel fichier voulez-vous ouvrir ? [nom de la feuille de dates] > " )
    with codecs.open(f'{fichier}.txt', encoding='utf-8') as file:
        list_date = []

        for line in file.read().split('\r\n'):
            date = line.split(':')
            list_date.append(date)

        place = 1
        place_q = 0

        if input("Voulez vous réviser les dates ou les évènement [1 ou 2] > ") == '2':
            place = 0
            place_q = 1

        ran.shuffle(list_date)

        for element in list_date:

            if element[place] == input(f"{element[place_q]} > "):
                print("oui")

            else:
                print(f"Mauvaise réponse. Bonne réponse : {element[place]}")