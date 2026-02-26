# 🤔 Q1: How do I take input and print it?
name = "Nikhil"  # normally: input("Enter your name: ")
print("Hello", name)


# 🤔 Q2: How to check even or odd?
num = 7
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# 🤔 Q3: How to find the largest of 3 numbers?
a, b, c = 10, 25, 15

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest number is:", largest)


# 🤔 Q4: How to print a multiplication table?
n = 5
print(f"Table of {n}")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 🤔 Q5: How to find factorial?
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)


# 🤔 Q6: How to check prime number?
n = 17
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print(n, "is prime?" , is_prime)


# 🤔 Q7: How to reverse a string?
text = "python"
reversed_text = text[::-1]
print("Reversed:", reversed_text)


# 🤔 Q8: How to count vowels in a string?
text = "hello world"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)


# 🤔 Q9: How to find sum of list?
nums = [10, 20, 30, 40]
total = 0

for n in nums:
    total += n

print("Sum of list:", total)


# 🤔 Q10: How to find max in list?
nums = [3, 7, 2, 9, 5]
max_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n

print("Max value:", max_val)


# 🤔 Q11: How to do Two Sum? (LeetCode style)
nums = [2, 7, 11, 15]
target = 9

seen = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in seen:
        print("Two sum indices:", seen[diff], i)
        break
    seen[nums[i]] = i


# 🤔 Q12: How to count set bits in a number?
n = 13  # binary 1101 → 3 ones
count = bin(n).count("1")
print("Set bits:", count)


# 🤔 Q13: How to sort numbers by set bits?
arr = [0,1,2,3,4,5,6,7,8]
sorted_arr = sorted(arr, key=lambda x: (bin(x).count("1"), x))
print("Sorted by bits:", sorted_arr)


# 🤔 Q14: Simple class example?
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name, "| Marks:", self.marks)

s1 = Student("Nikhil", 90)
s1.show()


# 🤔 Q15: How to handle errors?
try:
    x = int("abc")
except ValueError:
    print("Cannot convert to integer")


print("✅ Practice file finished")
