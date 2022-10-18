#"x = 5
#y = "Salut"

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

def maFonct (n):
    return abs(n-50)

fruits = [100, 50, 87, 65, 82, 23]
fruits.sort(key = maFonct)
print(fruits)