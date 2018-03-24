from Graph import Graph
from Queue import Queue
import networkx as nx
import matplotlib as plt
from sympy import isprime, primepi, prevprime, nextprime
from itertools import combinations

def general_collatz_tree(M, k = 3, root = 1):
    '''I am SO truly sorry for the running time
    of this algorithm. It has no choice but to be 
    exponential due to tree growth
    Generalization for all Collatz Trees'''
    tree = Graph()
    tree.add_vertex(root)
    frontier = Queue()
    frontier.push(root)
    primes = []
    p = k
    while True:
        try:
            p = prevprime(p)
        except:
            break
        primes.append(p)
    while len(tree) < M:
        x = frontier.pop()
        for i in range(len(primes) + 1):
            for tup in combinations(primes,i):
                y = x
                for prime in tup:
                    y = y*prime
                if y not in tree:
                    tree.add_vertex(y)
                    tree.add_edge(x, y)
                    frontier.push(y)
        if (x - 1)%k == 0:
            y = (x - 1)//k
            if y not in tree:
                tree.add_vertex(y)
                tree.add_edge(x, y)
                frontier.push(y)
    return tree

def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None, children = 2):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.
       MADE BY: JOEL @ https://stackoverflow.com/questions/29586520/can-one-get-hierarchical-graphs-from-networkx-with-python-3'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}    
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent != None:   #this should be removed for directed graphs.
        neighbors.remove(parent)  #if directed, then parent not in neighbors.
    if len(neighbors)!=0:
        dx = width/len(neighbors) 
        nextx = xcenter - width/children - dx/children
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                                parent = root)
    return pos

K = 5
CHILDREN = 2**(primepi(K - 1))
M = 86
FONT_SIZE = 0
NODE_SIZE = 2
DPI = 300
ROOT = 0
list_ = []

chosen_numbers = [5,7,9,10,11,13,14,16,17,20,21,22,23,25,26,27,30,32,34,35,36,37,39,40,41,42,44,47,49,51,52,54,56,57,58,59,61,63,64,65,66,68,71,73,76,77,79,81,83,84]

for M in chosen_numbers:
    graph = general_collatz_tree(M, K, root=ROOT+1)

    Matching_Graph = nx.Graph()
    for Vertex in graph.edge_list:
        Matching_Graph.add_node(Vertex)
        list_.append(Vertex)
    for Vertex in graph.edge_list:
        for other in graph.edge_list[Vertex]:
            Matching_Graph.add_edge(Vertex, other)
    pos = hierarchy_pos(Matching_Graph, ROOT, width=1000, vert_gap=100, children=CHILDREN)

    ###DRAW NODES
    nx.draw_networkx_nodes(Matching_Graph, pos,
                        nodelist=list_,
                        node_color='b',
                        node_size=NODE_SIZE,
                        alpha=0.6)

    ### NODE LABELS
    labels = {}
    for i in list_:
        labels[i] = str(i)
    nx.draw_networkx_labels(Matching_Graph, pos, labels, font_size=FONT_SIZE)

    #DRAW EDGES
    nx.draw_networkx_edges(Matching_Graph, pos, width=1.0, alpha=0.5)
    
    if len(str(M)) == 1:
        strM = "0" + str(M)
    else:
        strM = str(M)

    file_name = "Collatz_Tree_K" + str(K) + "_N" + strM + ".png"
    file_path = "Graph_Images/GIF/"+file_name
    plt.pyplot.axis('off')
    plt.pyplot.savefig(file_path, dpi = DPI)
    del Matching_Graph
