def remove_dup(A):
    i = 0
    while i < len(A)-1:
        print(i)
        if A[i] != A[i+1]:
            i += 1
            
        else:
            del A[i]
    return A

A = [1,2,3,4,4]
print(remove_dup(A))
 
