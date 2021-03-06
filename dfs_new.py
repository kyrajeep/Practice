# A function to conduct dfs.
def dfs(graph, visited, node):
    print(node)
    if node not in visited:
        visited.append(node)
# Note to self: you made the mistake of putting the for loop in the same position as the if statement
        for i in graph[node]:
            #print(node)
            #print(i, node)
            dfs(graph, visited, i)
           
    return visited
    '''
     Note to self: 
     return is executed on the CURRENT FUNCTION CALL
     It terminates only the CURRENT FUNCTION CALL and goes back up to the previous 
     function call. 
     Because the for loop calls keys we had the key error. So need to
     specify if a key does not have any children.
     What if you encounter something that was already visited? Then it returns the list
     Is that what a DFS is? You should ask this.
    '''

# a directed graph
graph = {'A': ['B','C'], 'B': ['D', 'F'], 'D': ['E','F'], 'E': ['D'],'F': [], 'C': []}

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

def test(): # Problem: I am not entirely sure if this is correct. -> ask someone
    if dfs(graph, [], 'A') == ['A', 'B', 'D', 'E', 'F', 'C']:
        return True
    else:
        return False

#print(dfs(graph, [], 'A'))
print(dfs(graph, [], 'A'))












