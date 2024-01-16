class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.isspace():
            return True
        s = s.lower()
        clean_string = [string for string in s if string.isalnum()]
      
    # rejoin intermediate list into a string
        clean_string = "".join(clean_string)
        print(clean_string)
        pointer1 = 0
        pointer2 = len(clean_string) - 1
        while pointer1 < pointer2:
            
            if clean_string[pointer1] == clean_string[pointer2]:
                pointer1 += 1
                pointer2 -= 1
         
            else: 
                return False
        return True
