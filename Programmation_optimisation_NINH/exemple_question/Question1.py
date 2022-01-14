# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 06:08:42 2022

@author: ninht
"""

import numpy as np

# génère une matrice vide de taille adéquate pour les variables et les contraintes.
def gen_matrix(var,cons):
    tab = np.zeros((cons+1, var+cons+2))
    return tab

# vérifie si la colonne la plus à droite présente des valeurs négatives AU-DESSUS de la dernière ligne. Si des valeurs négatives existent, un autre pivot est nécessaire.
def next_round_r(table):
    m = min(table[:-1,-1])
    if m>= 0:
        return False
    else:
        return True

# vérifie que la ligne inférieure, à l'exception de la dernière colonne, ne comporte pas de valeurs négatives. Si des valeurs négatives existent, un autre pivot est nécessaire.
def next_round(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    if m>=0:
        return False
    else:
        return True

# Similaire à la fonction next_round_r, mais renvoie l'indice de ligne de l'élément négatif dans la colonne la plus à droite.
def find_neg_r(table):
    # lc = number of columns, lr = number of rows
    lc = len(table[0,:])
    # search every row (excluding last row) in final column for min value
    m = min(table[:-1,lc-1])
    if m<=0:
        # n = row index of m location
        n = np.where(table[:-1,lc-1] == m)[0][0]
    else:
        n = None
    return n

# renvoie l'indice de colonne de l'élément négatif dans la ligne inférieure
def find_neg(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    if m<=0:
        # n = indice de ligne pour m
        n = np.where(table[lr-1,:-1] == m)[0][0]
    else:
        n = None
    return n

# situe l'élément pivot dans le tableau pour retirer l'élément négatif de la colonne la plus à droite.
def loc_piv_r(table):
        total = []
        # r = indice de ligne de l'entrée négative
        r = find_neg_r(table)
        # trouve tous les éléments de la ligne, r, à l'exclusion de la dernière colonne
        row = table[r,:-1]
        # trouve la valeur minimale dans la ligne (à l'exclusion de la dernière colonne)
        m = min(row)
        # c = indice de colonne pour l'entrée minimale dans la ligne
        c = np.where(row == m)[0][0]
        # tous les éléments de la colonne
        col = table[:-1,c]
        # il faut parcourir cette colonne pour trouver le plus petit rapport positif
        for i, b in zip(col,table[:-1,-1]):
            # i ne peut pas être égal à 0 et b/i doit être positif.
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # pour les éléments qui ne répondaient pas aux exigences ci-dessus. Sinon, notre numéro d'index serait défectueux.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index,c]
# processus similaire, renvoie un élément spécifique du tableau sur lequel on peut pivoter.
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # pour les éléments qui ne répondaient pas aux exigences ci-dessus. Sinon, notre numéro d'index serait erroné
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index,n]

# Prend une chaîne de caractères en entrée et retourne une liste de nombres à arranger dans un tableau.
def convert(eq):
    eq = eq.split(',')
    if '>=' in eq:
        g = eq.index('>=')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if '<=' in eq:
        l = eq.index('<=')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq
    

# La dernière ligne du tableau dans un problème de minimum est l'inverse d'un problème de maximisation, les éléments sont donc multipliés par (-1).
def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]
    return table

# génère x1,x2,...xn pour le nombre variable de variables.
def gen_var(table):
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

# fait pivoter le tableau de telle sorte que les éléments négatifs soient éliminés de la dernière ligne et de la dernière colonne.
def pivot(row,col,table):
    # nombre de lignes
    lr = len(table[:,0])
    # nombre de colonnes
    lc = len(table[0,:])
    t = np.zeros((lr,lc))
    pr = table[row,:]
    if table[row,col]**2>0: 
        e = 1/table[row,col]
        r = pr*e
        for i in range(len(table[:,col])):
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)
        t[row,:] = list(r)
        return t
    else:
        print('Impossible de pivoter sur cet élément.')

# vérifie s'il y a de la place dans la matrice pour ajouter une autre contrainte
def add_cons(table):
    lr = len(table[:,0])
    # on veut savoir s'il existe au moins deux rangées d'éléments nuls.
    empty = []
    # itérer à travers chaque ligne
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # utiliser la valeur au carré pour que (-x) et (+x) ne s'annulent pas mutuellement
            total += j**2
        if total == 0:
            # ajouter un zéro à la liste UNIQUEMENT si tous les éléments d'une ligne sont des zéros
            empty.append(total)
    # Il y a au moins 2 rangées avec tous les éléments zéro si ce qui suit est vrai
    if len(empty)>1:
        return True
    else:
        return False

# ajoute une contrainte à la matrice
def constrain(table,eq):
    if add_cons(table) == True:
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        # mettre en place un compteur pour itérer sur la longueur totale des lignes
        j = 0
        while j < lr:
            # Itération par ligne
            row_check = table[j,:]
            # le total sera la somme des entrées de la ligne
            total = 0
            # Trouver la première ligne avec toutes les entrées 0
            for i in row_check:
                total += float(i**2)
            if total == 0:
                # Nous avons trouvé la première ligne avec toutes les entrées zéro.
                row = row_check
                break
            j +=1

        eq = convert(eq)
        i = 0
        # itérer à travers tous les termes de la fonction de contrainte, en excluant le dernier.
        while i<len(eq)-1:
            # attribuer des valeurs de ligne selon l'équation
            row[i] = eq[i]
            i +=1
        #row[len(eq)-1] = 1
        row[-1] = eq[-1]

        # ajouter la variable slack selon l'emplacement dans le tableau.
        row[var+j] = 1
    else:
        print('Impossible d\'ajouter une autre contrainte.')

# vérifie si une fonction objective peut être ajoutée à la matrice
def add_obj(table):
    lr = len(table[:,0])
    # savoir s'il existe exactement une rangée d'éléments nuls.
    empty = []
    # itérer à travers chaque ligne
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # utiliser la valeur au carré pour que (-x) et (+x) ne s'annulent pas mutuellement
            total += j**2
        if total == 0:
            # ajouter un zéro à la liste UNIQUEMENT si tous les éléments d'une ligne sont des zéros
            empty.append(total)
    # Il y a exactement une ligne avec tous les éléments zéro si ce qui suit est vrai
    if len(empty)==1:
        return True
    else:
        return False

# ajoute la fonction onjective à la matrice.
def obj(table,eq):
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:,0])
        row = table[lr-1,:]
        i = 0
    # itérer à travers tous les termes de la fonction de contrainte, en excluant le dernier.
        while i<len(eq)-1:
            # attribuer des valeurs de ligne selon l'équation
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('Vous devez finir d\'ajouter les contraintes avant de pouvoir ajouter la fonction objectif.')

# résout le problème de maximisation pour une solution optimale, renvoie un dictionnaire avec les clés x1,x2...xn et max.
def maxz(table, output='summary'):
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)

    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val

# résout les problèmes de minimisation pour une solution optimale, retourne un dictionnaire avec les clés x1,x2...xn et min.
def minz(table, output='summary'):
    table = convert_min(table)

    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)

    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['min'] = table[-1,-1]*-1
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val
    
    
if __name__ == "__main__":    

    # #Question 1
    m = gen_matrix(3,3)
    constrain(m,'1,2,1.5,<=,12000')
    constrain(m,'1.5,1.5,1,<=,4600')
    constrain(m,'1.5,1.5,0.5,<=,2400')
    obj(m,'11,16,15')
    print(maxz(m))

