# missing number in array 
def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

print("missing number in [3,0,1]:", missing_number([3,0,1]))



# valid parentheses 
def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

print("'()[]{}' valid?", is_valid("()[]{}"))
print("'([)]' valid?", is_valid("([)]"))



# single number 
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # xor magic!
    return result

print("single in [4,1,2,1,2]:", single_number([4,1,2,1,2]))



# plus one to array of digits
def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

print("plus one to [9,9,9]:", plus_one([9,9,9]))



# move zeroes to end
def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

print("move zeroes [0,1,0,3,12]:", move_zeroes([0,1,0,3,12]))



# intersection of two arrays
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

print("intersection of [1,2,2,1] and [2,2]:", 
      intersection([1,2,2,1], [2,2]))



# ransom note (can you make it from magazine?)
def can_construct(ransom_note, magazine):
    for char in set(ransom_note):
        if ransom_note.count(char) > magazine.count(char):
            return False
    return True

print("make 'aa' from 'aab'?", can_construct("aa", "aab"))
print("make 'aa' from 'ab'?", can_construct("aa", "ab"))



# binary search (gotta learn this!)
def search(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
print("find 9:", search(nums, 9))
print("find 2:", search(nums, 2))



# first unique character in string
def first_uniq_char(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

print("first unique in 'loveleetcode':", first_uniq_char("loveleetcode"))



# majority element (appears more than n/2 times)
def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

print("majority in [2,2,1,1,1,2,2]:", majority_element([2,2,1,1,1,2,2]))

