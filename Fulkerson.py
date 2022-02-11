from collections import defaultdict
from itertools import chain

class Edge():
    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity= capacity

    def __repr__(self):
        return "%s -> %s : %d" % (self.source, self.sink, self.capacity)

class Graph:

    def __init__(self):
        self.edges = {}
        self.adjacents = {}

    def add_edges(self, source, sink, capacity):
        if source == sink: 
            raise ValueError("Source cannot be the sink")
        edge1 = Edge(source, sink, capacity)
        edge2 = Edge(source, sink,capacity)

        self.edges[edge1] = 0
        self.edges[edge2] = 0

        if source not in self.adjacents:
            self.adjacents[source] = []
        if sink not in self.adjacents:
            self.adjacents[sink] = []

        self.adjacents[source].append(edge1)
        self.adjacents[sink].append(edge2)

    def display_graph(self):
        unique = list(self.edges.keys())
        result = []
        for i in range(len(unique)):
            if unique[i].__repr__() not in result:
                result.append(unique[i].__repr__())

        for val in result:
            print(val)

    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, path):

        if s == t: 
            return path
        for edge in self.adjacents[s]:
            if edge not in path:
                if edge.capacity - self.edges[edge] > 0:
                    return self.searching_algo_BFS(edge.sink, s, path + [edge])
        return None
    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):

        path = self.searching_algo_BFS(source, sink, [])

        while (path):
            max_flow = min([edge.capacity for edge in path])
            for edge in path:
                self.edges[edge] += max_flow
            path = self.searching_algo_BFS(source, sink, [])
    
        return  sum([self.edges[edge] for edge in self.adjacents[source]]) - 1

t = Graph()

t.add_edges('s', 'o', 3)
t.add_edges('s', 'p', 3)
t.add_edges('o', 'p', 2)
t.add_edges('o', 'q', 3)
t.add_edges('p', 'r', 2)
t.add_edges('q', 'r', 4)
t.add_edges('r', 't', 3)
t.add_edges('q', 't', 2)


t.display_graph()
# print(result)
# t.add_edges('s', 'a', 10)
# t.add_edges('s', 'b', 10)
# t.add_edges('a', 'b', 2)
# t.add_edges('a', 'd', 8)
# t.add_edges('b', 'd', 9)
# t.add_edges('a', 'c', 4)
# t.add_edges('a', 'd', 8)
# t.add_edges('d', 't', 10)
# t.add_edges('c', 't', 10)

print (t.ford_fulkerson('s', 't'))