
list2 = [[2,3,5,6], [3,4,7,8], [1,2,3,4], [76, 78,77,65]]
list2.reverse()

def reverse(list):
   # temp = [[0 for col in range(len(list))] 
#for row in range(len(list))]
    
    for i in range(len(list)):
        j = 0
        while (i +j) < 4:
            
            list[i][i+j] = list[i+j][i]    
            j = j+1
    print(list)
    


reverse(list2)
        
