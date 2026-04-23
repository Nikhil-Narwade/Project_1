# regular expression matching
def is_match_regex(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # handle patterns like a*, a*b*, etc
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # zero occurrences
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # one or more
            elif p[j-1] == '.' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]

s = "aa"
p = "a*"
print(f"'{s}' matches regex '{p}'?", is_match_regex(s, p))


# longest increasing path in matrix
def longest_increasing_path_matrix(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
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

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print("longest increasing path:", longest_increasing_path_matrix(matrix))
