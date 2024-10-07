#!/usr/bin/python3

def affiche_blancs_puis_etoiles(B,E):
    return print(" "*B, "*"*E)

print("Affichage d'un triangle rectangle d'étoiles (angle à droite) \n")

Hauteur = int(input("Quelle hauteur ? \n"))
Etoiles = Hauteur
Blanc   = 0

x = 0
y = 0

while (x < Hauteur):
    affiche_blancs_puis_etoiles(Blanc,Etoiles)
    Etoiles -= 1
    Blanc   += 1
    x += 1
    