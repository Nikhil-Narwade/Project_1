# total hamming distance
def total_hamming_distance(nums):
    total = 0
    n = len(nums)
    
    for bit in range(32):
        count_ones = 0
        for num in nums:
            if num & (1 << bit):
                count_ones += 1
        total += count_ones * (n - count_ones)
    
    return total

nums = [4,14,2]
print("total hamming distance:", total_hamming_distance(nums))


# find the celebrity
def find_celebrity_bit(n, knows_func):
    # same as before but using bitmask for optimization
    candidates = (1 << n) - 1
    
    for i in range(n):
        if not (candidates >> i) & 1:
            continue
        
        for j in range(n):
            if i != j:
                if knows_func(i, j):
                    candidates &= ~(1 << i)
                    break
                else:
                    candidates &= ~(1 << j)
    
    if candidates == 0:
        return -1
    
    celebrity = (candidates.bit_length() - 1)
    
    # verify
    for i in range(n):
        if i != celebrity:
            if knows_func(celebrity, i) or not knows_func(i, celebrity):
                return -1
    
    return celebrity

# using same knows function from before
print("celebrity bit method:", find_celebrity_bit(3, knows))


# maximum xor of two numbers in array
def find_maximum_xor(nums):
    max_xor = 0
    mask = 0
    
    for bit in range(31, -1, -1):
        mask |= (1 << bit)
        prefixes = set()
        
        for num in nums:
            prefixes.add(num & mask)
        
        candidate = max_xor | (1 << bit)
        
        for prefix in prefixes:
            if candidate ^ prefix in prefixes:
                max_xor = candidate
                break
    
    return max_xor

nums = [3,10,5,25,2,8]
print("max xor:", find_maximum_xor(nums))
