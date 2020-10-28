#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import json
import string




# TODO: Définissez vos fonction ici

def differnce(fichier1, fichier2):
    with open(fichier1) as f1, open(fichier2) as f2:
        same = True
        while same:
            a = f1.read(1)
            b = f2.read(1)

            same = a == b
    return -1 if same else f1.tell()


def triplet(fichier, fichier2):
    # with open(fichier) as f, open("nouveauFichier", "w") as f2:
    #     for _ in len(fichier):
    #         carac = fichier.read(1)
    #         if carac == " ":
    #             f2.write(carac*3)
    #         else:
    #             f2.write(carac)

    with open(fichier, "r") as data, open(fichier2, "w") as f2:
        text = data.read()
        new_text = text.replace(" ", "   ")
        f2.write(new_text)

    # ou
    # with open(fichier, "r") as data, open(fichier2, "w") as f2:
    #     f2.write(data.read().replace(" ", "   "))

def notes():
    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}
    with open("notes.txt") as f, open("nouveau_fichier", "w") as n:
        tableau = f.readlines()
        for i in tableau:
            i.replace("n/", "")
            if float(i) < 21:
                notes = "F"
            elif float(i) < 41:
                notes = "D"
            elif float(i) < 51:
                notes = "C"
            elif float(i) < 71:
                notes = "B"
            else:
                notes = "A"
            n.write(i + " " + notes + "/n")
#sinon voir screenshot 28 octobre



def recette():
    dict ={}
    condition = True

    while (condition):
        recette = input ("ecrivez une recette, si vous avez termine, ecrivez fini")
        if recette !="fini":
            ingredient = input("ecrivez les ingredient de cette recette")
            dict.update({recette: ingredient})
        else:
            condition = False

    y = input("Que voulez vous faire dautre? A.modifier une recette, B. suppprimer une recette, C.vous avez fini")

    if y == "C":
        with open("test.json", 'w') as f:
            json.dump(dict, f, indent=4)
        return
    if y =="A" or y == "B":
        z = input("quelle recette?")
        if y == "B":
            del dict[z]
        else:
            ingredients = input("ecrire ingredient")
            dict[z] = ingredients

    else:
        print("commande non valide")

    with open("test.json", 'w') as f:
        json.dump(dict, f, indent=4)

#meilleur version voir screenshot 28 octobre

def nombre(fichier):

    with open(fichier) as f:
        resultat = [int(word) for word in f.read().split() if word.isdigit()]
    return resultat.sort

#.read() donne une string de tout le texte (au lieu de readline ou reaslines que ces par ligne
#et non tout le text. Alors quand on fait .split() on fais ensuite une liste ou chaque element sont les mots
#puisquon separe par les espaces





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    nombre("exemple.txt")

