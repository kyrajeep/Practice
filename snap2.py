"""
There’s a knight in cell (x, y) of a 8x8 chess board, write a function to return all possible cells the knight might be in after k steps, and the number of different paths to travel to that cell.

For example
((0, 0), 1) Returns {(1, 2): 1, (2, 1): 1}

((0, 0), 2) Returns {(0, 0): 2, (3, 3): 2, (0, 4): 1, (2, 4): 1, (2, 0): 1, (3, 1): 1, (1, 3): 1, (0, 2): 1, (4, 2): 1, (4, 0): 1}


http://www.chesscorner.com/tutorial/basic/knight/knight.htm


moves = [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1)]
"""
moves = [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1)]
def movements(loc, steps):
    moves = [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1)]
    while steps > 0:
        for i in moves:
            result = [sum(x) for x in zip(loc,i)] # (1, 2)  + (3, 4) = (1, 2, 3, 4)
        steps -= 1 
    return result

def check(result):
    stored_moves = {}
    if 0<=result[0] and result[0]<=7 and 0<=result[1] and result[1]<=7:
        if result not in stored_moves.keys():
            stored_moves[result] = 1
        else:
            stored_moves[result] += 1
    
    
def helper(stored_moves, loc, steps):
    result = movements(loc, steps)
    check(result)
check(movements((0,0), 2))  

        
    
        
#print(movements((0,0), 1))
        
            
        

