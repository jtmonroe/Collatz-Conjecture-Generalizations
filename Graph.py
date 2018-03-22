class Graph(object):
    __slots__ = ['edge_list', 'directed']
    """An attempt to simplify the basics of a graph in python using
    one dictionary. Does not support weighted edges."""
    def __init__(self):
        self.edge_list = {}
        self.directed = False

    def __len__(self):
        return len(self.edge_list)

    def __str__(self):
        string = ""
        for Vertex in self.edge_list:
            if len(self.edge_list[Vertex]) == 0:
                string += (str(Vertex) + ": \n")
                continue
            vals = str(self.edge_list[Vertex])
            string += (str(Vertex) + ": " + vals[1:len(vals)-1] + "\n")
        return string

    def __contains__(self, elem):
        return (elem in self.edge_list)

    def add_vertex(self, label):
        if label in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        self.edge_list[label] = set()

    def del_vertex(self, label):
        if label not in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        del self.edge_list[label]
        #TODO Remove all mentions of vertex from friends

    def add_edge(self, label1, label2):
        if label1 not in self.edge_list or label2 not in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        self.edge_list[label1].add(label2)
        self.edge_list[label2].add(label1)

    def del_edge(self, label1, label2):
        if label1 not in self.edge_list or label2 not in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        self.edge_list[label1].remove(label2)
        self.edge_list[label2].remove(label1)

    def add_edge_dir(self, start, to):
        if start not in self.edge_list or to not in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        self.edge_list[start] = to
        self.directed = True

    def del_edge_dir(self, start, to):
        if start not in self.edge_list or to not in self.edge_list:
            raise LookupError("Vertex is not in Graph")
        self.edge_list[start].remove(to)

    def complement(self):
        total_Vertex = set(self.edge_list)
        complement = Graph()
        for Vertex in total_Vertex:
            complement.edge_list[Vertex] =\
                (total_Vertex - self.edge_list[Vertex]) - {Vertex}
        return complement

    def degree(self, vertex):
        if self.directed is False:
            return len(self.edge_list[vertex])
        to_return = len(self) - 1
        for Vertex in self.edge_list:
            if vertex not in self.edge_list[Vertex]:
                to_return -= 1
        return to_return
