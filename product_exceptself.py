# converted from pseudocode
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output=[]
        length = len(nums)
        cur = 1
        for i in range(length):
            cur = cur * nums[i]
            prefix.append(cur)
        print(prefix)
        cur = 1
        for j in reversed(range(length)):
            print(j)
            cur = cur * nums[j]
            postfix.insert(0,cur)
        print(postfix)
        for k in range(length):
            if k == 0:
                output.append(postfix[k+1])
            elif k == length - 1:
                output.append(prefix[k-1])
            else:
                output.append(postfix[k+1] * prefix[k-1])
        return output
