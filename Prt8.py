#island perimeter 
def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                
                # check neighbors (subtract if adjacent land)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    
    return perimeter

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print("island perimeter:", island_perimeter(grid))

# find the difference (find extra char)
def find_the_difference(s, t):
    # xor all chars
    result = 0
    for c in s + t:
        result ^= ord(c)
    return chr(result)

print("extra char in 'abcd' and 'abcde':", find_the_difference("abcd", "abcde"))

#  word pattern (does string follow pattern?)
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            if w in word_to_char:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
    
    return True

print("'abba' matches 'dog cat cat dog'?", 
      word_pattern("abba", "dog cat cat dog"))

# sum of left leaves
def sum_of_left_leaves(root):
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return dfs(node.left, True) + dfs(node.right, False)
    
    return dfs(root, False)

# making a tree
leaf_tree = TreeNode(3)
leaf_tree.left = TreeNode(9)
leaf_tree.right = TreeNode(20)
leaf_tree.right.left = TreeNode(15)
leaf_tree.right.right = TreeNode(7)

print("sum of left leaves:", sum_of_left_leaves(leaf_tree))

#  reverse string (recursion)
def reverse_string_rec(s):
    if len(s) <= 1:
        return s
    return reverse_string_rec(s[1:]) + s[0]

print("reverse 'hello' recursively:", reverse_string_rec("hello"))

# third maximum number
def third_max(nums):
    nums = list(set(nums))  # remove duplicates
    if len(nums) < 3:
        return max(nums)
    
    nums.sort(reverse=True)
    return nums[2]

print("third max in [3,2,1]:", third_max([3,2,1]))
print("third max in [1,2]:", third_max([1,2]))


# find all numbers disappeared in array
def find_disappeared_numbers(nums):
    
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1
    
    # collect indices that are still positive
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    
    return result

nums = [4,3,2,7,8,2,3,1]
print("disappeared numbers:", find_disappeared_numbers(nums)

  # maximum product of three numbers
def maximum_product(nums):
    nums.sort()
    # either product of three largest or two smallest and largest
    return max(nums[-1] * nums[-2] * nums[-3], 
               nums[0] * nums[1] * nums[-1])

print("max product of three in [1,2,3,4]:", maximum_product([1,2,3,4]))
