# contains duplicate
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

print("has duplicate [1,2,3,1]?", contains_duplicate([1,2,3,1]))


# happy number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

print("is 19 happy?", is_happy(19))
print("is 2 happy?", is_happy(2))

# power of two
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n-1)) == 0

print("16 power of two?", is_power_of_two(16))
print("18 power of two?", is_power_of_two(18))


# reverse vowels
def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s)-1
    
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

print("reverse vowels of 'hello':", reverse_vowels("hello"))


# guess number higher or lower (binary search again)
def guessNumber(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if guess(mid) == 0:  # guess() is a pre-defined API
            return mid
        elif guess(mid) == -1:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# climbing stairs (how many ways?)
def climb_stairs(n):
    if n <= 2:
        return n
    one, two = 1, 2
    for i in range(3, n+1):
        three = one + two
        one, two = two, three
    return two

print("ways to climb 5 stairs:", climb_stairs(5))


# best time to buy and sell stock
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print("max profit [7,1,5,3,6,4]:", max_profit([7,1,5,3,6,4]))


# linked list cycle detection (slow and fast pointers)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# making a test cycle
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # create cycle
print("has cycle?", hasCycle(head))


# merge two sorted lists
def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 or list2
    return dummy.next

# test merge
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

merged = mergeTwoLists(l1, l2)

# helper to print list
def printList(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print("->".join(vals))

print("merged list:")
printList(merged)
