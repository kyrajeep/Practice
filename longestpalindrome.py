class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        # return the index where a palindrome could be
        indices= self.find(s)
        indices_one = self.find_one(s)
        # gothrough the list of palindromes
        self.iterate_palin(s,indices,palindromes)
        
        self.iterate_palin(s,indices_one,palindromes)
        
        return max(palindromes)
    def find(self, s):
        indices = []
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                indices.append(i)
            
        return indices
    def find_one(self, s):
        
        indices_one = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                indices_one.append((i,i+1))
            
        return indices_one
        
    def iterate_palin(self,s,indices,palindromes):
        if indices:
            
            for i in indices:
                condition = True
                j = 1
                while condition is True:
                    if i-j >=0 and i+j < len(s): 
                
                        if s[i-j] == s[i+j]:
                            j += 1
                        else: 
                            condition = False
                            if 
                            palindromes.append(s[i:i+2+1])
                            
                    else:
                        
                        palindromes.append(s[i:i+2+1])
                        condition = False
            return
        else:
            return
            