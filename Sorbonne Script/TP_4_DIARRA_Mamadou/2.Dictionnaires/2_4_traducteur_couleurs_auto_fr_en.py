#!/usr/bin/python3

couleursFR_ANG = {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "marron":"brown", "vert":"green", "gris":"grey", "rose":"pink","jaune":"yellow", "orange":"orange", "violet":"purple",}
couleursANG_FR = {"white":"blanc", "black":"noir", "red":"rouge", "blue":"bleu", "brown":"marron", "green":"vert", "grey":"gris", "pink":"rose", "yellow":"jaune", "orange":"orange", "violet":"purple"}

x = 0

print("Bienvenue dans ce formidable outil de traduction français-anglais ou vice-versa.")

while x == 0:

    choix = input("Couleur en français ou anglais ? ")

    if(choix):
        
        if choix == "quitter":
            print("Merci d'avoir utiliser ce service et à bientôt.")
            break

        if choix in couleursFR_ANG:
            print(f"Traduction anglaise : {couleursFR_ANG[choix]}")
            continue

        if choix in couleursANG_FR:
            print(f"Traduction française : {couleursANG_FR[choix]}")
            continue

        choix2 = input("Désolé, je ne connais pas. À quelle langue appartient-elle ? ") 

        if (choix2 == "français"):
            trad = input("Traduction anglaise ? ")
            couleursFR_ANG[choix] = trad
            continue

        if (choix2 == "anglais"):
            trad = input("Traduction française ?")
            couleursANG_FR[choix] = trad
            continue