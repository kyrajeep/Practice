class Solution:
    def removeDuplicates(self, nums):
        curr_idx = 0

        while curr_idx < len(nums) - 1:     # iterating through nums list till next-to-last element (curr_idx + 1 always checked)
            if nums[curr_idx] == nums[curr_idx+1]:  # if current and next element are the same
                del nums[curr_idx]          # current element is deleted
                curr_idx -= 1               # to stay at the same place in list, we have to dicrease 1 (1 will be added in the next step)
            curr_idx += 1                   # going further in the list

        return len(nums)
    
    """
    what's important here is the fact, that in while loop condition is checked with every step,
    so len(nums) when del is decreasing and will not cause index error in the end of iteration
    as in for loop
    """
test = Solution()
print(test.removeDuplicates([1,1,2,2]))
print(test.removeDuplicates([1,1,2,2,3,3,3]))