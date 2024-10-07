#!/usr/bin/python3

couleurs = {"blanc":"white", "noir":"black", "rouge":"red", "bleu":"blue", "marron":"brown", "vert":"green", "gris":"grey", "rose":"pink","jaune":"yellow", "orange":"orange", "violet":"purple"}

choix = input("Couleur en français ? ")
print(f"Traduction anglaise : {couleurs[choix]}")