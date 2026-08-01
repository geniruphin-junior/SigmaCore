from math_moteur import ruphia_ultra_engine as rue
import sys, os
from array_stat import exec_stat as stat
import sys

print("======== Bienvenue dans le moteur scientifique =========\n")
print("Mode : Sympy + Numpy | Stat, Trigo, Algèbre")
menu = "1.Algèbre\n2.Trigonometrie\n3.Stat\n4.calcul simple\n5.Retour"
print(menu)
try:
    while True:
        choise_user = input("quelle est votre option : ")
        if choise_user == "5":

            raise KeyboardInterrupt
        elif choise_user == "1" or choise_user in [
            "Algebre",
            "algebre",
            "algebra",
            "algèbre",
        ]:
            equation = input("Metter ici votre équation :")
            print(rue(equation))
        elif choise_user == "2" or choise_user in ["Trigo", "trigonometrie", "trigo"]:
            expr = input(("mettez ici votre expression trigonometrique"))
            print(rue(expr))
        elif choise_user == "3" or choise_user in [
            "stat",
            "statistiques",
            "statistique",
        ]:
            print("mettez ici votre jeu de données en forme ")
            liste = input("Poser ici votre liste : ")
            print(stat(liste))

        elif choise_user == "4":
            calcul = input("mets tes calculs simples ici: ")
            print(rue(calcul))
        else:
            print("Cette fonctionnalité n'est pas reconnue par le moteur")
except KeyboardInterrupt:
    print("arret du processus")
    sys.exit(1)
