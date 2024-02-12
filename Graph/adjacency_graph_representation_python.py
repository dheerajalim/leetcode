class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for edges in self.adj_list:
            print(edges)


vertices = 4

graph = Graph(vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)

graph.print_graph()
