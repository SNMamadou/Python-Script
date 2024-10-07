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