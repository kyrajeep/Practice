def dutch_flag(A, index):
    smaller = 0
    larger = len(A) -1
    pivot = A[index]
    for i in range(len(A)):
        if pivot > A[i]:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Should we run two passes? Is there a way to do it in one?
    # this is a more obvious solution though.
    # should there be some constraint on 'smaller'
    for j in reversed(range(len(A))):
        if pivot < A[j]:
            A[j], A[larger] = A[larger], A[j]
            larger -= 1
    return A

A = [1,3,2]
print(dutch_flag(A,2))