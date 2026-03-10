# group anagrams 
def group_anagrams(strs):
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        # sort string to use as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("anagram groups:")
for group in group_anagrams(words):
    print(group)


# product of array except self (no division)
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # right products
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result

print("product except self [1,2,3,4]:", product_except_self([1,2,3,4]))


# spiral matrix 
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("spiral order:", spiral_order(matrix))


# rotate image (rotate matrix 90 degrees)
def rotate(matrix):
    n = len(matrix)
    
    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]
print("rotated matrix:")
for row in rotate(mat):
    print(row)
