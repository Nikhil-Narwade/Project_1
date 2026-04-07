# sum of two integers
def get_sum_bit(a, b):
    # no + or - allowed
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print("1 + 2 =", get_sum_bit(1, 2))
print("5 + 7 =", get_sum_bit(5, 7))


# missing number
def missing_number_xor(nums):
    n = len(nums)
    xor_all = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all

nums = [3,0,1]
print("missing number:", missing_number_xor(nums))


# reverse bits
def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

n = 43261596  # 00000010100101000001111010011100
print("reversed bits:", reverse_bits(n))


# counting bits
def count_bits(n):
    dp = [0] * (n + 1)
    offset = 1
    
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    
    return dp

print("bits count for 0-5:", count_bits(5))
