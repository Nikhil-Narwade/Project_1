

# problem 1: two sum 

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


print("two sum:", two_sum([2,7,11,15], 9))  # [0,1]



# problem 2: palindrome number 

def is_palindrome(x):
    if x < 0:
        return False
    # convert to string and check
    return str(x) == str(x)[::-1]

print("121 palindrome?", is_palindrome(121))    # true
print("-121 palindrome?", is_palindrome(-121))  # false



# problem 3: roman to integer 

def roman_to_int(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 
             'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    
    for c in s[::-1]:  # go backwards
        curr = roman[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

print("MCMXCIV =", roman_to_int("MCMXCIV"))  # 1994



# problem 4: valid parentheses 

def is_valid(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0

print("()[]{} valid?", is_valid("()[]{}"))    # true
print("([)] valid?", is_valid("([)]"))        # false



# problem 5: longest common prefix 

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

words = ["flower", "flow", "flight"]
print("common prefix:", longest_common_prefix(words))  # "fl"



# problem 6: remove duplicates from sorted array 
def remove_duplicates(nums):
    if not nums:
        return 0
    
    write_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[write_pos] = nums[i]
            write_pos += 1
    return write_pos

nums = [1,1,2,2,3,3,4]
k = remove_duplicates(nums)
print("unique count:", k)  # 4
print("array now:", nums[:k])  # [1,2,3,4]



# problem 7: plus one 

def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

print("plus one to [9,9,9]:", plus_one([9,9,9]))  # [1,0,0,0]



# problem 8: single number 
# find number that appears only once
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # xor magic!
    return result

print("single number in [4,1,2,1,2]:", 
      single_number([4,1,2,1,2]))  # 4
