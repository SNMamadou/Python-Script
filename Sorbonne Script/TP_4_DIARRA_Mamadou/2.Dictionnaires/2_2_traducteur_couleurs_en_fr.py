#!/usr/bin/python3

couleursFR_ANG = {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "marron":"brown", "vert":"green", "gris":"grey", "rose":"pink","jaune":"yellow", "orange":"orange", "violet":"purple"}
couleursANG_FR = {"white":"blanc", "black":"noir", "red":"rouge", "blue":"bleu", "brown":"marron", "green":"vert", "grey":"gris", "pink":"rose", "yellow":"jaune", "orange":"orange", "violet":"purple"}

x = 0

while x == 0:
    choix = input("Couleur en anglais ? ")

    if choix == "quitter":
        print("Merci d'avoir utiliser ce service et à bientôt.")
        x = 1
    elif choix in couleursANG_FR:
        print(f"Traduction anglaise : {couleursANG_FR[choix]}")
    else:
        print("Veuiller entrer une couleur en français")