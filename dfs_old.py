graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
# passing in visited.
def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, visited, n)
    
    return visited

visited = dfs(graph1, [], 'A')
print(visited)
   