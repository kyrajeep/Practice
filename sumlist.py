#input: list
#output: sum of each element of the list

def sumlist(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return (list1[0] + sumlist(list1[1:]))

print(sumlist([1,2,3,9]))
print(sumlist([1]))
#print(sumlist())
