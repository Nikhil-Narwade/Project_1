# reverse integer
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    reversed_num *= sign
    
    # check 32-bit overflow
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

print("reverse 123:", reverse_integer(123))
print("reverse -123:", reverse_integer(-123))
print("reverse 1534236469 (overflow):", reverse_integer(1534236469))


# happy number (cycle detection with slow/fast)
def is_happy_fast(n):
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1

print("19 happy?", is_happy_fast(19))


# excel sheet column title (number to letters)
def convert_to_title(column_number):
    result = []
    
    while column_number > 0:
        column_number -= 1
        result.append(chr(ord('A') + column_number % 26))
        column_number //= 26
    
    return ''.join(result[::-1])

print("1 ->", convert_to_title(1))
print("28 ->", convert_to_title(28))
print("701 ->", convert_to_title(701))


# factorial trailing zeroes
def trailing_zeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

print("trailing zeroes in 10!:", trailing_zeroes(10))
print("trailing zeroes in 100!:", trailing_zeroes(100))
