class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # end when we reach n**2. board[n][n]
        visited = set()
        n = len(board)
        q = deque()
        q.append([1,0]) #encode the tile number and current result
        while q:
            number, result = q.popleft()
            for i in range(1,7):
                next = number + i
                r, c = self.numtoCoord(next)
                if next == n * n:
                    return result + 1
                if board[r][c] != -1:
                    next = board[r][c]
                if next not in visited:
                    result += 1
                    q.append(next, result)
                    visited.add(next, result)    
    def numtoCoord(self, next):
        # TODO
        pass
