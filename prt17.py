#1 Two Sum (using hashmap)
def two_sum(nums, target):
    lookup = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
    
    return []

print("Two sum indices:", two_sum([2, 7, 11, 15], 9))

#2 Valid Parentheses
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

print("Is '()[]{}' valid?:", is_valid("()[]{}") )

#3 Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    return dummy.next

#4 Container With Most Water
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        h = min(height[left], height[right])
        width = right - left
        max_water = max(max_water, h * width)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

print("Max water:", max_area([1,8,6,2,5,4,8,3,7]))

#5 Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

print("Longest unique substring in 'abcabcbb':", 
      longest_unique_substring("abcabcbb"))
