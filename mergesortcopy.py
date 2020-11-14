def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = 0 
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
                
            else:
                arr[k] = L[i]
                i += 1
            k += 1
        # after comparing, for elements that are left because in the previous 
        # while loop we are comparing only while both arrays have positive length
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr
    


print(mergeSort([1,3,2,4]))
print(mergeSort([8,2,3,1,9,6,8,2]))
print(mergeSort([1,9,8,6,7,3,5,0,2,9,7,1]))