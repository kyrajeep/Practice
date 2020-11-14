def rotate_array(l, k):
    length = len(l)
    array = []
    for j in range(length): 
        array.append(0)
    for i in range(len(l)):
        index = (i + k) % length 
        #temp = l[index]
        #l[index] = l[i]
        array[index] = l[i]
        #l[index + k % length] = temp
    return array 

print(rotate_array([1,2,3,4,5,6,7], 3))
print(rotate_array([1,2,3],1))
print(rotate_array([3,1,2,5],2))


def rotate_array(l, k):
    length = len(l)
 
    j = 1
    i = 0
    while j <= length: 
        index = k * j % length
        temp = l[index]
        l[index] = l[i]
       
        j += 1
        
        
    return array 

