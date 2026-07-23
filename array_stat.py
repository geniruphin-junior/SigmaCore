import numpy as np
import pandas as pd
import re


def exec_stat(liste):

    liste = liste.lower().strip()

    if "[" and "]" in liste:
        true_liste = liste.copy()
        true_liste = list_str = re.search(r"\[.*\]", true_liste).group()
        resultat = f"Voici les métriques de votre liste : \nSomme = {np.sum(true_liste)},\nMoyenne = {np.mean(true_liste)},Ecart-type = {np.std(true_liste)},Variance = {np.var(true_liste)},Médiane = {np.median(true_liste)},Q1/Q3 = {np.percentile(true_liste,25)} / {np.percentile(true_liste,75)}"
    return resultat
