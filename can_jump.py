# almost but no cigar
# think about the simple cases that are wrong in the beginning.
# but you did do a really good job. Fantastic work!
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp = [0] * len(nums)
        if len(nums) <= 1:
            if nums == []:
                return False
            else:
               
                
                return True
        else:
            if nums[0] == 0:
                return False
            target = len(nums) - 1
       
            i = 0 # where I start
        # stopping condition is if we traversed through the whole thing.
            for i in range(target):
            
                j = nums[i]
                if j >= 1:
                    for k in range(1, j+1): # for all the possible steps
                        print(k)
                        l = nums[i+k] # the value stored in the list
                        if l+i+k >= target:
                            return True
                else:
                     continue
            
            return False