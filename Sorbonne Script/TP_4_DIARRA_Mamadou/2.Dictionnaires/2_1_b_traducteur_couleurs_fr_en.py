#!/usr/bin/python3

couleurs = {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "marron":"brown", "vert":"green", "gris":"grey", "rose":"pink","jaune":"yellow", "orange":"orange", "violet":"purple"}

x = 0

while x == 0:
    choix = input("Couleur en français ? ")

    if choix == "quitter":
        print("Merci d'avoir utiliser ce service et à bientôt.")
        x = 1
    elif choix in couleurs:
        print(f"Traduction anglaise : {couleurs[choix]}")
    else:
        print("Veuiller entrer une couleur en français")