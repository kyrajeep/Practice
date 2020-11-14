import bisect
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
    return i
    #raise ValueError

print(index([1,2,3,5], 4))