class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0 
        rows, columns = len(grid), len(grid[0])
        q = collections.deque()
        visited = []
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(row, column):
        # add the first element
            current = [row, column]
            q.append(current)
            visited.append(current)
            while q:
                current = q.popleft()
                for i in directions:
                # add the adjacent elements
                    dir = current + i
                    if dir not in visited:
                        q.append(dir)
                    
                    
            return visited, result
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and [i,j] not in visited: 
                    bfs(i,j)
        return result
