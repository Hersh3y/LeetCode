def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = b + temp
    return b


print(climbStairs(2)) # Output: 2
print(climbStairs(3)) # Output: 3
print(climbStairs(4)) # Output: 5
print(climbStairs(5)) # Output: 8
print(climbStairs(6)) # Output: 13
print(climbStairs(7)) # Output: 21