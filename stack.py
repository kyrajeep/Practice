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
        

  #  def pop():

   # def push():
l = [1,2,3,4]
s = stack()
s.top(l)