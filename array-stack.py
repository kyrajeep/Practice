class arraystack:
    def __init__(self):
        self.head = 0
        #wait, slightly confused about this part. can initialize with head= tail = 0 and then augment in functions?
        # yes, but the code is cleaner this way if your initialization is the same each time.
        self.tail = 0
        self.max_size = 9
        self.array_stack = list()
        
        # should I make a stack attribute? Is that an attribute?

    def peek(self):
        if len(self.array_stack) <= 0:
            return ("Stack is empty")
        else:
            return self.array_stack[len(self.array_stack) - 1]

    def push(self, element):
        
        if len(self.array_stack) >= self.max_size:
            return ("Stack is full")
            
        else: 
            self.array_stack.append(element)
            self.tail += 1
          
    def popp(self):
        if len(self.array_stack) <= 0:
            return ("Stack is empty")
        else:
            self.array_stack.pop(len(self.array_stack)-1)
            self.tail -= 1


s = arraystack()
s.push(5)
print(s.peek())
s.popp()
print(s.peek())