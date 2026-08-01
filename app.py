from math_moteur import MathSuperEngine as Me
import sys, os
from array_stat import exec_stat as stat

print("======== Bienvenue dans le moteur scientifique =========\n")
menu = "1.Algèbre\n2.Trigonometrie\n3.Stat\n4.calcul simple\n5.Retour"
print(menu)
while True:
    choise_user = input("quelle est votre option : ")
    if choise_user == "5":
        print("arret du processus")
        break
    elif choise_user == "1" or choise_user in [
        "Algebre",
        "algebre",
        "algebra",
        "algèbre",
    ]:
        equation = input("Metter ici votre équation :")
        print(Me(equation))
    elif choise_user == "2" or choise_user in ["Trigo", "trigonometrie", "trigo"]:
        expr = input(("mettez ici votre expression trigonometrique"))
        print(Me(expr))
    elif choise_user == "3" or choise_user in ["stat", "statistiques", "statistique"]:
        print("mettez ici votre jeu de données en forme ")
        liste = input("Poser ici votre liste : ")
        print(stat(liste))

    elif choise_user == "4":
        calcul = input("mets tes calculs simples ici: ")
        print(Me(calcul))
    else:
        print("Cette fonctionnalité n'est pas reconnue par le moteur")
