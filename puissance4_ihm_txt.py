#!/usr/bin/env python3
""" Script qui permet de jouer à l'aide d'une interface texte au jeu de puissance 4 """

from plateau_puissance4 import contenu_case, colonne_remplie, VIDE, JAUNE, ROUGE, LARGEUR_PLATEAU, HAUTEUR_PLATEAU
from puissance4 import jouer_une_partie, PARTIE_NULLE, JAUNE_GAGNE, ROUGE_GAGNE
from ia_puissance4 import obtenir_meilleur_coup

SYMBOLES = {JAUNE:"o", ROUGE:"x", VIDE:" "}

def obtenir_coup(plateau: "Plateau", qui_joue: "Couleur") -> int:
    """ Fonction qui permet de demander un coup valide 
(compris entre 1 et LARGEUR_PLATEAU et dont la colonne n'est pas totalement rempli) 
à un joueur humain"""
    coup = None
    while not coup:
        try:
            print(plateau_en_chaine(plateau))
            print(f"Vous avez les {SYMBOLES[qui_joue]} ou voulez vous jouer : ")
            coup = int(input())
            if coup < 1 or coup > LARGEUR_PLATEAU:
                coup = None
            elif colonne_remplie(plateau, coup):
                coup = None
        except ValueError:
            coup = None
    return coup

def obtenir_coup_ia(plateau: "Plateau", qui_joue: "Couleur") -> int:
    """ Fonction qui demande à l'intelligence artificielle de calculer un coup """
    print(plateau_en_chaine(plateau))
    print(f"J'ai les {SYMBOLES[qui_joue]}, je réfléchis")
    coup = obtenir_meilleur_coup(plateau, qui_joue)
    print(f"Je joue en {coup}")
    return coup

def plateau_en_chaine(plateau: "Plateau") -> str:
    """Fonction qui permet d'avoir une représentation textuelle d'un plateau de Puissance 4"""

    res = ""
    for i in range (1,LARGEUR_PLATEAU):
        ligne = LARGEUR_PLATEAU-i
        chaine = "|".join([SYMBOLES[contenu_case(plateau, colonne, ligne)] for colonne in range(1,LARGEUR_PLATEAU+1)])
        res = res + "|" + chaine + "|\n"
    res = res + "+-" * LARGEUR_PLATEAU + "+\n"
    res = res + " " + " ".join(str(i) for i in range(1,LARGEUR_PLATEAU+1))
    return res

def choisir_type_joueur(couleur_du_joueur: str) -> "Fonction":
    """Fonction qui permet de retourner la fonction à appeler pour obtenir un coup d'un (Humain ou IA)"""
    res = None
    while not res:
        try:
            print(f"Le joueur ayant les {couleur_du_joueur} sera un humain 0 ou un l'IA 1:")
            saisie = int(input())
            if saisie == 0:
                res = obtenir_coup
            elif saisie == 1:
                res = obtenir_coup_ia
            else:
                res = None
        except ValueError:
            res = None
    return res
                
if __name__ == "__main__":
    obtenir_coup_jaune = choisir_type_joueur("jaune")
    obtenir_coup_rouge = choisir_type_joueur("rouge")
    plateau, qui_a_gagne = jouer_une_partie(obtenir_coup_jaune, obtenir_coup_rouge)
    print(plateau_en_chaine(plateau))
    if qui_a_gagne ==  PARTIE_NULLE:
        print("Partie nulle")
    elif qui_a_gagne == JAUNE_GAGNE:
        print(f"Les {SYMBOLES[JAUNE]} ont gagne")
    else:
        print(f"Les {SYMBOLES[ROUGE]} ont gagne")
