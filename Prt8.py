# distribute candies (max different types)
def distribute_candies(candy_type):
    return min(len(set(candy_type)), len(candy_type) // 2)

print("max different candies:", distribute_candies([1,1,2,2,3,3]))

# shortest word distance
def shortest_distance(words_dict, word1, word2):
    pos1, pos2 = -1, -1
    min_dist = float('inf')
    
    for i, word in enumerate(words_dict):
        if word == word1:
            pos1 = i
        if word == word2:
            pos2 = i
        
        if pos1 != -1 and pos2 != -1:
            min_dist = min(min_dist, abs(pos1 - pos2))
    
    return min_dist

words = ["practice", "makes", "perfect", "coding", "makes"]
print("distance between 'coding' and 'practice':", 
      shortest_distance(words, "coding", "practice"))

# island perimeter (another approach)
def island_perimeter_bfs(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        
        visited.add((i, j))
        perimeter = 0
        perimeter += dfs(i+1, j)
        perimeter += dfs(i-1, j)
        perimeter += dfs(i, j+1)
        perimeter += dfs(i, j-1)
        
        return perimeter
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return dfs(i, j)
    return 0

print("perimeter bfs style:", island_perimeter_bfs(grid))

#  license key formatting
def license_key_format(s, k):
    
    s = s.replace("-", "").upper()
  
    result = []
    for i in range(len(s), 0, -k):
        start = max(0, i - k)
        result.append(s[start:i])
    
    return "-".join(result[::-1])

print("format '5F3Z-2e-9-w' with k=4:", 
      license_key_format("5F3Z-2e-9-w", 4))

#  number complement
def find_complement(num):
    
    bit_length = num.bit_length()
  
    mask = (1 << bit_length) - 1

    return num ^ mask

print("complement of 5 (101 -> 010):", find_complement(5))

# keyboard row (words that can be typed using one row)
def find_words(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    
    result = []
    for word in words:
        w = set(word.lower())
        if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
            result.append(word)
    
    return result

test_words = ["Hello", "Alaska", "Dad", "Peace"]
print("one row words:", find_words(test_words))

# next greater element I
def next_greater_element(nums1, nums2):
    
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    for num in stack:
        next_greater[num] = -1
    
    return [next_greater[num] for num in nums1]

print("next greater for [4,1,2] in [1,3,4,2]:", 
      next_greater_element([4,1,2], [1,3,4,2]))

