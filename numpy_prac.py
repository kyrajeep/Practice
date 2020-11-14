#practice for Intro ML - Gradient Descent : Feb 25th 2020
import numpy as np
y = np.zeros((2, 3, 4))
#print(y)
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[2,3,4], [9,7,8]])
#print(np.hstack((a,b)))

c = np.array([[2,3,4], [5,6,7]])
d = np.array([[3,4,5], [4,5,3]])
#print(np.hstack((c,d)))

#print([i for i in range(4)])
random_n = np.random.choice(range(2),3)
#print(c)
#print(random_n)
# the indexing: the second part is columnwise
#print(c[random_n,:-1]) # stops right before the last entry.   
a = np.ones([9, 3, 2, 4])
c = np.ones([9, 5, 4, 3])   # how to dot product and matmul. 
print(a)
print(c)
print(np.dot(a, c).shape)

#print(np.matmul(a, c).shape)



x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))
#print(xx)
#print(x)
#print(y)
#print(xx + y) # hmm I don't understand by what principle it does this.
#print(z)