#A simple implementation of the top method in class stack!
class stack:
    def top(self, l):
        #the top method takes in an array l.
        
        if l[len(l)-1] == None:
            #if the top element is None, it returns an error.
            print("Error")
        else:
            #otherwise it returns the top element
            print(l[len(l)-1])

    
    def push(self, l,x):
        l.append(x)
        print(l)
   
l = [1,2,3,4]
s = stack()
s.top(l)
s.push(l,5)
#python has a built-in pop function for a list interface.
l.pop(len(l)-1)
print(l)