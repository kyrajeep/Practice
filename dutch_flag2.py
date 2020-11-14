def dutch_flag2(pivot_index, inputarray):
    pivot = inputarray[pivot_index]
    smaller = 0
    
    for i in range(len(inputarray)):
        if inputarray[i] < pivot:
            inputarray[i], inputarray[smaller] = inputarray[smaller], inputarray[i]
            smaller += 1
    larger = len(inputarray) - 1
    for i in reversed(range(len(inputarray))):
        if inputarray[i] > pivot:
            inputarray[i], inputarray[larger] = inputarray[larger], inputarray[i]
            larger -= 1



B = [12, 3, 1,9]

dutch_flag2(0, B)
print(B)