# input: list
# output: sum of that list

# the base case is the terminating condition.
# if you can express the function with the function itself, you can use recursion.

def sum_list(l):
    if len(l) == 1:
        return len[0]
    else:
        return len[0] + sum_list(l[1:])



