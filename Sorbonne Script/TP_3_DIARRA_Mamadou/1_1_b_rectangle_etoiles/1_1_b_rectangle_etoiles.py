#!/usr/bin/python3

def affiche_blancs_puis_etoiles(B,E):
    return print(" "*B, "*"*E)

print("Affichage d'un rectangle d'étoiles.")

Hauteur = int(input("Quelle hauteur ? \n"))
Largeur = int(input("Quelle largeur ? \n"))
x = 0

while (x < Hauteur):
    affiche_blancs_puis_etoiles(0,Largeur)
    x += 1

while True:
    OuiNon = input("Voulez vous transposer le rectangle ? \n")

    x = 0

    if OuiNon == "oui":
        while (x < Largeur):
            affiche_blancs_puis_etoiles(0,Hauteur)
            x += 1
        break

    elif OuiNon == "non":
        break

    else:
        print("Il faut écrire oui ou non !!")
