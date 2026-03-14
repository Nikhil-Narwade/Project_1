#  decode ways (dp)
def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        one_digit = int(s[i-1:i])
        two_digit = int(s[i-2:i])
        
        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

print("decode ways for '226':", num_decodings("226"))


# unique paths with obstacles
def unique_paths_with_obstacles(obstacle_grid):
    if not obstacle_grid or obstacle_grid[0][0] == 1:
        return 0
    
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]

grid = [[0,0,0],[0,1,0],[0,0,0]]
print("unique paths with obstacle:", unique_paths_with_obstacles(grid))


# ump game (can reach last index)
def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True

print("can jump [2,3,1,1,4]?", can_jump([2,3,1,1,4]))
print("can jump [3,2,1,0,4]?", can_jump([3,2,1,0,4]))

# gas station (can complete circuit)
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    total = 0
    start = 0
    
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            start = i + 1
    
    return start

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print("start station:", can_complete_circuit(gas, cost))


# single number II (every number appears thrice except one)
def single_number_ii(nums):
    # bit manipulation magic
    ones = twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

print("single in [2,2,3,2]:", single_number_ii([2,2,3,2]))
