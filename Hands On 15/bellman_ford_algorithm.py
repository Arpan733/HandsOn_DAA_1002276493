def bellman_ford(graph, vertices, start):
    distances = {i: float('inf') for i in range(len(vertices))}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in graph:
        if distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances


graph_edges = [
    (0, 1, 6),
    (0, 3, 7),
    (1, 2, 5),
    (1, 3, 8),
    (1, 4, -4),
    (2, 1, -2),
    (3, 2, -3),
    (3, 4, 9),
    (4, 0, 2),
    (4, 2, 7),
]

vertices = ['A', 'B', 'C', 'D', 'E']

start_node = 0
shortest_distances = bellman_ford(graph_edges, vertices, start_node)

print(f"Shortest distances from {vertices[start_node]}:")

for node in range(len(vertices)):
    print(f"{vertices[start_node]} -> {vertices[node]} = {shortest_distances[node]}")
