def fib_iter(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0,1
    for _ in range(1,n):
        #print(_)
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


print(fib_iter(9))
