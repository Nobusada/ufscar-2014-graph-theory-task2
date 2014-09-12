""" Trabalho T2 da disciplina Teoria dos Grafos, ministrada em 2014/02
"""
import networkx as nx

G = nx.read_gml('karate.gml')
w_real = []

for i in G.edge:
        aux = (len(G.edge[i]) * 1.0) / (2 * len(G.nodes()))
        w_real.append(aux)

""""
def random_walk(initial_node, steps): #is expected that the initial node is the id of the node, and how many steps its gonna make
        while steps > 0:
            possible_nodes = G.edge[initial_node].keys()
            possible_nodes.sort()
            possible_nodes_odds = {}
            for i in possible_nodes:
                possible_nodes_odds[i] = w_real[i-1]
                #print possible_nodes_odds
                #return possible_nodes_odds
                #randomização do node escolhidos
            steps-=1
            random_walk(new_node, steps)
""""
