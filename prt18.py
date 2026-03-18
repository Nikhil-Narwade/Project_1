# find all duplicates in array
def find_duplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

print("duplicates in [4,3,2,7,8,2,3,1]:", find_duplicates([4,3,2,7,8,2,3,1]))


# valid perfect square (without sqrt)
def is_perfect_square(num):
    if num < 1:
        return False
    if num == 1:
        return True
    
    left, right = 1, num // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

print("16 perfect square?", is_perfect_square(16))
print("14 perfect square?", is_perfect_square(14))


# reverse only letters (keep special chars in place)
def reverse_only_letters(s):
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return ''.join(s)

print("reverse only letters in 'a-bC-dEf-ghIj':", 
      reverse_only_letters("a-bC-dEf-ghIj"))


# find the difference 
def find_difference(s, t):
    # using ord() and chr()
    diff = 0
    for c in s:
        diff ^= ord(c)
    for c in t:
        diff ^= ord(c)
    return chr(diff)

print("extra char in 'abcd' and 'abcde':", find_difference("abcd", "abcde"))

#  add strings (without converting to int)
def add_strings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        
        total = n1 + n2 + carry
        result.append(str(total % 10))
        carry = total // 10
        
        i -= 1
        j -= 1
    
    return ''.join(result[::-1])

print("123 + 456 =", add_strings("123", "456"))
