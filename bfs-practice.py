def BFS(graph):
    queue1 = []
    #queue1.append(node)
    result = []
    for i in graph.keys():
        #double check with the index
        queue1.append(graph[i])
        element = queue1.pop()
        result.append(element)
    while queue1:
        element = queue1.pop()
        result.append(element)
    return result

A = {1: [2,3], 2: [4,5], 3: [6,7], 4: [8]}
print(BFS(A))
        