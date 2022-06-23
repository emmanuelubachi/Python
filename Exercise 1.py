# =============================================================================
# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
# =============================================================================

def is_multiple(n, m):
    if m == 0: return(False)
    if n%m == 0:
        return True
    else:
        return False
    
multiple = is_multiple(14, 2)
multiple

# -----------------------------------------------------------------------Better

def is_multiple(n,m):
    if m == 0: return (False)
    return (n%m == 0)

multiple = is_multiple(14, 2)
multiple

# =============================================================================
# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
# =============================================================================

def is_even(k):
    for i in range(0, k+1, 2):
        if k in range(0, k+1, 2):
            return True
        else:
            return False
        
even = is_even(101)
even

# -----------------------------------------------------------------------Better

def is_even(k:int):
    assert type(k) == int, 'Your input must be an int'
    return (k&1 == 0)

even = is_even(5)
even

4 & 1 ==0
4 and 1 ==0

# =============================================================================
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.
# =============================================================================

def minmax(data):
    min_ = max_ = data[0] 
    for i in data:
        if i < min_: min_ = i
        elif i > max_: max_ = i          
    return min_, max_

num = [2,4,6,9]
mx = minmax(num)
mx

# =============================================================================
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
# =============================================================================





















