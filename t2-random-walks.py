"""
Trabalho T2 da disciplina Teoria dos Grafos, ministrada em 2014/02
    Alunos:
        Daniel  Nobusada
        Thales Eduardo Adair Menato         407976
        Jorge Augusto Bernardo              407844
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import pdb  # pdb.trace() pra debug

#   Importa grafo Zachary's Karate Club
matrixG = nx.read_gml('karate.gml')
"""
1)  Computacao da distribuicao estacionaria teorica (steady state) do grafo
    w(i) = d(vi) / 2|E|
"""
w_real = []
for i in matrixG.nodes_iter():
        aux = float(matrixG.degree(i)) / float((2 * matrixG.number_of_edges()))
        w_real.append(aux)
"""
2)  Calcular The Power Method
    http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/
    downloads/c10s3.pdf
"""
#   Matriz P recebe a matriz de adjacencia de matrixG
matrixP = nx.adjacency_matrix(matrixG)
#   A soma de cada linha eh calculado
sum_linha = []
for i in matrixP:
    sum_linha.append(i.sum())
#   Para cada p(i,j) de P temos p(i,j) = p(i,j)/sum_linha(i)
for i in range(0, matrixP.shape[0]):
    for j in range(0, matrixP.shape[1]):
        matrixP[i, j] = float(matrixP[i, j]) / float(sum_linha[i])
# Vetor w_inicial onde a soma eh 1 com divisao de probabilidade 1/G.order()
# Para o grafo utilizado G.order() = 34
w_inicial = np.array([1.0/float(matrixG.order())
                      for i in range(0, matrixG.order())])
# Calcular w_power5
w_power5 = np.dot(w_inicial, matrixP)
for i in range(0, 4):
    w_power5 = np.dot(w_power5, matrixP)
# Calcular w_power100
w_power100 = np.dot(w_inicial, matrixP)
for i in range(0, 99):
    w_power100 = np.dot(w_power100, matrixP)
# A soma de todos os elementos destes vetores eh 1

"""
import numpy as np

x = np.arange(9).reshape((3,3))
y = np.arange(3)

print np.dot(x,y)   --> multiplicacao de matrizes

Como gerar uma matriz atraves de listas
a = [1, 5, 10]
b = [5, 2, 3]
c = [4, 7, 2]
mat = [a, b, c]

P = np.matrix(mat)
"""
