# search in rotated sorted array
def search_rotated(nums, target):
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

rotated = [4,5,6,7,0,1,2]
print("find 0 in rotated array:", search_rotated(rotated, 0))


# find first and last position in sorted array
def search_range(nums, target):
    def find_left():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def find_right():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    left_idx = find_left()
    right_idx = find_right()
    
    if left_idx <= right_idx and left_idx < len(nums) and nums[left_idx] == target:
        return [left_idx, right_idx]
    return [-1, -1]

arr = [5,7,7,8,8,10]
print("range of 8:", search_range(arr, 8))

# sqrt with precision (binary search)
def sqrt_precision(x, precision=0.0001):
    if x < 0:
        return None
    if x == 0 or x == 1:
        return x
    
    left, right = 0, x
    while right - left > precision:
        mid = (left + right) / 2
        if mid * mid < x:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2

print("sqrt of 2 with precision:", sqrt_precision(2))


# pow(x, n) (exponentiation)
def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    
    if n % 2 == 0:
        return my_pow(x * x, n // 2)
    else:
        return x * my_pow(x * x, n // 2)

print("2^10 =", my_pow(2, 10))
print("2^-2 =", my_pow(2, -2))
