#input: 2Darray
# I would like to number the array and make it into a tree
# or should I make the positions into a tree?
# i am guessing the array goes like
#Input: 
 # [[Black, White, Exit], 
  # [White, Black, White],
   #[Enter, White, White]]
# output: path

# the positions are the nodes

# how do you return the position - index
def makegraph(A):
    for i in A:
# not sure about how to do this part    
def findpath(graph, visited, node):
    if node not in visited:
        visited.append(node)
        if graph[node]:
            for i in graph[node]:
                findpath(graph, visited, node)
    return visited
    

