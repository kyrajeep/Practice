def remove_dup(A):
    hashtable = {}
    for i in A:
        hashtable[i] = False
    #for i in len(A): # might have some errors if we 
    # can we start from the back?
    # is it better to start from the back? maybe
    # what about the elements shifting? I don't think the shifting matters that much.
    # 
    j = 0
    while j < len(A):
        if hashtable[A[j]] == True:
            A.remove(A[j])
            
        elif hashtable[A[j]] == False:
            hashtable[A[j]] = True
            j += 1
    return A
        
#print(remove_dup([1,2,3]))
print(remove_dup([1,1,2,2,3]))
print(remove_dup([1,2,3,3,4,4]))
print(remove_dup([1, 3, 3, 6, 6, 7]))
print(remove_dup([1,1,1,3,3,2,2]))