#Using the two-pointer technique because the array is sorted.
#As long as nums[i] = nums[j], we increment j
#to skip the duplicate. What if they are not the same?

def arrayduplicate(nums):
        
    len_ = 1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        
        if nums[i] != nums[i-1]:
            nums[len_] = nums[i]
            
            len_ +=1
    return len_

print(arrayduplicate([1,2,3,3,4]))
