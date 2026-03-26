# fibonacci with memoization 
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print("fibonacci 30:", fib_memo(30))

# tribonacci sequence
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
    
    return c

print("tribonacci 10:", tribonacci(10))


# min cost climbing stairs 
def min_cost_stairs(cost):
    prev2, prev1 = cost[0], cost[1]
    
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr
    
    return min(prev2, prev1)

stairs_cost = [10,15,20]
print("min cost stairs:", min_cost_stairs(stairs_cost))


# perfect squares (least number of squares sum to n)
def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    
    return dp[n]

print("least squares for 12:", num_squares(12))


# integer break (break into sum of ints for max product)
def integer_break(n):
    if n <= 3:
        return n - 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    
    return dp[n]

print("max product breaking 10:", integer_break(10))
