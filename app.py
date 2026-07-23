from math_moteur import MathSuperEngine
import sys, os
from array_stat import exec_stat

print("======== Bienvenue dans le moteur scientifique =========\n")
menu = "1.Algèbre\n2.Trigonometrie\n3.Stat\n4.calcul simple\n5.Retour"

print(menu)
choise_user = input("quelle est votre option : ")
if choise_user == "1" or choise_user in [
    "Algebre",
    "algebre",
    "algebra",
    "analyse",
    "algèbre",
]:
    print("Metter ici votre équation")
elif choise_user == "2" or choise_user in ["Trigo", "trigonometrie", "trigo"]:
    print("mettez ici votre expression trigonometrique")
elif choise_user == "3" or choise_user in ["stat", "statistiques", "statistique"]:
    print("mettez ici votre jeu de données en forme [a,b,c,d,c]")
    liste = input("Poser ici votre liste : ")
    print(exec_stat(liste))

elif choise_user == "4":
    print("mets tes calculs")
else:
    print("Cette fonctionnalité n'est pas reconnue par le moteur")
