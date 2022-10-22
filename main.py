#"x = 5
#y = "Salut"
import importlib

#print(x)
#print(y)

#x = 1
#y = 3.5
#z= 1j

#a=float(x)
#b=int(y)
#c=complex(x)

#print(a)
#print(b)
#print(c)

#print(type(a))
#print(type(b))
#print(type(c))

#import random
#print(random.randrange(1,10))

# from math import factorial
# factorial(5)
# print(factorial(5))

# a = "Hello, ça va"
# print(a[1])

# for x in "Vincent":
#     print (x)
#
# a = "Hello, ça va"
# print(len(a))

# a = "Hello, ça va ? Mais ça va"
# if "va" not in a:
#     print("pas trouvé")

# x= "Salut les amis"
# print(x[2:5])

# x= "Salut les amis"
# print(x[:5])

# nombre = 15
# print("Le nombre est" + str(nombre))

# a = 2
# b = 6
# c = 3
#
# print(a, b, c, sep=" + ")

# list1 = range(3)
# list2 = range(5)
#
# print(list(list2))

# a = "Hello"
# print(a.upper())
#
# b= "VOILA"
# print(b.lower())
#
# c= " Bonjour ça va ? "
# print(c.strip())
#
# d= " Bonjour ça va? "
# print(d)
#
# e= "Bonjour ça va?"
# print(e.replace("j", "o"))

# f= " Bonjour, ça va ? "
# print(f.split(" , "))


# age = 40
# txt = "Voici mon age" + str(age)
# print(txt)

# age = 40
# age2 =45
# age3 = 70
# txt = "Voici mon age {} dans 5 ans je vais avoir {} et beaucoup plus tard {}"
# print(txt.format(age, age2, age3))

# a = "Bonjour voici \"Le\" merveilleux langage"
# print(a)

# a = "Bonjour, voici un exemple de phrase, et encore un exemple"
# x = a.find("exemple")
# print(x)

# print(10>9)
# print(10==9)
# print(10<9)

# x = "Hello"
# y = 20
# print(bool(x))
# print(bool(y))

# a = "Bonjour"
# print(a.replace("Bonjour", "Bonsoir"))

# a = "Bonjour tout le monde. Je répéte Bonjour"
# print(a.replace("Bonjour", "Bonsoir", 1))

# chaine = "Pierre, Julien, Anne, Marie, Lucien"
# chaine_liste = chaine.split(", ")
# chaine_liste.sort()
# chaine_en_ordre= ", ".join(chaine_liste)
# print(chaine_en_ordre)

# ma_liste = ["Pierre","Julien","Anne","Marie","Lucien"]
# print(ma_liste)

# ma_liste = ["Pierre","Julien","Anne","Marie","Lucien"]
# print(len(ma_liste))

# ma_liste = list(("Pierre","Julien","Anne","Marie","Lucien"))
# print(ma_liste)

#ma_liste = ["Pierre","Julien","Anne","Marie","Lucien"]
# print(ma_liste[-1])
# print(ma_liste[1:4])

# if ("Julien") in ma_liste:
#     print("oui")

# ma_liste[1] = "Vincent"
# print(ma_liste)

# ma_liste[1:3] = ["Vincent", "Sophie"]
# print(ma_liste)

# ma_liste[1:3] = ["Vincent", "Sophie", "Alexandre", "Marion", "Clément"]
# print(ma_liste)

# ma_liste[1:3] = ["Vincent"]
# print(ma_liste)

# ma_liste.insert(2, "Vincent")
# print(ma_liste)

# ma_liste1 = ["Anne","Marie","Lucien"]
# ma_liste2 = ["Pierre","Julien"]
#
# ma_liste1.extend(ma_liste2)
# print(ma_liste1)

# ma_liste1 = ["Anne","Marie","Lucien"]
# ma_listetuple = ["Pierre","Julien"]
#
# ma_liste1.extend(ma_listetuple)
# print(ma_liste1)

# ma_liste1 = ["Anne","Marie","Lucien"]
# ma_liste1.pop(1)
# print(ma_liste1)

# ma_liste1 = ["Anne","Marie","Lucien"]
# del ma_liste1[0]
# print(ma_liste1)

# ma_liste1 = ["Anne","Marie","Lucien"]
# ma_liste1.clear()
# print(ma_liste1)

# ma_liste1 = ["Anne","Marie","Lucien"]
# x = 0
# while x<len(ma_liste1):
#     print(ma_liste1[x])
#     x=x+1
#
# ma_liste1 = ["Anne","Marie","Lucien"]
# [print(x) for x in ma_liste1]

# import math
# rayon = 10.0
# volume = ( 4.0 * math.pi / 3.0) * (rayon ** 3)
# print(volume)

# fruits = ["Banane", "Pomme", "kiwi", "mangue"]
# fruits.sort()
# print(fruits)

# fruits = [100, 52, 87, 34]
# fruits.sort()
# print(fruits)

# fruits = ["Banane", "Pomme", "kiwi", "mangue"]
# fruits.sort(reverse = True)
# print(fruits)

# def maFonct (n):
#     return abs(n-50)
#
# fruits = [100, 50, 87, 65, 82, 23]
# fruits.sort(key = maFonct)
# print(fruits)

