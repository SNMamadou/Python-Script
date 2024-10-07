#!/usr/bin/python3

def recherche_dichotomique_recursive(element):
    limitemin = 0
    limitemax = 100
    Detective = 0
    Tentative = 0

    while(element != Detective):
        Detective = (limitemin + limitemax) // 2

        if (element < Detective):
            limitemax = Detective - 1
            print(limitemax)
            Tentative += 1
        elif(element > Detective):
            limitemin = Detective + 1
            print(limitemin)
            Tentative += 1
        else:
            Detective = element
    return print(f"Bonne réponse : {Detective}, votre score est de : {Tentative}")

Secret = int(input("Le joueur secret doit choisir un nombre entre entier entre 0 et 100 : "))

Deviner = recherche_dichotomique_recursive(Secret)
