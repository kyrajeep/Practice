def dutch_flag(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break #why do you 'break'?


A = [1, 7,2, 8]
dutch_flag(len(A)-1,A)
print(A)