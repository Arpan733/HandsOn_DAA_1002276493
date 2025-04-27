class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.edges = []

    def addEdge(self, u, v, w):
        self.edges.append((u, v, w))

    def floyd_warshall(self):
        dist = {i: {j: float('inf') for j in range(self.V)} for i in range(self.V)}

        for i in range(self.V):
            dist[i][i] = 0

        for u, v, w in self.edges:
            dist[u][v] = w

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


graph = Graph(5)

graph.addEdge(0, 1, 6)
graph.addEdge(0, 3, 7)
graph.addEdge(1, 2, 5)
graph.addEdge(1, 3, 8)
graph.addEdge(1, 4, -4)
graph.addEdge(2, 1, -2)
graph.addEdge(3, 2, -3)
graph.addEdge(3, 4, 9)
graph.addEdge(4, 0, 2)
graph.addEdge(4, 2, 7) 

shortest_paths = graph.floyd_warshall()

print("All-pairs shortest distances matrix:")
print("    ", end="")

for v in range(graph.V):
    print(f"{v:^7}", end="")

print()

for u in range(graph.V):
    print(f"{u}  ", end=" ")

    for v in range(graph.V):
        value = shortest_paths[u][v]

        if value == float('inf'):
            print(f"{'INF':^7}", end="")
        else:
            print(f"{value:^7}", end="")

    print()
