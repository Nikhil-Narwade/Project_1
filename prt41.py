# ugly number (only prime factors 2,3,5)
def is_ugly(n):
    if n <= 0:
        return False
    
    for factor in [2,3,5]:
        while n % factor == 0:
            n //= factor
    
    return n == 1

print("6 ugly?", is_ugly(6))
print("14 ugly?", is_ugly(14))


# ugly number II (nth ugly number)
def nth_ugly_number(n):
    ugly = [1] * n
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5
    
    for i in range(1, n):
        ugly[i] = min(next2, next3, next5)
        
        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5] * 5
    
    return ugly[n-1]

print("10th ugly number:", nth_ugly_number(10))


# super ugly number (multiple primes)
def nth_super_ugly_number(n, primes):
    ugly = [1] * n
    indices = [0] * len(primes)
    values = [p for p in primes]
    
    for i in range(1, n):
        ugly[i] = min(values)
        
        for j in range(len(primes)):
            if values[j] == ugly[i]:
                indices[j] += 1
                values[j] = ugly[indices[j]] * primes[j]
    
    return ugly[n-1]

primes = [2,7,13,19]
print("12th super ugly number:", nth_super_ugly_number(12, primes))


# add digits (digital root)
def add_digits(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9

print("digital root of 38:", add_digits(38))
