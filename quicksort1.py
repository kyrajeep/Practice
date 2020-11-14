# Referenced Hackerrank's Quicksort video on YouTube.

# partition and then put it togethr
# input: list
# output: sorted list via quicksort
def quicksort(A, left, right):
    # the equal in greater or equal is very important. otherwise it errors
    if left >= right:
        return
    else:
        pivot = A[(left+right)//2]
        part_loc = partition(A,left, right, pivot)
        quicksort(A, left, part_loc-1)
        quicksort(A, part_loc, right)
        return A

def partition(A,left, right, pivot):
    while left <= right:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    return left


print(quicksort([1, 3, 2, 9, 1], 0, 4))
print(quicksort([1,9,2,4,2,7,9,8,11,12], 0, 9))     

   