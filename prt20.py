valid palindrome


def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print("palindrome?", is_palindrome("A man, a plan, a canal: Panama"))

move zeroes

def move_zeroes(nums):
    i = 0
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0
    return nums

print("move zeroes:", move_zeroes([0,1,0,3,12]))

majority element

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

print("majority:", majority_element([2,2,1,1,1,2,2]))

missing number

def missing_number(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)

print("missing:", missing_number([3,0,1]))

single number

def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

print("single:", single_number([4,1,2,1,2]))

intersection of two arrays

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print("intersection:", intersection([1,2,2,1],[2,2]))
