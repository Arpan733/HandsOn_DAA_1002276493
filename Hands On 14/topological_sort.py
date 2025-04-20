from collections import defaultdict

def topological_sort(graph):
    visited_node = set()
    graph_stack = []

    def dfs(node):
        visited_node.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited_node:
                dfs(neighbor)
        
        graph_stack.append(node)

    graph_vertices = set(graph.keys())
    
    for neighbors in graph.values():
        graph_vertices.update(neighbors)

    for v in sorted(graph_vertices):
        if v not in visited_node:
            dfs(v)

    return graph_stack[::-1]


graph = defaultdict(list)

graph['m'].extend(['q', 'r', 'x'])
graph['n'].extend(['q', 'u', 'o'])
graph['q'].append('t')
graph['u'].append('t')
graph['o'].extend(['r', 's', 'v'])
graph['r'].extend(['u', 'y'])
graph['s'].append('r')
graph['p'].extend(['s', 'z', 'o'])
graph['y'].append('v')
graph['v'].extend(['x', 'w'])
graph['w'].append('z')

result = topological_sort(graph)

print("Topological Sort Order:")
print(result)
