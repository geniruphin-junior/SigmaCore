import numpy as np


def exec_stat(liste):
    liste = np.array(liste)
    resulta = f"Voici une analyse des vos données: \nsomme : {np.sum(liste)},\nMoyenne : {np.mean(liste)},Ecart-type : {np.std(liste)},\nMaximum : {np.max(liste)},\nMinimum : {np.minimum(liste)}"
    return liste
