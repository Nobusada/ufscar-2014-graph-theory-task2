"""
Trabalho T2 da disciplina Teoria dos Grafos, ministrada em 2014/02
                    'All Hail Gabe Newell'
    Alunos:
        Daniel  Nobusada                    344443
        Thales Eduardo Adair Menato         407976
        Jorge Augusto Bernardo              407844
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#   Importa grafo Zachary's Karate Club
graphG = nx.read_gml('karate.gml')
"""
1)  Computacao da distribuicao estacionaria teorica (steady state) do grafo
    w(i) = d(vi) / 2|E|
"""
w_real = []
for i in graphG.nodes_iter():
        aux = float(graphG.degree(i)) / float((2 * graphG.number_of_edges()))
        w_real.append(aux)
"""
2)  Calcular The Power Method
    http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/
    downloads/c10s3.pdf
"""
#   Matriz P recebe a matriz de adjacencia de matrixG
matrixP = nx.adjacency_matrix(graphG)
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
w_inicial = np.array([1.0/float(graphG.order())
                      for i in range(0, graphG.order())])
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
3)  Escolha de 2 vertices distintos e realizar a caminhada aleatoria de ambos
"""
# Funcao Random Walk
def random_walk(node, numPassos):
    #   Vetor contendo numero de posicoes = numeros de vertices(noh)
    caminhada = [0.0 for i in range(0, graphG.number_of_nodes())]
    #   Para o numero de passos desejado, uma lista contendo os vizinhos sera armazenada
    #   um indice aleatorio desta lista eh selecionado como proximo noh que entao passa
    #   a ser o noh atual e numero de visitar naquele noh eh incrementado
    for i in range(0, numPassos):
        vizinhos = graphG.neighbors(node)
        proxNo = vizinhos[np.random.randint(0, len(vizinhos))]
        node = proxNo
        caminhada[node-1] += 1
    #   Realiza a divisao pelo numero de passos em todos os numeros de lista
    for i in range(0, len(caminhada)):
        caminhada[i] /= numPassos
    #   Retorna vetor contendo o numero de passadas / num de passos em cada vertice (noh)
    return caminhada

# Escolha de dois vertices (noh) aleatorios
nodeA = np.random.random_integers(1, graphG.number_of_nodes())
nodeB = np.random.random_integers(1, graphG.number_of_nodes())
# Caso vertice B seja igual a A, receber outros numeros ateh que sejam distintos
while nodeB is nodeA:
    nodeB = np.random.random_integers(1, graphG.number_of_nodes())
# 2 caminhadas aleatorias de tamanho N = 100
w_random100a = random_walk(nodeA, 100)
w_random100b = random_walk(nodeB, 100)
# 2 caminhadas aleatorias de tamanho N = 10000
w_random10000a = random_walk(nodeA, 10000)
w_random10000b = random_walk(nodeB, 10000)

# Print no console de todos os dados obtidos
print "w_power5: "
w_power5_lista = []
for i in range(0, w_power5.size):
    w_power5_lista.append('%.4f'%w_power5[0, i])
print w_power5_lista

print "w_power100: "
w_power100_lista = []
for i in range(0, w_power100.size):
    w_power100_lista.append('%.4f'%w_power100[0, i])
print w_power100_lista

print "w_random100a:"
print w_random100a

print "w_random100b:"
print w_random100b

print "w_random10000a:"
print w_random10000a

print "w_random10000b:"
print w_random10000b
