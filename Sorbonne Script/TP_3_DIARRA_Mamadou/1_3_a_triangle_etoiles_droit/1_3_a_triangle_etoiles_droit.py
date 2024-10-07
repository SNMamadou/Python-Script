#!/usr/bin/python3

def affiche_blancs_puis_etoiles(B,E):
    return print(" "*B, "*"*E)

print("Affichage d'un triangle rectangle d'étoiles (angle à droite) \n")

Hauteur = int(input("Quelle hauteur ? \n"))
Etoiles = 1
Blanc   = Hauteur - 1 


while (x < Hauteur):
    affiche_blancs_puis_etoiles(Blanc,Etoiles)
    Blanc -= 1
    Etoiles += 1
    x += 1

