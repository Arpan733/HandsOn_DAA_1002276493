import heapq

class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.graph = {i: [] for i in range(vertices_count)}
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, start):
        edge_distances = {vertex: float('inf') for vertex in self.graph}
        edge_distances[start] = 0
        queue = [(0, start)]

        while queue:
            cd, cv = heapq.heappop(queue)

            if cd > edge_distances[cv]:
                continue

            for n, w in self.graph[cv]:
                distance = cd + w

                if distance < edge_distances[n]:
                    heapq.heappush(queue, (distance, n))
                    edge_distances[n] = distance

        return edge_distances


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

graph.dijkstra(0)

start_node = 0
shortest_distances = graph.dijkstra(start_node)

print(f"Shortest distances from node {start_node}:")
for node in range(graph.V):
    print(f"{start_node} -> {node} = {shortest_distances[node]}")