class Solution:
    def merge(self, nums1, nums2, m, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
         
        # for loop: we know nums2 is of length n
        # nums1 needs to use the while loop since until
        # we find an element smaller than nums2
        # TODO: m does not include the 0 elements. 
        # edge cases: what if either or both are empty
        # if both are of length one: [0], [1] or [1], [0]
        
        if m == 0 and n == 0:
            nums1 = []
            return
            # if num2 has nonzero elements
        elif m == 0 and n >= 1:
            nums1.pop()
            nums1.insert(m, nums2[n-1])
            return
        elif m >= 1 and n == 0:
            return
        j = 0
        i = 0
        while j <= len(nums2) - 1 and i <= len(nums1)-1:
            if nums1[i] < nums2[j] and nums1[i] != 0:
                i += 1
            elif nums2[j] >= nums1[i] or nums1[i] == 0:
                    # if nums2 elemenet is bigger than current but smaller
                    # or equal to the next element in nums1
                    
                nums1.pop()
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
        return
                 
sol = Solution()
sol.merge([1,2,3,0,0,0], [2,5,6],m = 3, n = 3)