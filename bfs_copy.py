from collections import defaultdict
#create the graph object as a defaultdict. what if they give you the graph? would make it easier

class Graph:
    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def bfs(self, s):
        #print(len(self.graph))
        visited = [False] * (len(self.graph))

        queue = []
        queue.append(s)
        # I actually forgot this part!
        visited[s] = True
        while queue:
            a = queue.pop(0)
            #print(a)
            for i in self.graph[a]:
                print(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    #print(i)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(1, 4) 
g.addEdge(1, 5) 
 

g.bfs(0)