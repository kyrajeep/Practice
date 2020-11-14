def fib(n,l):
# base case
    if n == 0:
        return(0,l)
    if n == 1:
        return(1,l)
     
    
    if n-1 in l.keys():
#getting n1 from the dictionary l
#with key n-1
        n1 = l[n-1]
    else:
#updating the hash table so that we don't have to repeat for n2
        n1,l1 = fib(n-1,l)
#inserting into the dictionary. This step makes it so that l is updated for 
# using for n2.
        l1[n-1] = n1        

    if n-2 in l.keys(): 
        n2 = l[n-2]
    else: # if it is a new key
        n2,l2 = fib(n-2,l1)   #updated l from previous, that's what l1 is for
        #additional variables than my code
        l2[n-2] = n2 #update dict
    return(n1+n2,l)

fn, fa = fib(9,{0:0,1:1})
print(fn)
print(fa)
#True/False,, numbers, constants
#here it works because n is a number passed in
    
# error raising. if n is a number. if it is not: raise an error (you need to input a number)


