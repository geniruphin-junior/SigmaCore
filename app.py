# import des modules persos,de numpy et sympy
from math_moteur import ruphia_ultra_engine as rue
import sys, os
from array_stat import exec_stat as stat
import sys

# acceuil de l'app
print("======== Bienvenue dans le moteur scientifique =========\n")
print("Mode : Sympy + Numpy | Stat, Trigo, Algèbre")
menu = "1.Algèbre\n2.Trigonometrie\n3.Stat\n4.calcul simple\n5.Retour\n6.documentation"
print(menu)

# fonctionalitées de l'app
try:
    while True:
        # pour sortir
        choise_user = input("quelle est votre option : ")
        if choise_user == "5":
            raise KeyboardInterrupt

        # algebre
        elif choise_user == "1" or choise_user in [
            "Algebre",
            "algebre",
            "algebra",
            "algèbre",
        ]:
            equation = input("Metter ici votre équation :")
            print(rue(equation))

        # trigonometrie
        elif choise_user == "2" or choise_user in ["Trigo", "trigonometrie", "trigo"]:
            expr = input(("mettez ici votre expression trigonometrique"))
            print(rue(expr))

        # statistiques
        elif choise_user == "3" or choise_user in [
            "stat",
            "statistiques",
            "statistique",
        ]:
            print("mettez ici votre jeu de données en forme ")
            liste = input("Poser ici votre liste : ")
            print(stat(liste))

        # calcul basique
        elif choise_user == "4":
            calcul = input("mets tes calculs simples ici: ")
            print(rue(calcul))

        # documentations
        elif choise_user == "6":
            with open(file="notes.txt", mode="r", encoding="UTF-8") as doc:
                print(doc.read())
        else:
            print("Cette fonctionnalité n'est pas reconnue par le moteur")
except KeyboardInterrupt:
    print("arret du processus")
    sys.exit(1)
