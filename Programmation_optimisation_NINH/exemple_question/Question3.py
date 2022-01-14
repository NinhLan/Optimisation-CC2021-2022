# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 06:10:58 2022

@author: ninht
"""

import numpy as np
import warnings

def simplex(type, A, B, C, D, M):
    """Calcule un point optimal pour le modèle de programmation linéaire donné par A*x <= B , Optimisation z= C' * x
    Arguments :
    type -- type d'optimisation, il peut être 'max' ou 'min'.
    A    -- matrice A du modèle (tableau numpy)
    B    -- matrice B du modèle, vecteur colonne (tableau numpy)
    C    -- matrice C du modèle, vecteur colonne (tableau numpy)
    D    -- vecteur colonne avec les types de restrictions du modèle (tableau numpy), 1 est <=, 0 est =, -1 est >=
            pour <= les restrictions ne font rien
            pour = restrictions ajouter une variable artificielle et un grand M dans la fonction objective (min --> +M , max --> -M)
            pour >= restrictions multiplier par -1
    M    -- grande valeur de M
    """
   

    # m -- nombre de restrictions
    # n -- nombre de variables
    (m, n)= A.shape

    basic_vars = []
    count = n

    # matrice avec de nouvelles variables
    R = np.eye(m)

    # les valeurs des nouvelles variables
    P = B

    # indicateur de position des variables artificielles
    artificial= []

    for i in range(m):
        if D[i] == 1:
            # ajouter la variable slack à la fonction objectif
            C = np.vstack((C, [[0]]))

            # enregistrer la variable slack comme variable de base
            count = count + 1
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 0]

        elif D[i] == 0:
            # ajouter la variable artificielle à la fonction objectif avec la grande valeur de M
            if type == 'min':
                C = np.vstack((C, [[M]]))
            else:
                C = np.vstack((C, [[-M]]))

            # enregistrer la variable artificielle comme variable de base
            count = count + 1
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 1]
        elif D[i] == -1:
            # ajouter les variables excédentaires et artificielles à la fonction objectif
            if type == 'min':
                C = np.vstack((C, [[0], [M]]))
            else:
                C = np.vstack((C, [[0], [-M]]))

            R = repeatColumnNegative(R, count + 1 - n)
            P = insertZeroToCol(P, count + 1 - n)

            # enregistrer la variable artificielle comme variable de base
            count = count + 2
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 0, 1]
        else:
            print("invalid case")

    # vertex actuel
    X = np.vstack((np.zeros((n, 1)), P))

    # ajouter de nouvelles variables à la matrice A
    A = np.hstack((A, R))

    # tableau simplex
    st = np.vstack((np.hstack((-np.transpose(C), np.array([[0]]))), np.hstack((A, B))))

    # nombre de colonnes
    (rows, cols) = st.shape

    # basic_vars = ((n + 1):n+m)'

    print('\nsimplex tableau\n')
    print(st)
    print('\ncurrent basic variables\n')
    print(basic_vars)
    print('\noptimal point\n')     
    print(X[basic_vars[i]])
        
    

    # vérifier si z != 0 (quand il y a des variables artificielles
    z_optimal = np.matmul(np.transpose(C), X)

    print('\nactuelt Z\n\n', z_optimal)

    if z_optimal != 0:
        for i in range(m):
            if D[i] == 0 or D[i] == -1:
                if type == 'min':
                    st[0,:]= st[0,:] + M * st[1+i,:]
                else:
                    st[0,:]= st[0,:] - M * st[1+i,:]

        print('\ntableau simplex corrigé\n')
        print(st)

    iteration = 0
    while True:
        if type == 'min':
            # Sélectionnez la valeur la plus positive
            w = np.amax(st[0, 0:cols-1])
            iw = np.argmax(st[0, 0:cols-1])
        else:
            # sélectionnez la valeur la plus négative
            w = np.amin(st[0, 0:cols-1])
            iw = np.argmin(st[0, 0:cols-1])

        if w <= 0 and type == 'min':
            print('\nPoint optimal global\n')
            break
        elif w >= 0 and type == 'max':
            print('\nPoint optimal global\n')
            break
        else:
            iteration = iteration + 1

            print('\n----------------- Iteration {} -------------------\n'.format(iteration))

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                T = st[1:rows, cols-1] / st[1: rows, iw]

            R = np.logical_and(T != np.inf, T > 0)
            (k, ik) = minWithMask(T, R)

            # ligne z actuelle
            cz = st[[0],:]

            # élément pivo
            pivot = st[ik+1, iw]

            # ligne du pivot divisée par l'élément du pivot
            prow = st[ik+1,:] / pivot

            st = st - st[:, [iw]] * prow

            # la ligne pivot est un cas particulier
            st[ik+1,:]= prow

            # nouvelle variable de base
            basic_vars[ik] = iw

            print('\nvariables de base actuelles\n')
            print(basic_vars)

            # new vertex
            basic = st[:, cols-1]
            X = np.zeros((count, 1))

            t = np.size(basic_vars)

            for k in range(t):
                X[basic_vars[k]] = basic[k+1]

            print('\npoint optimal actuel\n')
            print(X, '\n ==> donc:')
            for i in range(0,len(basic_vars)):
        
                print(X[basic_vars[i]], end=', ')
            # print(X)

            # new z value
            C = -np.transpose(cz[[0], 0:count])

            z_optimal = cz[0, cols-1] + np.matmul(np.transpose(C), X)
            st[0, cols-1] = z_optimal

            print('\n\ntableau de simplexe\n\n')
            print(st)

            print('\nactuel Z\n\n')
            print('Z = ', z_optimal)

    # check if some artificial variable is positive (infeasible solution)
    tv = np.size(artificial)
    for i in range(tv):
        if artificial[i] == 1:
            if X[n + i] > 0:
                print('\nsolution infaisable\n')
                break

    return (z_optimal[0, 0], X)


def minWithMask(x, mask):

    min = 0
    imin = 0

    n = np.size(x)

    for i in range(n):
        if mask[i] == 1:
            if min == 0:
                min = x[i]
                imin = i
            else:
                if min > x[i]:
                    min = x[i]
                    imin = i

    return (min, imin)


def repeatColumnNegative(Mat, h):
    """Répéter la colonne h multipliée par - 1"""
    (r, c) = Mat.shape
    Mat = np.hstack((Mat[:, 0:h-1], -Mat[:, [h-1]], Mat[:, h-1:c]))

    return Mat


def insertZeroToCol(col, h):
    """insérer un zéro à la colonne"""
    k = np.size(col)
    col = np.vstack((col[0:h-1, [0]], np.array([[0]]), col[h-1:k, [0]]))

    return col




if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    #Question 3:
    (z, x) = simplex('min', np.array([[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]),
                        np.array([[400], [300], [200], [300]]),
                        np.array([[30], [25], [36], [30]]),
                        np.array([[1], [1], [0], [0]]),
                  10000)
    print (z,x)
