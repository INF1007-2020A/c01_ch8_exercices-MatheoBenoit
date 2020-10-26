#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



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



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
