class Solution:
    # Given parentheses, make sure they are matched.
    # e.g. ()[],  ([{}])
    def isValid(self, s: str) -> bool:
        # Are there only 6 possibilities available?
        # Distinguish butween ()[] and ([])
        # Initialize the stack with 0 to avoid Empty List error.
        stack = [0]
        hashmap = {0: None, "}": "{", ")": "(", "]": "["}
        for i in reversed(range(len(s))):
            print(i, s[i])
            # Add to stack if }, ), or ]
            if s[i] in hashmap:
                stack.append(s[i])
            else:
                # If {, (, [, compare with the stack
                current = stack.pop()
                if hashmap[current] != s[i]:
                    return False
        return stack == [0]
