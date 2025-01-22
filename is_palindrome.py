class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove alphanumeric characters and convert to lowercase
        s = list(s)
        s = "".join(i for i in s if i.isalnum())
        s = s.lower()
        print(s)

        # Set two pointers
        first = 0
        second = len(list(s)) - 1
        s = list(s)
        while first < second:
            if s[first] == s[second]:
                first += 1
                second -= 1
            else:
                return False
        return True
