class Edge(object):
    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity= capacity

    def __repr__(self):
        return "%s -> %s : %d" % (self.source, self.sink, self.capacity)

class Graph(object):

    def __init__(self):
        self.edges = {}
        self.adjacents = {}

    def get_edges(self, v):
        return self.adjacents[v]

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

    def list_edges(self):
        unique = list(self.edges.keys())
        result = []
        for i in range(len(unique)):
            if unique[i].__repr__() not in result:
                result.append(unique[i].__repr__())

        for val in result:
            print(val)

    def list_nodes(self):
        nodes1 = []
        for node in self.edges.keys():
            nodes1.append(node.source)
            nodes1.append(node.sink)
        
        nodes2 = []
        for node in nodes1:
            if node not in nodes2:
                nodes2.append(node)
        return nodes2

    def display_graph(self):
        L = []
        for edge in self.edges:
            x = ("{} : {}({}) ".format(edge.source, edge.sink, edge.capacity))
            if x not in L:
                L.append(x)
        for i in L:
            print(i)        
        

    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, source, t, path):
        if source == t: 
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity -self.edges[edge]
            if residual > 0 and not edge in path:
                result = self.searching_algo_BFS(edge.sink, source, path + [edge])
                if result != None: 
                    return result
    
    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):

        path = self.searching_algo_BFS(source, sink, [])
        
        while (path):
            max_flow = min([edge.capacity for edge in path])
            for edge in path:
                self.edges[edge] += max_flow
            path = self.searching_algo_BFS(source, sink, [])
            
        return  sum([self.edges[edge] for edge in self.adjacents[source]])

t = Graph()





t.add_edges('s', 'a', 3)
t.add_edges('s', 'b', 2)
t.add_edges('a', 'b', 5)
t.add_edges('a', 't', 2)
t.add_edges('b', 't', 3)

# print(t.display_graph())
import unittest

class TestGraph(unittest.TestCase):
    def setUp(self):

        self.network1 = Graph()
        self.network1.add_edges('s', 'a', 3)
        self.network1.add_edges('s', 'b', 2)
        self.network1.add_edges('a', 'b', 5)
        self.network1.add_edges('a', 't', 2)
        self.network1.add_edges('b', 't', 3)

        self.network2 = Graph()
        self.network2.add_edges('s', 'v', 8)
        self.network2.add_edges('s', 'w', 8)
        self.network2.add_edges('v', 'w', 1)
        self.network2.add_edges('v', 't', 8)
        self.network2.add_edges('w', 't', 8)
        
    def test_ford_fulkerson(self):
        self.assertEqual(self.network1.ford_fulkerson('s', 't'), 5)
        self.assertEqual(self.network2.ford_fulkerson('s', 't'), 16)

if __name__ == '__main__':
    t.display_graph()
    unittest.main() 
    
