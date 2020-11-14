def merge(A):
    if len(A) > 1:
        mid = len(A) // 2 
        L = A[:mid]
        R = A[mid:]
        merge(L)
        merge(R)

        i = j = k = 0
        # made another mistake. Do you understand what the iterator is doing?
        # for each function call, the length of L is not changing. It is only with different function calls
        # Note the iterator (incrementing part) is i and j.
        while len(L) > i and len(R) > j:
            if L[i] > R[j]:
                A[k] = R[j]
                j += 1
                
            else:
                A[k] = L[i]
                i +=1
            k+=1
        # again, the same mistake
        while len(L) > i:
            A[k] = L[i]
            k += 1
            i += 1
        # again, the same mistake. Which iterator are we going through? j and i right?
        # and we are incrementing. length of R is not changing in the while statement
        while len(R) > j:
            A[k] = R[j]
            k += 1
            i += 1
    return(A)
print(merge([9,8,3,2,1]))