# laliste = ["fraise", "orange", "mangue", "banane"]
# laliste.sort()
# print(laliste)
#
# laliste2 = [1, 30, 25, 70]
# laliste2.sort()
# print(laliste2)

#si je veux "reverse" mon tri
# laliste = ["fraise", "orange", "mangue", "banane"]
# laliste.sort(reverse= True)
# print(laliste)

# def myfunc(x):
#     return abs(x-50)
#
# laliste = [100, 50, 65, 82, 23]
# laliste.sort( key = myfunc)
# print(laliste)

#faire une copie d'une liste
# laliste2 = [100, 50, 65, 82, 23]
# laliste2c = laliste2.copy()
# print(laliste2c)

#faire une "jointure" de liste
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
# liste3 = liste1 + liste2
# print(liste3)

#autre méthode
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
#
# for x in liste2:
#     liste1.append(x)
# print(liste1)

#et encore une autre méthode
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
#
# liste1.extend(liste2)
# print(liste1)

#vider la liste
# liste1 = ["x", "y", "z"]
# liste1.clear()
# print(liste1)

#les tuples
# montuple = ("Pomme", "Kiwi", "Citron")
# print(montuple)
# print(type(montuple))
# print(len(montuple))

#créer un tuple avec un objet

# montuple = ("poire",)
# print(type(montuple))

#et ici ? string
# montuple = ("poire")
# print(type(montuple))

#On peut mélanger les types et avoir des tuples constitués de booléens, de chaines,
#d'entier etc...
# montuple = (1, 2, 5)
# print(type(montuple))

#Le tuple est une classe comme les autres types en python

#faire appel au constructeur du tuple

# montuple = tuple(("pomme", "poire", "kiwi"))
# print(montuple)
# print(montuple[1])   me retourne l'élément poire
# print(montuple[-1])  me retourne le dernier élément

#on accède du coup à l'élément 3,4 et 5 (en position) mais pas 6
# montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
# print(montuple[2:5])

#me donne les 4 premiers éléments de mon tuple
# montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
# print(montuple[:4])

#me donne le troisième élément en position inclut jusqu'à la fin du tuple
# montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
# print(montuple[2:])

#on a pas le dernier élément puis on aura Melon, Fraise et Banane
# montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
# print(montuple[-4:-1])

# montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
# if "Citron" in montuple:
#     print("Oui Citron y est...")

#Comment mettre à jour un élément de mon tuple...pourtant il est immuable ?

# montuple = ("Pomme", "Kiwi", "Citron")
# a =list(montuple)
# a[1] = "fraise"
# montuple = tuple(a)
# print(montuple)

#Comment ajouter un élément dans mon tuple...

# montuple = ("Pomme", "Kiwi", "Citron")
# a =list(montuple)
# a.append("Pasteque")
# montuple = tuple(a)
# print(montuple)

#Ajouter un tule à un tuple
# montuple = ("Pomme", "Kiwi", "Citron")
# a = ("Fraise",)
# montuple += a
# print(montuple)

#Supprimer un élément
# montuple = ("Pomme", "Kiwi", "Citron")
# a = list(montuple)
# a.remove("Pomme")
# montuple = tuple(a)
# print(montuple)

#supprimer le tuple en entier
# montuple = ("Pomme", "Kiwi", "Citron")
# del montuple
# print(montuple)

#récupérer les éléments du tuple dans des variables
# montuple = ("Pomme", "Kiwi", "Citron")
# (a,b,c) = montuple
# print(a)
# print(b)
# print(c)

#récupérer les éléments du tuple dans des variables
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
# (a,b,*c) = montuple
# print(a)
# print(b)
# print(c)

#Parcourir un tuple via une boucle
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
# for x in montuple:
#     print(x)

#Parcourir un tuple en utilisant le numéro d'index et la longueur du tuple ( len, range et une boucle for )
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
# for x in range(len(montuple)):
#     print(montuple[x])

#Et pourquoi pas avec un while ?
# montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
# x = 0
# while x < len(montuple):
#     print(montuple[x])
#     x = x + 1
#
#Joindre des tuples et les multiplier
montuple1 = ("Pomme", "Kiwi", "Citron")
montuple2 = (4, 12, 6)
montuple3 = montuple1 + montuple2
print(montuple3)
montuple4 = montuple1 * 2
print(montuple4)

#Exercice
#Construire un code qui affiche une liste des nombres pairs de 1 à 100
liste_nombres_pairs = range(2, 101, 2)
print(list(liste_nombres_pairs))

#Exercice
#Construire un code qui affiche le lancé de 6 dés aléatoires
#6 valeurs possible, de 1 à 6
import random
for _ in range(6):
    nombre = random.choice(range(1, 7))
    print(nombre)

#Exercice
#Compter le nombre d'occurence d'une lettre

#Extension basique
lettre = "a"
phrase = "Salut ça va?"
print(phrase.lower().count(lettre))

#Extension: Compter le nombre d'occurence de chaque lettre puis afficher la fréquence de chaque lettre de la phrase

#importation "simple"
#pour importer un fichier python dans un autre, par exemple dans
# main.py je veux importer code.py
#import code

#importation comme un objet
#import importlib
file = importlib.import_module("Code")
obj = file.Codeclass()
obj.show()

#importation par from
from Code import CodeClass
var1 = CodeClass()
var1.show()


