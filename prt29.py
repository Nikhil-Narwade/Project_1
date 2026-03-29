# maximum product subarray
def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        candidates = (max_prod * num, min_prod * num, num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)
    
    return result

print("max product subarray [2,3,-2,4]:", max_product_subarray([2,3,-2,4]))

# word break
def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

s = "leetcode"
word_dict = ["leet","code"]
print("can break 'leetcode'?", word_break(s, word_dict))

#  longest increasing path in matrix
def longest_increasing_path(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def dfs(i, j):
        if memo[i][j] != 0:
            return memo[i][j]
        
        max_len = 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                max_len = max(max_len, 1 + dfs(x, y))
        
        memo[i][j] = max_len
        return max_len
    
    result = 0
    for i in range(rows):
        for j in range(cols):
            result = max(result, dfs(i, j))
    
    return result

mat = [[9,9,4],[6,6,8],[2,1,1]]
print("longest increasing path:", longest_increasing_path(mat))


# longest consecutive sequence
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest

nums = [100,4,200,1,3,2]
print("longest consecutive sequence:", longest_consecutive(nums))
