import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

dictPlayers = {}
frame = pd.read_excel('reprezentacja.xlsx')
columnss = frame.columns[1::]
listWeights = [0.5, 1, 2]
listColors = ['r', 'm', 'c']


def nodziarz(lista):
    for node in lista:
        G.add_node(node)
    return True


def czeker(frame, columns, nm_col, row, param):
    if int(frame[columns[nm_col]][row]) < param:
        return 1
    else:
        return 0


for index, player in enumerate(frame[columnss[1]]):
    temp = {}
    dictPlayers[player] = temp
    temp['mecze'] = czeker(frame, columnss, 3, index, 30)
    temp['wiek'] = czeker(frame, columnss, 2, index, 25)
    temp['liga'] = frame[columnss[5]][index]

for player in frame[columnss[1]]:
    temp = dictPlayers[player]
    for player1 in frame[columnss[1]]:
        if player != player1:
            temp1 = dictPlayers[player1]
            if temp1['mecze'] == temp['mecze'] and temp1['wiek'] == temp['wiek']:
                G.add_edge(player, player1, color=listColors[0], weight=listWeights[0])
            if temp1['wiek'] == temp['wiek'] and temp1['liga'] == temp['liga']:
                G.add_edge(player, player1, color=listColors[1], weight=listWeights[1])
            if temp1['mecze'] == temp['mecze'] and temp1['liga'] == temp['liga']:
                G.add_edge(player, player1, color=listColors[2], weight=listWeights[2])

# WSKAŹNIKI#
degree = nx.number_of_nodes(G)
size = nx.number_of_edges(G)
density = 2 * size / degree * (degree - 1)
centrality = nx.degree_centrality(G)
closeness = nx.closeness_centrality(G)
print(f'Ilość wierzchołków: {degree}\nIlość krawędzi: {size}\nGęstość: {density}\nStopień centralności:\n{centrality}\nBliskość:\n{closeness}')

nx.draw(G, edge_color=listColors, width=listWeights)
plt.show()
