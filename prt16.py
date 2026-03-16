# multiply strings (without converting to int)
def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    
    result = [0] * (len(num1) + len(num2))
    
    # reverse iteration
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            pos1, pos2 = i + j, i + j + 1
            total = mul + result[pos2]
            
            result[pos1] += total // 10
            result[pos2] = total % 10
    
    # remove leading zeros
    result_str = ''.join(map(str, result))
    return result_str.lstrip('0')

print("123 * 456 =", multiply_strings("123", "456"))

# longest palindromic substring 
def longest_palindrome(s):
    if not s or len(s) < 2:
        return s
    
    start, max_len = 0, 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        # odd length
        l1, r1 = expand_around_center(i, i)
        if r1 - l1 + 1 > max_len:
            start, max_len = l1, r1 - l1 + 1
        
        # even length
        l2, r2 = expand_around_center(i, i+1)
        if r2 - l2 + 1 > max_len:
            start, max_len = l2, r2 - l2 + 1
    
    return s[start:start + max_len]

print("longest palindrome in 'babad':", longest_palindrome("babad"))


# zigzag conversion
def convert(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [''] * num_rows
    curr_row = 0
    going_down = False
    
    for c in s:
        rows[curr_row] += c
        if curr_row == 0 or curr_row == num_rows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
    
    return ''.join(rows)

print("zigzag of 'PAYPALISHIRING' with 3 rows:", 
      convert("PAYPALISHIRING", 3))


# string to integer 
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    idx = 0
    
    if s[0] in '+-':
        sign = -1 if s[0] == '-' else 1
        idx += 1
    
    result = 0
    while idx < len(s) and s[idx].isdigit():
        result = result * 10 + int(s[idx])
        idx += 1
        
        # check overflow
        if result > 2**31 - 1:
            return 2**31 - 1 if sign == 1 else -2**31
    
    return sign * result

print("'   -42' to int:", my_atoi("   -42"))
print("'4193 with words' to int:", my_atoi("4193 with words"))
