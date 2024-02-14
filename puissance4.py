#!/usr/bin/env python3

from plateau_puissance4 import plateau_vide, plateau_rempli, jouer, JAUNE, ROUGE, LARGEUR_PLATEAU, HAUTEUR_PLATEAU, nb_pions_alignes_verticalement, nb_pions_alignes_horizontalement, nb_pions_alignes_diagonalement_SONE, nb_pions_alignes_diagonalement_NOSE, hauteur_colonne

PARTIE_NULLE = 0
JAUNE_GAGNE = 1
ROUGE_GAGNE = 2

def dernier_coup_gagnant(plateau: "Plateau", colonne: int) -> bool:
    """Fonction qui permet de savoir si le dernier coup joué dans une certaine colonne est un coup gagnant"""
    return nb_pions_alignes_verticalement(plateau, colonne, hauteur_colonne(plateau, colonne)) >= 4 \
        or nb_pions_alignes_horizontalement(plateau, colonne, hauteur_colonne(plateau, colonne)) >= 4 \
        or nb_pions_alignes_diagonalement_SONE(plateau, colonne, hauteur_colonne(plateau, colonne)) >= 4 \
        or nb_pions_alignes_diagonalement_NOSE(plateau, colonne, hauteur_colonne(plateau, colonne)) >= 4

def jouer_une_partie(obtenir_coup_jaune: "Fonction(Plateau, Couleur) -> int",
                     obtenir_coup_rouge: "Fonction(Plateau, Couleur) -> int") \
                     -> "PARTIE_NULLE|JAUNE_GAGNE|ROUGE_GAGNE":
    """ Fonction qui permet de jouer une partie de puissavnce 4 
    en donnant deux fonctions qui permettent 
    d'obtenir, à chauqe tour de jeu, un coup pour les jaunes et pour les rouges"""
    
    plateau = plateau_vide()
    qui_joue = JAUNE
    obtenir_coup = obtenir_coup_jaune
    coup = obtenir_coup(plateau, qui_joue)
    jouer(plateau, coup, qui_joue)
    while not plateau_rempli(plateau) and not dernier_coup_gagnant(plateau, coup):
        obtenir_coup = obtenir_coup_rouge if obtenir_coup == obtenir_coup_jaune else obtenir_coup_jaune
        qui_joue = ROUGE if qui_joue == JAUNE else JAUNE
        coup = obtenir_coup(plateau, qui_joue)
        jouer(plateau, coup, qui_joue)
    if plateau_rempli(plateau) and not dernier_coup_gagnant(plateau, coup):
        return plateau, PARTIE_NULLE
    else:
        return plateau, JAUNE_GAGNE if qui_joue == JAUNE else ROUGE_GAGNE
    
    
    
