from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)

    for v in sorted(vertices):
        if v not in visited:
            dfs(v)

    return stack[::-1]

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
