# toeplitz matrix 
def is_toeplitz(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

mat = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print("is toeplitz?", is_toeplitz(mat))


# flip image 
def flip_and_invert_image(image):
    for row in image:
        # reverse and invert in one go
        for i in range((len(row) + 1) // 2):
            # swap and flip bits
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return image

img = [[1,1,0],[1,0,1],[0,0,0]]
print("flipped and inverted:", flip_and_invert_image(img))


# transpose matrix
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

mat = [[1,2,3],[4,5,6]]
print("transpose:")
for row in transpose(mat):
    print(row)


# fair candy swap
def fair_candy_swap(alice_sizes, bob_sizes):
    sum_a, sum_b = sum(alice_sizes), sum(bob_sizes)
    diff = (sum_a - sum_b) // 2
    set_b = set(bob_sizes)
    
    for x in alice_sizes:
        y = x - diff
        if y in set_b:
            return [x, y]
    return []

alice = [1,1]
bob = [2,2]
print("candy swap:", fair_candy_swap(alice, bob))


# monotonic array 
def is_monotonic(nums):
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            decreasing = False
        if nums[i] < nums[i-1]:
            increasing = False
    
    return increasing or decreasing

print("[1,2,2,3] monotonic?", is_monotonic([1,2,2,3]))
print("[1,3,2] monotonic?", is_monotonic([1,3,2]))


# sort array by parity 
def sort_by_parity(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
        
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    
    return nums

print("sort by parity [3,1,2,4]:", sort_by_parity([3,1,2,4]))


# peak index in mountain array
def peak_index(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

mountain = [0,1,2,3,4,5,3,2,1,0]
print("peak at index:", peak_index(mountain))
