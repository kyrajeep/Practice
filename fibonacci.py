def fibonacci(n, fib_list):
    if n < 0:
        print("Invalid input")
      
    if n <= len(fib_list):
        return fib_list[n-1]
    else:
        fib_list.append(fibonacci(n-2, fib_list))
        fib_list.append(fibonacci(n-1, fib_list))
        return fib_list[n-2] + fib_list[n-1]


print(fibonacci(9, [0, 1]))