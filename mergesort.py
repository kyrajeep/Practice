def mergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        # when these functions are called recursively, the function call is not 
        # finished when the element length goes down to 1. 
        # So the calls pop back up again and again until the whole array is sorted.
        # when the functions are called but the calls are not finished, 
        # they are still running somewhere. They do not finish until the while loops
        # are also finished. 
        i = j = k = 0
        print(i,j,k)
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7, 8, 9, 1, 2]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
  