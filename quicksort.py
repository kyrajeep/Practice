# Referenced Hackerrank's Quicksort video on YouTube.
# Why is it optimal? Space: O(1). We do not need extra space to store all the sorted variables.
# The time is not optimal in worst case but it is used because of the space complexity.
# Also enables parallelization
# partition and then put it togethr
# input: list
# output: sorted list via quicksort
def quicksort(A, left, right):
    # the equal in greater or equal is very important. otherwise it errors
    if left >= right:
        return
    else:
        pivot = A[(left+right)//2]
        part_loc = partition(A, left, right, pivot)
        quicksort(A, left, part_loc-1)
        # we sort through the elements supposed smaller than pivot
        #print(left, right)
        # the index right is constantly updated in partition
        quicksort(A, part_loc, right)
        return A

def partition(A,left, right, pivot):
    # inputs: left = left index, right = right index
    # pivot: gets changed at each iteration to speed up
    while left <= right:
        while A[left] < pivot:
            # increment the left index until I find an element smaller than pivot
            left += 1
        while A[right] > pivot:
            right -= 1
        if left <= right:
            # swap elements in-place if they are not ordered
            # we can break out of the top while loop if ordered
            A[left], A[right] = A[right], A[left]
            left += 1 # go to the next index to check if smaller/bigger than pivot
            right -= 1
    return left  # returns the left as the new pivot


print(quicksort([1, 3, 2, 9, 1], 0, 4))
print(quicksort([1,9,2,4,2,7,9,8,11,12], 0, 9))     