# Returns count of possible paths to reach cell  
# at row number m and column number n from the  
# topmost leftmost cell (cell at 1, 1) 
def numberOfPaths(m, n): 
    # Create a 2D table to store 
    # results of subproblems. what if there are too many? 
    count = [[0 for x in range(m)] for y in range(n)] 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for i in range(n): 
        count[i][0] = 1; 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for j in range(m): 
        count[0][j] = 1; 
    # Calculate count of paths for other 
    # cells in bottom-up manner using the 
    # recursive solution 
    for i in range(1, m): 
        for j in range(1, n):              
            count[i][j] = count[i-1][j] + count[i][j-1] 
    
    return count[m-1][n-1] 
  
# Driver program to test above function  
m = 3
n = 2
print( numberOfPaths(m, n)) 
  
# This code is contributed by Aditi Sharma and I fixed a bug 
# on dimension errors
# how to test this code?