import random

#Exercice 3.1

def random_list(l, n):
    
    x = 0
    list_gen = []

    for x in range(l):
        list_gen.append(random.randrange(n))

    return list_gen

#Exercice 3.2

def split(L, n):

    x = 0
    i = 0

    list_split_1 = []
    list_split_2 = []

    for x in L:

        i += 1

        if (i <= n):
            list_split_1.append(x)
            continue
        else:
            list_split_2.append(x)

    return list_split_1, list_split_2
#list_test = [1,2,3,4,5,6,8,9,13,56,9]
#print(split(list_test, 4))

#Exervice 3.3

def fusion(L1, L2):

    list_fusion = []

    #extend ajoute les itérable un par un alors que append non
    list_fusion.extend(L1)
    list_fusion.extend(L2)

    return list_fusion
#test1 = [1,2,3,4,5]
#test2 = [6,7,8,9,10]
#print(fusion(test1, test2))

#Exercice 3.4

def tri_fusion(L):
    
    if len(L) <= 1:
        return L
    
    compteur = len(L)// 2

    L1, L2 = split(L, compteur)

    trie_L1 = tri_fusion(L1)
    trie_L2 = tri_fusion(L2)

    #print(trie_L1)
    #print(trie_L2)

    return fusion(trie_L1, trie_L2)

test = [1,3,2,6,9,8,56,34,92,1]
print(tri_fusion(test))