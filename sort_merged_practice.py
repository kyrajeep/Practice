import heapq
# I need to do a few of these implementations to really understand the function. 
# Kind of not getting why it is so useful. I suppose log(n) is good and also O(1) 
# to locate the smallest/ largest element is very very good. 
# O(1) time to locate the smallest element is great!
def sort_merged(sorted_arrays):
    # wait I don't remember a thing. Heapify? no, I think they come as arrays
    min_heap = []
    sorted_iter = [iter(x) for x in sorted_arrays]
    print(sorted_iter) #want to figure out how the iterators work?
    for i, it in enumerate(sorted_iter):
     #   print(i, it)
        # put enumerate to put automatic counter.
        # without the 'next' it errors because the library cannot compare with 
        # the <list-iterator object>. It needs to be iterated.
        first_iter = next(it, None)
        print(first_iter)
        if first_iter:       
            heapq.heappush(min_heap, (i, first_iter))
            print(min_heap)
    result = []
    #while min_heap:
        
     #   return None

sort_merged([[1,2,3], [3,4,5]])