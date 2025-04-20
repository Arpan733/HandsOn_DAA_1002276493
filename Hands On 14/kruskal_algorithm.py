class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def find_node(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_node(self.parent[node])
        
        return self.parent[node]

    def node_union(self, u, v):
        root_u = self.find_node(u)
        root_v = self.find_node(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class KruskalAlgorithm:
    def __init__(self):
        self.graph_edges = set()
        self.graph_nodes = set()

    def add_edge_to_graph(self, u, v, weight):
        self.graph_edges.add((weight, u, v))
        self.graph_nodes.update([u, v])

    def algorithm(self):
        disjoint_set = DisjointSet()

        for node in self.graph_nodes:
            disjoint_set.make_set(node)

        mst = []
        total_weight = 0

        for w, u, v in sorted(self.graph_edges):
            if disjoint_set.find_node(u) != disjoint_set.find_node(v):
                mst.append((u, v, w))
                total_weight += w
                disjoint_set.node_union(u, v)

        return mst, total_weight


kruskal_graph = KruskalAlgorithm()

kruskal_graph.add_edge_to_graph('a', 'b', 4)
kruskal_graph.add_edge_to_graph('a', 'h', 8)
kruskal_graph.add_edge_to_graph('b', 'h', 11)
kruskal_graph.add_edge_to_graph('b', 'c', 8)
kruskal_graph.add_edge_to_graph('c', 'i', 2)
kruskal_graph.add_edge_to_graph('c', 'f', 4)
kruskal_graph.add_edge_to_graph('c', 'd', 7)
kruskal_graph.add_edge_to_graph('d', 'e', 9)
kruskal_graph.add_edge_to_graph('d', 'f', 14)
kruskal_graph.add_edge_to_graph('e', 'f', 10)
kruskal_graph.add_edge_to_graph('f', 'g', 2)
kruskal_graph.add_edge_to_graph('g', 'h', 1)
kruskal_graph.add_edge_to_graph('g', 'i', 6)
kruskal_graph.add_edge_to_graph('h', 'i', 7)

mst, total_weight = kruskal_graph.algorithm()

print("Edges in the Minimum Spanning Tree (MST):")

for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with weight {weight}")

print(f"Total weight of MST: {total_weight}")