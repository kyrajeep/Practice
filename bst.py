#implement a binary search tree
#approximate the square root of a number?
# x * x = x^2
# why would you use a binary search for that? -> this is brilliant. 
# I think as I solve more problems it becomes more natural to think this way
# how would I write test cases
 # with integers I already know the answer to
# input: number n
# output: the square root 
# can I do a small example?
# what would be a suitable small example?
# if s * s = x then s is the output (solution)
# if s * s > x then solution < s
# if s * s < x then solution > s


# test cases : n = 4, sol = 2
# n = 8, sol = math.floor(math.sqrt(8))
# does the answer have to be an integer?
# If x is not a perfect square, then return floor(√x).
# 3 things to check. should I delegate it to a helper function
# there are three different responses depending on the output of this helper
# is n a global?
# how to respond to this helper
# should I create a class, a blueprint to print this out again and again?
import math
# n has to be a global variable. is the next line enough?

class squareroot:
# I decided to make this into a class because I am comfortable with it
# and also because I was having some issues passing around a global var
    def __init__(self, n):
        self.n = n
    
    def squarert(self):
        
# now implement the binary search
# start at 0
# how am I going to store variables and pass them around
# do i have problem wiht scope?
        m = self.n/2
    
        prev_small = 0
        prev_big = self.n
    
        while (abs(m - prev_big) > 0.01 and abs(m - prev_small) > 0.01):
            print("in while") 
        
            if self.squaretrue(m) == 0:
                #if self.isinteger(m):
                return m
                #else:
                 #   return math.floor(math.sqrt(m)) 
            
            if self.squaretrue(m) == 1:
            
                prev_big = m
                m = (prev_small + prev_big)/2
            if self.squaretrue(m) == 2:
            
                prev_small = m
            
                m = (prev_small + prev_big)/2    
    

# the helper function to check if the current number is a sqrt

    def squaretrue(self, m):
# have to save the previous iteration. i don't think it has to be a hash
# maybe an array
    
        if (m**2 == self.n) or abs(self.n-m**2) < 0.01:
            return 0
        elif m**2 > self.n:

            return 1
        elif m**2 < self.n:
            return 2
        # how to pass this around
        # smells like recursion
        # I have to call the previous. but only the previous

    def isinteger(self,k):
        if abs(k - int(k)) == 0:
            return True
        else:
            return False

#test cases
    def testsquarert():
#I tried to test the function, but ended up making it into a class so 
# could not use this test function
# I 
        pass
        if squarert(4) == 2:
            print("test for n = 4 passed")
        elif squarert(4) != 2:
            print("test for n = 4 failed")
        if squarert(8) == math.floor(math.sqrt(8)):
            print("test for n = 8 passed")
        elif squarert(8) != math.floor(math.sqrt(8)):
            print("test for n = 8 failed")


sqrtclass = squareroot(8)

print(sqrtclass.squarert())







