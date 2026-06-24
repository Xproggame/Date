import random
from random import *

ran = Random()

while True:
    file = open(f'{input("Quel fichier voulez-vous ouvrir ? [nom de la feuille de dates] > " )}.txt', 'r+')
    list_date = []

    for line in file.read().split('\n'):
        date = line.split(':')
        list_date.append(date)

    file.close()

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