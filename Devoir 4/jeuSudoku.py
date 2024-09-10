def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER

    for i in grille[row] :
        if i == num :
            return False
    return True
    

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER

    for i in grille:
        if i[col] == num :
            return False
    return True
            

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER

    R_row = 3 * (row // 3)
    C_col = 3 * (col // 3)
    for i in range(R_row, R_row + 3) :
        for j in range(C_col, C_col + 3) :
            if grille[i][j] == num :
                return False
    return True


def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # A COMPLETER

    for i in grille :
        for j in i :
            if j == 0 :
                return False
    return True

  
def verifierValide(grille, row, col, num):
    
    ''' (list, int, int, int) ->  bool
    * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
    * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
    '''
   
   # A COMPLETER

    return verifierLigne(grille, row, num) and verifierCol(grille, col, num) and verifierSousGrille(grille, row, col, num)














   

