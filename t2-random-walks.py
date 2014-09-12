""" Trabalho T2 da disciplina Teoria dos Grafos, ministrada em 2014/02
"""
import networkx as nx

G = nx.read_gml('karate.gml')
w_real = []

for i in G.edge:
        aux = (len(G.edge[i]) * 1.0) / (2 * len(G.nodes()))
        w_real.append(aux)

