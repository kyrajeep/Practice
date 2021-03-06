import math

def reverse(list1):

#a function to reverse order of a list. It takes in
#a list and returns a list

    #initialize the i to enter into a loop
    i = 0
    
    while i <= (len(list1)-1):
        # a for loop that swaps values up until 
        # half of the list length.
        for i in range(math.ceil((len(list1)-1)/2)):
            a = list1[i]
            list1[i] = list1[len(list1)-1-i]
            list1[len(list1)-1-i] = a
        
        return list1
    
       
def test_reverse():

#a test function for reverse

    if reverse([1,2]) == [2,1]:
        print("length 2 passed")
    if reverse([3, 2, 5]) == [5, 2, 3]:
        print("length 3 passed")
    if reverse([4, 7, 17, 19]) == [19, 17, 7, 4]:
        print("length 4 passed")
    if reverse([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]:
        print("length 6 passed")
test_reverse()
reverse([0,2])