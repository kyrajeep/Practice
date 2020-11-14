def searchit(A, x):
    begin = 0
    end = len(A) - 1
    result = -2
    
    while begin <= end:
        
        mid = (end + begin) // 2
        #print(mid)
        if A[mid] > x:
            #print(1)
            end = mid -1
            
        elif A[mid] < x:
            #print(2)
            begin = mid + 1
        else:
            #print(3)
            result = mid
            end = mid - 1
    return result


print(searchit([1,2,3,4,5,6,7,8,8,9,10],8))