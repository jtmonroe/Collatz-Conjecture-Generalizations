from Graph import Graph
from Queue import Queue
import networkx as nx
import matplotlib as plt

#Pseudocode algorithm
# Structures:
    #1: Graph built with dict and sets
    #2: queue for frontier nodes

#Start at root 1 and take 2 functions
    #first function: 2x
    #Second function: if x-1 is divisible by k, then (x - 1)/k

#If the second function is used, then add that node to the frontier queues

#Discontinue when frontier is of a certain size

def collatz_tree(M, k = 3):
    tree = Graph()
    tree.add_vertex(1)
    frontier = Queue()
    frontier.push(1)
    while len(frontier) < M:
        x = frontier.pop()
        if (x - 1) % k == 0:
            y = (x - 1)//3
            if y not in tree:
                tree.add_vertex(y)
                tree.add_edge(x, y)
                frontier.push(y)
        z = 2*x
        if z not in tree:
            tree.add_vertex(z)
            tree.add_edge(x, z)
            frontier.push(z)
    return tree

def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent != None:   #this should be removed for directed graphs.
        neighbors.remove(parent)  #if directed, then parent not in neighbors.
    if len(neighbors)!=0:
        dx = width/len(neighbors) 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                                parent = root)
    return pos

K = 7
list_ = []
graph = collatz_tree(50, K)

Matching_Graph = nx.Graph()
for Vertex in graph.edge_list:
    Matching_Graph.add_node(Vertex)
    list_.append(Vertex)

for Vertex in graph.edge_list:
    for other in graph.edge_list[Vertex]:
        Matching_Graph.add_edge(Vertex, other)

pos = hierarchy_pos(Matching_Graph, 0, width=1000, vert_gap=100)

###DRAW NODES
nx.draw_networkx_nodes(Matching_Graph, pos,
                       nodelist=list_,
                       node_color='b',
                       node_size=600,
                       alpha=0.6)

### NODE LABELS
labels = {}
for i in list_:
    labels[i] = str(i)
nx.draw_networkx_labels(Matching_Graph, pos, labels, font_size=20)

#DRAW EDGES
nx.draw_networkx_edges(Matching_Graph, pos, width=1.0, alpha=0.5)

plt.pyplot.axis('off')
plt.pyplot.savefig("Collatz_Tree.png")
