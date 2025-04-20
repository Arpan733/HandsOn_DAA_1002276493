class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class KruskalAlgorithm:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal(self):
        self.edges.sort()
        disjoint_set = DisjointSet(self.vertices)

        mst = []
        total_weight = 0
        for weight, u, v in self.edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                mst.append((u, v, weight))
                total_weight += weight
                disjoint_set.union(u, v)

        return mst, total_weight


node_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
index_to_node = {v: k for k, v in node_to_index.items()}

kruskal = KruskalAlgorithm(9)
kruskal.add_edge(node_to_index['a'], node_to_index['b'], 4)
kruskal.add_edge(node_to_index['a'], node_to_index['h'], 8)
kruskal.add_edge(node_to_index['b'], node_to_index['h'], 11)
kruskal.add_edge(node_to_index['b'], node_to_index['c'], 8)
kruskal.add_edge(node_to_index['c'], node_to_index['i'], 2)
kruskal.add_edge(node_to_index['c'], node_to_index['f'], 4)
kruskal.add_edge(node_to_index['c'], node_to_index['d'], 7)
kruskal.add_edge(node_to_index['d'], node_to_index['e'], 9)
kruskal.add_edge(node_to_index['d'], node_to_index['f'], 14)
kruskal.add_edge(node_to_index['e'], node_to_index['f'], 10)
kruskal.add_edge(node_to_index['f'], node_to_index['g'], 2)
kruskal.add_edge(node_to_index['g'], node_to_index['h'], 1)
kruskal.add_edge(node_to_index['g'], node_to_index['i'], 6)
kruskal.add_edge(node_to_index['h'], node_to_index['i'], 7)

mst, total_weight = kruskal.kruskal()

print("Edges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"Edge ({index_to_node[u]}, {index_to_node[v]}) with weight {weight}")

print(f"Total weight of MST: {total_weight}")
