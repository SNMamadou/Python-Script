#!/usr/bin/python3

#Pour que le code soit assez visible j'ai ajouté quelques commentaires

from random import randrange

def recherche_dichotomique_recursive(elementJoueur,elementPC):
    limitemax = 100
    limitemin = 0
    Detective = 0
    TentativePC = 0
    TentativeJoueur = 0
    x = 0           

#Boucle jusqu'a ce qu'une des boucle retourne x a 1
    while x == 0:
        Deviner = int(input("Deviner un nombre : \n"))
        Detective = (limitemin + limitemax) // 2
        
        #La partie du code de la machine
        if (elementPC < Detective):
            limitemax = Detective - 1
            print(f"Tentative PC : {limitemax}")
            TentativePC += 1
        elif(elementPC > Detective):
            limitemin = Detective + 1
            print(f"Tentative PC : {limitemin}")
            TentativePC += 1
        else:
            Detective = elementPC   
            print(f"Bonne réponse machine : {Detective}, votre score est de : {TentativePC}")
            x = 1
            
        #La partie de code du joueur
        if elementJoueur == Deviner:
            print(f"Bonne réponse joueur : {Deviner}, votre score est de : {TentativeJoueur}")
            x = 1
        else:
            print("Mauvaise réponse")
            TentativeJoueur += 1
     
SecretJoueur = int(input("Le joueur doit choisir un nombre pour la machine entre 0 et 100 : "))

print("La partie commence \n")

print("Le joueur secret doit choisir un nombre entre entier entre 0 et 100 \n")

#Le print permet d'avoir la vateur généré pour voir si le code fonctionne quand trouvé
SecretPC = randrange(1,101)
print(SecretPC)

recherche_dichotomique_recursive(SecretPC,SecretJoueur)
