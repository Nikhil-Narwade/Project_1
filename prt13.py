# generate parentheses (backtracking)
def generate_parenthesis(n):
    result = []
    
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    backtrack('', 0, 0)
    return result

print("parentheses for n=3:", generate_parenthesis(3))


# letter combinations of phone number
def letter_combinations(digits):
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(combination, next_digits):
        if not next_digits:
            result.append(combination)
            return
        
        for letter in phone[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])
    
    backtrack('', digits)
    return result

print("letter combos for '23':", letter_combinations('23'))


# combination sum (find combos that sum to target)
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result

print("combinations sum to 7 from [2,3,6,7]:", 
      combination_sum([2,3,6,7], 7))


# subsets (all possible subsets)
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

print("subsets of [1,2,3]:", subsets([1,2,3]))


# permutations of array
def permute(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result

print("permutations of [1,2,3]:", permute([1,2,3]))


# word search (find word in grid)
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(i, j, k):
        if k == len(word):
            return True
        
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            board[i][j] != word[k]):
            return False
        
        # mark as visited
        temp = board[i][j]
        board[i][j] = '#'
        
        # check neighbors
        found = (dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or 
                 dfs(i, j+1, k+1) or dfs(i, j-1, k+1))
        
        # unmark
        board[i][j] = temp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    
    return False

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print("find 'ABCCED' in board?", exist(board, "ABCCED"))

