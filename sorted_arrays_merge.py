import heapq
def merge_sorted_arrays(sorted_arrays):
    # we represent a heap as an array: read again(didn't fully get)
    min_heap= []
    
    # builds a list of iterators for each array in sorted_arrays.
    # iter: converts iterables to iterators.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    #print(sorted_arrays_iters)
    #puts first element from each iterator in min_heap.
    for i, it in enumerate(sorted_arrays_iters):
        #print(i, it)  #'it' is a list_iterator object. enumerate gives you the indices
        #heapq.heappush(min_heap, (it, i))
        first_element = next(it, None)
        #print(first_element)
        #print(first_element)  # first element is just the iterator it being enumerate
        if first_element is not None:
            #Difference between first_element and i? Why are we pushing both
            heapq.heappush(min_heap, (first_element, i))
            #print(min_heap) Heap is an object with its own print function. Therefore
            # does not print the desired result
        # above pushes elements to the minheap
    result = []
    while min_heap:
        # repeat the process until there is no more element in the heap :) 
        # this loop gets the smallest element? because it is minheap? Yes
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        #print(smallest_entry, smallest_array_i) # it is iterating through the heap
        # each time the smallest_array_i is printed, one at a time.
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        
        result.append(smallest_entry)
        #go to the next element that is the smallest
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            # this part less clear?
            # does the heapq automatically orders the heap or is that what we are doing?
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

#Pythonic solution, uses sthe heapq.merge() method which takes multiple inputs

#def merge_sorted_arrays_pythonic(sorted_arrays):
 #   return list(heapq.merge(sorted_arrays))



sorted_arrays = [[3,5,7], [0,6], [0,6,28]]
print(merge_sorted_arrays(sorted_arrays))