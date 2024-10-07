#!/usr/bin/python3

from random import randrange

print("Le joueur secret doit choisir un nombre entre entier entre 0 et 100 \n")
Secret = randrange(1,101)

print(Secret)

Tentative = 0

while True:
    Deviner = int(input("Deviner un nombre : \n"))

    if Secret == Deviner:
        print(f"Bonne réponse, votre score est de : {Tentative}")
        break
    else:
        print("Mauvaise réponse")
        Tentative += 1
