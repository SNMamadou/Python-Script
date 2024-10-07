def affiche_blancs_puis_etoiles(nbr_espace: int, nbr_etoile: int):
    return print(" " * nbr_espace, "*" * nbr_etoile)

hauteur = int(input("Hauteur du triangle ? \n"))

for i in range(hauteur-1,-1,-1):
    affiche_blancs_puis_etoiles(hauteur - (i + 1), 2 * i + 1)
