def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print("two sum:", two_sum([2,7,11,15], 9))



def reverse_string(s):
    return s[::-1]

print("reverse of 'hello':", reverse_string("hello"))



def is_palindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

print("121 palindrome?", is_palindrome(121))
print("-121 palindrome?", is_palindrome(-121))



def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("fibonacci 6:", fib(6))



def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print("fizzbuzz up to 15:")
print(fizz_buzz(15))



def max_product(nums):
    nums.sort()
    return nums[-1] * nums[-2]

print("max product of [1,5,3,9,2]:", max_product([1,5,3,9,2]))



def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print("vowels in 'hello world':", count_vowels("hello world"))



def remove_duplicates(nums):
    return list(set(nums))

print("remove dupes from [1,2,2,3,4,4,5]:", 
      remove_duplicates([1,2,2,3,4,4,5]))


def find_max(nums):
    if not nums:
        return None
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print("largest in [4,2,9,7,5]:", find_max([4,2,9,7,5]))



def is_digit_string(s):
    for char in s:
        if not char.isdigit():
            return False
    return True

print("'12345' all digits?", is_digit_string("12345"))
print("'12a45' all digits?", is_digit_string("12a45"))



def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

print("sum of [1,2,3,4,5]:", sum_list([1,2,3,4,5]))



def count_occurrences(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

print("how many 2's in [1,2,3,2,4,2]:", 
      count_occurrences([1,2,3,2,4,2], 2))



def is_even(n):
    return n % 2 == 0

print("10 is even?", is_even(10))
print("7 is even?", is_even(7))



def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

print("average of [10,20,30,40]:", average([10,20,30,40]))



def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

print("reverse 'hello world python':", 
      reverse_words("hello world python"))



def find_min(nums):
    if not nums:
        return None
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

print("smallest in [8,3,1,9,4]:", find_min([8,3,1,9,4]))



def is_palindrome_string(s):
    s = s.lower()
    return s == s[::-1]

print("'racecar' palindrome?", is_palindrome_string("racecar"))
print("'hello' palindrome?", is_palindrome_string("hello"))



def count_words(sentence):
    return len(sentence.split())

print("words in 'python is fun to learn':", 
      count_words("python is fun to learn"))



def multiply_list(nums):
    result = 1
    for num in nums:
        result *= num
    return result

print("product of [2,3,4]:", multiply_list([2,3,4]))

