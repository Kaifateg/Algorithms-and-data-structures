from collections import deque


class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


graph = DirectedGraph()
for value in ["A", "B", "C", "D"]:
    graph.add_vertex(value)

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


bfs(graph, "A")


class TheAdjacencyMatrix:
    def __init__(self, graphs):
        self.graph = [[0]*graphs for _ in range(graphs)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1

    def print_graph(self):
        for row in self.graph:
            print(row)


adjacency = TheAdjacencyMatrix(4)
adjacency.add_edge(0, 1)
adjacency.add_edge(1, 2)
adjacency.add_edge(2, 3)
adjacency.add_edge(3, 0)
adjacency.print_graph()

graph.print_graph()