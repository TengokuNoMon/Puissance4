#!/usr/bin/env python3
"""Module permettant de manipuler un plateau de Puissance 4"""

VIDE = 0
JAUNE = 1
ROUGE = 2

LARGEUR_PLATEAU = 7
HAUTEUR_PLATEAU = 6


def plateau_vide() -> "Plateau":
    """Fonction qui permet d'obtenir un plateau vide de LARGEUR_PLATEAU colonnes (1..LARGEUR_PLATEAU) chaque colonne étant de hauteur HAUTEUR_PLATEAU"""
    plateau_vide=[]
    for i in range(HAUTEUR_PLATEAU):
    	plateau_vide.append([VIDE for n in range(LARGEUR_PLATEAU)])
    return plateau_vide


def jouer(plateau: "Plateau", colonne: int, pion: "JAUNE|ROUGE") -> None:
    """Fonction qui permet de jouer un pion dans un colonne pas encore remplie (hauteur_colonne(colonne) <= HAUTEUR_PLATEAU)"""
    if not colonne_remplie(plateau, colonne) :
    	plateau[hauteur_colonne(plateau,colonne)][colonne - 1]=pion
    return  plateau

def contenu_case(plateau: "Plateau", colonne: int, ligne:int) -> "Contenu":
    """Fonction qui permet d'obtenir le contenu d'une case du plateau: ROUGE, JAUNE ou VIDE à partir de la colonne (1..LARGEUR_PLATEAU) et de la ligne (1..HAUTEUR_PLATEAU)"""
    
    return plateau[ligne - 1][colonne - 1]

def hauteur_colonne(plateau: "Plateau", colonne: int) -> int:
    """Fonction qui permet d'obtenir la hauteur d'une colonne (1..LARGEUR_PLATEAU)"""
    for ligne in range(1, HAUTEUR_PLATEAU+1):
    	if contenu_case(plateau,colonne,ligne) ==  VIDE:
    		return(ligne-1)
    return(HAUTEUR_PLATEAU)

def colonne_remplie(plateau: "Plateau", colonne: int) -> bool:
    """Fonction qui permet de savoir si une colonne (1..LARGEUR_PLATEAU) est remplie"""
    return hauteur_colonne(plateau,colonne)==HAUTEUR_PLATEAU

def plateau_rempli(plateau: "Plateau") -> bool:
    """Fonction qui permet de savoir si le plateau est rempli"""
    condition_arret=True
    colonne=1
    while condition_arret and colonne<=LARGEUR_PLATEAU:
    	condition_arret=colonne_remplie(plateau,colonne)
    	colonne+=1
    return condition_arret
def _nb_pions_alignes(plateau: "Plateau", colonne:int, ligne:int, pas_x:int, pas_y:int):
    col = colonne
    lig = ligne
    res = 0
    pion_ref = contenu_case(plateau,colonne,ligne)
    while col in range(1,LARGEUR_PLATEAU+1) and \
          lig in range(1,HAUTEUR_PLATEAU+1) and \
          contenu_case(plateau, col, lig) == pion_ref:
        res +=1
        col +=pas_x
        lig += pas_y
    return res
    
    
def nb_pions_alignes_horizontalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    horizontalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    return  _nb_pions_alignes(plateau,colonne,ligne,-1,0) \
            +_nb_pions_alignes(plateau,colonne,ligne,1,0) \
            -1

    
def nb_pions_alignes_verticalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    verticalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    return _nb_pions_alignes(plateau, colonne, ligne, 0 , -1) \
    +_nb_pions_alignes(plateau, colonne, ligne, 0, 1) \
    -1

def nb_pions_alignes_diagonalement_SONE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Sud-Ouest au Nord-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    return _nb_pions_alignes(plateau, colonne, ligne, -1 , -1 ) \
           +_nb_pions_alignes(plateau, colonne, ligne, 1, 1 )\
            -1

def nb_pions_alignes_diagonalement_NOSE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Nord-Ouest au Sud-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    return _nb_pions_alignes(plateau, colonne, ligne, 1, -1) \
           +_nb_pions_alignes(plateau, colonne, ligne, -1 ,1 )\
            -1

if __name__ == "__main__":
    p = [[ROUGE, JAUNE, JAUNE, JAUNE, ROUGE, ROUGE, VIDE],
         [VIDE, JAUNE, ROUGE, ROUGE, JAUNE, VIDE, VIDE],
         [VIDE, VIDE, ROUGE, JAUNE, ROUGE, VIDE, VIDE],
         [VIDE, VIDE, JAUNE, VIDE, JAUNE, VIDE, VIDE],
         [VIDE, VIDE, VIDE, VIDE, ROUGE, VIDE, VIDE],
         [VIDE, VIDE, VIDE, VIDE, JAUNE, VIDE, VIDE]]
    res = "OK" if contenu_case(p, 1,2) == VIDE else "KO"
    print(f"  contenu_case vide {res}")
    res = "OK" if contenu_case(p, 2,1) == JAUNE else "KO"
    print(f"  contenu_case JAUNE {res}")
    res = "OK" if contenu_case(p, 3,2) == ROUGE else "KO"
    print(f"  contenu_case ROUGE {res}")
    res = "OK" if hauteur_colonne(p, 7) == 0 else "KO"
    print(f"  hauteur_colonne vide {res}")
    res = "OK" if hauteur_colonne(p, 2) == 2 else "KO"
    print(f"  hauteur_colonne non vide {res}")
    res = "OK" if not colonne_remplie(p, 2) else "KO"
    print(f"  colonne_remplie non remplie {res}")
    res = "OK" if colonne_remplie(p, 5) else "KO"
    print(f"  colonne_remplie remplie {res}")
    res = "OK" if not plateau_rempli(p) else "KO"
    print(f"  plateau_rempli non rempli {res}")
    res = "OK" if plateau_rempli([[ROUGE]*LARGEUR_PLATEAU]*HAUTEUR_PLATEAU) else "KO"
    print(f"  plateau_rempli rempli {res}")    
    p = plateau_vide()
    test = [hauteur_colonne(p, colonne) for colonne in range(LARGEUR_PLATEAU)]
    res = "OK" if sum(test) == 0 else "KO"
    print(f"  plateau_vide {res}")
    jouer(p,2,JAUNE)
    jouer(p,2,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,4,JAUNE)
    jouer(p,4,JAUNE)
    jouer(p,4,ROUGE)
    jouer(p,4,ROUGE)
    jouer(p,5,JAUNE)
    jouer(p,5,ROUGE)
    jouer(p,5,JAUNE)    
    res = "OK" if contenu_case(p, 2, 2) == ROUGE else "KO"
    print(f"  jouer {res}")
    res = "OK" if nb_pions_alignes_horizontalement(p, 3,1) == 4 else "KO"
    print(f"  nb_pions_alignes_horizontalement {res}")       
    res = "OK" if nb_pions_alignes_verticalement(p, 4,1) == 2 else "KO"
    print(f"  nb_pions_alignes_verticalement {res}")
    res = "OK" if nb_pions_alignes_diagonalement_SONE(p, 4,3) == 2 else "KO"
    print(f"  nb_pions_alignes_diagonalement_SONE {res}")    
    res = "OK" if nb_pions_alignes_diagonalement_NOSE(p, 4,3) == 3 else "KO"
    print(f"  nb_pions_alignes_diagonalement_NOSE {res}")    
    
