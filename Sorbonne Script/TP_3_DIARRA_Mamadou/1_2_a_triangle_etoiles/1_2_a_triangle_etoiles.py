#!/usr/bin/python3

def affiche_blancs_puis_etoiles(B,E):
    return print(" "*B, "*"*E)


print("Affichage d'un triangle rectangle d'étoiles. \n")

x = 0

Hauteur = int(input("Quelle hauteur ? \n"))
Largeur = 0

while (x < Hauteur):
    affiche_blancs_puis_etoiles(0,Largeur)
    x += 1
    Largeur += 1
