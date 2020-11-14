def merge(A):
    # recursion is a more straightforward way of implementing mergeSort over iteration.
    # I forgot how the partitioning works...
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        
        merge(L)
        merge(R)
    
        i = j = k = 0
        #counting the elements this way
        while i < len(L) and j < len(R):
            print(i,j)
            if L[i] > R[j]:
                A[k] = R[j]
                j += 1
            else:
                A[k] = L[i]
                i += 1
            k += 1
        # this works because if both elements were left, the above loop would have peretuated. 
        # only one of these while loops will execute.
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k +=1
    return A

print(merge([1,4,2]))
print(merge([1,8,2,12,9]))