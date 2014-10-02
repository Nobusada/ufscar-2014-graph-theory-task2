"""
Trabalho T2 da disciplina Teoria dos Grafos, ministrada em 2014/02
    Alunos:
        Daniel  Nobusada
        Thales Eduardo Adair Menato         407976
        Jorge Augusto Bernardo              407844
"""
import networkx as nx
import numpy as np

G = nx.read_gml('karate.gml')
w_real = []
_NUM_NODES = len(G.node)

for i in G.edge:
        aux = (len(G.edge[i]) * 1.0) / (2 * len(G.nodes()))
        w_real.append(aux)

a_m = nx.adjacency_matrix(G)
sum_a_m = []
for i in a_m:
    sum_a_m.append(i.sum())

p_aux_matrix = []
for i in range(0, _NUM_NODES):
    line_array = a_m[0].getA1()
    line = []

    for j in line_array:
        value = j / sum_a_m[i]
        line.append(value)

    p_aux_matrix.append(line)
p_matrix = np.matrix(p_aux_matrix)

w_power5 = np.multiply(p_matrix, p_matrix)
for i in range(0, 3):
    w_power5 = np.multiply(w_power5, p_matrix)

w_power100 = np.multiply(p_matrix, p_matrix)
for i in range(0, 98):
    w_power100 = np.multiply(w_power100, p_matrix)
