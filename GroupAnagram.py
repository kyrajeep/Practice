#Questions:
#how should I take in a class input?
class Solution:
    def __init__(self, list2):
        #what are the advantage of initializing types in the constructor
        #well, it is a class variable so it is in the constructor
        self.list2 = list2
        self.types = []
        self.result = []
    def groupAnagrams(self):
        #create empty arrays for storing letters for each element and for saving the result
        
        #first of all, add to types the letters of the first element of the input
        #is it a legitimate choice to just input a number?
        #go through the input list to see if the word matches any element in types
        for i in range(len(self.types)):

            # start at the 2nd element
            for j in range(len(self.list2)):
                if self.match(list2[j], types[i]):
                    self.result.append(self.list2[j])
                    break
                else: 
                    self.addNewElement(i+1)
                    
        
       
    def addNewElement(self, number):
        #this is a helper function for a new element that did not have the same letters 
        #as types before. takes in a number which represents the specific word
        for i in range(len(self.list2[number])):
            self.types[number].append(self.list[number][i])
            self.result[number].append(self.list[number])
                
                
    def match(self, list3, types2):
        #one string at a time
        # one type at a time
        # a helper function for seeing if all letters in the string matches the 
        #have to go through one type at a time, no? 
    # so have the input of types and the word??       
#input: list, one element in types
        #output: boolean
        # see if each letter in the list is in types
        #list1 is the current list in types
        #go through types[0] then 
        for i in range(len(list3)):
            for j in range(len(types2)):
                if list3[i] not in types2:
                    return False
        return True
                
                
               
#don't do something immediately


     
        
            
sol = Solution(["eat", "tea", "tan", "ate", "nat", "bat"])
sol.
sol.groupAnagrams()
print(sol.result)