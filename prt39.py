# power of four
def is_power_of_four(n):
    # power of two and 1 at odd position
    return n > 0 and (n & (n-1)) == 0 and (n & 0x55555555) != 0

print("16 power of four?", is_power_of_four(16))
print("8 power of four?", is_power_of_four(8))


# m6find the duplicate number
def find_duplicate(nums):
    # floyd's cycle detection
    slow = fast = nums[0]
    
    # find meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # find cycle start
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

nums = [1,3,4,2,2]
print("duplicate number:", find_duplicate(nums))


# maximum product of word lengths
def max_product_word_lengths(words):
    # use bitmask for each word
    masks = []
    for word in words:
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        masks.append(mask)
    
    max_len = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if masks[i] & masks[j] == 0:
                max_len = max(max_len, len(words[i]) * len(words[j]))
    
    return max_len

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print("max product of word lengths:", max_product_word_lengths(words))
