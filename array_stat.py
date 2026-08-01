import numpy as np
import pandas as pd
import re


def exec_stat(liste):

    true_liste = liste.lower().strip()

    if "[" and "]" in true_liste:

        true_liste = list_str = re.search(r"\[.*\]", true_liste).group()
        data = np.array(true_liste)
        resultat = f"Voici les métriques de votre liste : \nSomme = {np.sum(data)},\nMoyenne = {np.mean(data):.2f}\n,Ecart-type = {np.std(data):.2f}\n,Variance = {np.var(data):.2f}\n,Médiane = {np.median(data):.2f}\n,Q1/Q3 = {np.percentile(data,25)} / {np.percentile(data,75)}"
    return resultat
