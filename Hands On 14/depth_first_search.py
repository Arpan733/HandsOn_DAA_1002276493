from collections import defaultdict

class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def depth_first_search(self, start_node):
        visited_node = set()
        self.dfs_recursive(start_node, visited_node)

    def dfs_recursive(self, node, visited_node):
        if node in visited_node:
            return

        print(node, end=" ")
        visited_node.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited_node:
                self.dfs_recursive(neighbor, visited_node)


graph = GraphDFS()

graph.add_edge('u', 'v')
graph.add_edge('u', 'x')
graph.add_edge('v', 'y')
graph.add_edge('x', 'v')
graph.add_edge('y', 'x')
graph.add_edge('w', 'y')
graph.add_edge('w', 'z')
graph.add_edge('z', 'z')

print("Depth First Search starting from node 'u':")
graph.depth_first_search('u')
print()  