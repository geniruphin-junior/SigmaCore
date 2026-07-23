import numpy as np
import pandas as pd


def exec_stat(liste=[1, 2, 3, 5, 6, 898, 34]):
    liste = np.array(liste)
    resultat = f"Voici une analyse des vos données: \nsomme : {np.sum(liste)},\nMoyenne : {np.mean(liste)},Ecart-type : {np.std(liste)},\nMaximum : {np.max(liste)},\nMinimum : {np.min(liste)}"
    return resultat
