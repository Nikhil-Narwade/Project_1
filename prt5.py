# valid anagram (check if two strings are anagrams)
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print("'anagram' and 'nagaram' anagrams?", is_anagram("anagram", "nagaram"))



# palindrome number 
def is_palindrome_number(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    return x == reversed_num or x == reversed_num // 10

print("121 palindrome?", is_palindrome_number(121))
print("10 palindrome?", is_palindrome_number(10))


# longest common prefix
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
print("common prefix:", longest_common_prefix(words))



# remove element from array
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3,2,2,3]
k = remove_element(nums, 3)
print("after removing 3:", nums[:k])


# implement strStr() (find first occurrence)
def str_str(haystack, needle):
    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print("find 'll' in 'hello':", str_str("hello", "ll"))


# search insert position (binary search)
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print("insert position for 5 in [1,3,5,6]:", search_insert([1,3,5,6], 5))
print("insert position for 2 in [1,3,5,6]:", search_insert([1,3,5,6], 2))


# length of last word
def length_of_last_word(s):
    words = s.split()
    return len(words[-1]) if words else 0

print("last word length in 'hello world':", length_of_last_word("hello world"))



# plus one (another approach)
def plus_one_another(digits):
    num = 0
    for d in digits:
        num = num * 10 + d
    num += 1
    return [int(x) for x in str(num)]

print("plus one to [1,2,3]:", plus_one_another([1,2,3]))
