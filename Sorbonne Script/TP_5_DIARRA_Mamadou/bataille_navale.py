import turtle

def obtenir_coordonnees(entetes_colonnes, entetes_lignes):
    while True:
        coordonnees = input("Coordonnées (ex: C3) ? ").strip().upper()
        if len(coordonnees) < 2:
            continue
        colonne, ligne = coordonnees[0], coordonnees[1:]
        if colonne in entetes_colonnes and ligne in entetes_lignes:
            return colonne, ligne

def creer_grille(entetes_colonnes, entetes_lignes):
    navires = [[('A', '1'), ('A', '2'), ('A', '3')], [('C', '3'), ('D', '3')], [('D', '5'), ('E', '5')]]
    grille = {(colonne, ligne): False for colonne in entetes_colonnes for ligne in entetes_lignes}
    for navire in navires:
        for case in navire:
            grille[case] = True
    return navires, grille

def deplacer(position):
    turtle.up()
    turtle.goto(position)
    turtle.down()

def tracer_carre(position, taille, plein, couleur):
    deplacer(position)
    if plein:
        turtle.fillcolor(couleur)
        turtle.begin_fill()
    for _ in range(4):
        turtle.forward(taille)
        turtle.left(90)
    if plein:
        turtle.end_fill()

def tracer_grille(position_initiale, taille, nombre_lignes, nombre_colonnes):
    x0, y0 = position_initiale
    for ligne in range(nombre_lignes):
        for colonne in range(nombre_colonnes):
            tracer_carre((x0 + colonne * taille, y0 + ligne * taille), taille, False, "white")

def ecrire(position, taille, caractere):
    deplacer((position[0] + taille / 2, position[1] + taille / 4))
    turtle.write(caractere, align="center", font=("Arial", int(taille / 2), "normal"))

def tracer_entetes(position_initiale, taille, entetes_colonnes, entetes_lignes):
    x0, y0 = position_initiale
    for idx_colonne, colonne in enumerate(entetes_colonnes):
        ecrire((x0 + idx_colonne * taille, y0 - taille), taille, colonne)
    for idx_ligne, ligne in enumerate(entetes_lignes):
        ecrire((x0 - taille, y0 + idx_ligne * taille), taille, ligne)

def jouer():
    entetes_colonnes = "ABCDE"
    entetes_lignes = "12345"
    position_initiale = (-200, -200)
    taille = 50

    navires, grille = creer_grille(entetes_colonnes, entetes_lignes)
    turtle.speed(0)
    turtle.hideturtle()
    tracer_grille(position_initiale, taille, len(entetes_lignes), len(entetes_colonnes))
    tracer_entetes(position_initiale, taille, entetes_colonnes, entetes_lignes)

    devinees = {}
    navires_en_vie = navires.copy()

    while navires_en_vie:
        colonne, ligne = obtenir_coordonnees(entetes_colonnes, entetes_lignes)
        if (colonne, ligne) in devinees:
            continue
        position_tir = (colonne, ligne)
        if grille[(colonne, ligne)]:
            tracer_carre(position_tir, taille, True, "salmon4")
            devinees[(colonne, ligne)] = True
            navires_en_vie = [navire for navire in navires_en_vie if not all(case in devinees for case in navire)]
        else:
            tracer_carre(position_tir, taille, True, "azure")
            devinees[(colonne, ligne)] = False

    print("Bravo, vous avez coulé tous les navires !")
    turtle.done()

jouer()
