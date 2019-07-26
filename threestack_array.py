#there are three stacks
# each of them have push and pop and return top element functionalities.
#any other function I should consider?
#Let's start with the three!!
# can you make it so that the size would change????
# I think it's ok to put just push since I know how to do the rest


class threestacks:
    def __init__(self, size1, size2, size3, array_size):
        
        self.size1 = size1
        self.size2 = size2
        self.size3 = size3
        
        self.array_size = array_size
        self.array_total = [None for a in range(array_size)]
        

        # a class var. an array of size array_size. where should it be?
    
    def push(self, stack_number, element):
        #I do not want to use the if statement every single time. is there another way
        # I thought the array size does not change? This code is NOT for replacing. If I were 
        # replace it I suppose I would have to delete first? do not know how. should I know?
        if stack_number == 1:
            self.array_total.insert(self.size1,element) 
        elif stack_number == 2:
            self.array_total.insert(self.size2 + self.size1, element)
        elif stack_number == 3:
            self.array_total.insert(self.size3 + self.size2 + self.size1,element)
        
        else:
            print("Such array does not exist")
        
        #uh oh

if __name__ == "__main__":
    l = threestacks(1,2,3,6)
    print(l.array_total)
    l.push(2, 2)
    print(l.array_total)



    
