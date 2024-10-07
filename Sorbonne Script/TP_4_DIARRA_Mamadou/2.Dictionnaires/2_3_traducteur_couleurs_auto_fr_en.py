#!/usr/bin/python3

couleursFR_ANG = {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "marron":"brown", "vert":"green", "gris":"grey", "rose":"pink","jaune":"yellow", "orange":"orange", "violet":"purple"}
couleursANG_FR = {"white":"blanc", "black":"noir", "red":"rouge", "blue":"bleu", "brown":"marron", "green":"vert", "grey":"gris", "pink":"rose", "yellow":"jaune", "orange":"orange", "violet":"purple"}

x = 0

print("Bienvenue dans ce formidable outil de traduction français-anglais ou vice-versa.")

while x == 0:
    choix = input("Couleur en français ou anglais ? ")
    y = 0
    z = 0

    for y in couleursFR_ANG:
        if y == choix:
            print(f"Traduction anglaise : {couleursFR_ANG[choix]}")
        
    for z in couleursANG_FR:
        if z == choix:
            print(f"Traduction anglaise : {couleursANG_FR[choix]}")

    if choix == "quitter":
        print("Merci d'avoir utiliser ce service et à bientôt.")
        x = 1