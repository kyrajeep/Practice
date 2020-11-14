def update_digit(inarray):
    inarray[-1] += 1
    for i in reversed(range(1, len(inarray))):
        #print(2)
        if inarray[i] == 10:
            inarray[i] = 0
            inarray[i-1] += 1
            i -= 1
        else:
            inarray[-1] += 1
    if inarray[0] == 10:
        inarray[0] = 1
        inarray.append(0)
    return inarray


B = [9,9,9]
update_digit(B)
print(B)