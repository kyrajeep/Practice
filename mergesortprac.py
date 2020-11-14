# input: unsorted list
# output: sorted list
# Do you know how it works? break down the elements until there is only 
# one element and sort them recursively. 

def mergesort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        #print(left)
        right = A[mid:]
        #print(right)
        mergesort(left)
        mergesort(right)
        
        result = []
        index_l=0
        index_r=0
        index_result = 0 
        #why can't the while loop be indented in?
        while len(left) > 0 and len(right) > 0:
        # pay attention to the indices here:
            #print(index_l, index_r)
            if left[index_l] > right[index_r]:
                print(index_result, index_r)
                result.append(right[index_r])
                index_r += 1 #mistake: now we are incrementing indefinitely
            else:
                result.append(left[index_l])
                index_l += 1
            
             

        while len(left) > 0:
            result.append(left[index_l])
            index_l += 1
            #index_result += 1
        while len(right) > 0:
            result[index_result].append(right[index_r]) 
            index_r += 1
            #index_result += 1
        return result

    
    
print(mergesort([3,1,2,9]))

   