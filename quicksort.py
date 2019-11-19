def quicksort(A, left, right):
    if left >= right:
        return
    pivot = A[(left + right)//2]
    part_point = partition(A, left, right, pivot)
    quicksort(A, left, part_point-1)   # a little unsure about the indices here
    quicksort(A, part_point, right)    # at part_point :)
    return A
def partition(A, left, right, pivot):
    while left <= right:
    # because we are going to increment and decrement left and right
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1
        # got the following line wrong. makes sense: when we hit the right elements and 
        # if the order is switched we switch them over.
        if left <= right:
            A[left], A[right] = A[right], A[left]
            # forgot the following part too. makes sense. move on to the next elem
            left += 1
            right -= 1
    return left

    
    
A = [1,4,3,2,9]
print(quicksort(A, 0, 4))

