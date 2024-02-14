#!/usr/bin/env python3

from plateau_puissance4 import plateau_rempli, contenu_case, \
    hauteur_colonne, colonne_remplie, jouer,\
    nb_pions_alignes_horizontalement, nb_pions_alignes_verticalement, \
    nb_pions_alignes_diagonalement_SONE, nb_pions_alignes_diagonalement_NOSE, \
    HAUTEUR_PLATEAU, LARGEUR_PLATEAU, JAUNE, ROUGE

import random

def obtenir_meilleur_coup(plateau: "Plateau", couleur: "JAUNE|ROUGE") -> int:
    """Fonction qui sera redéveloppée dans le deuxième TP sur le puissance 4
Pour l'instant le choix du coup est aléatoire"""
    coup_trouve = False
    while not coup_trouve:
        colonne_choisie = random.randrange(1, LARGEUR_PLATEAU)
        coup_trouve = not colonne_remplie(plateau, colonne_choisie)
    return colonne_choisie
