# merge k sorted lists
import heapq

def merge_k_lists(lists):
    heap = []
    
    # push first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# test with sample lists
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]
merged = merge_k_lists(lists)
print("merged k lists:")
printList(merged)


# sliding window maximum
def max_sliding_window(nums, k):
    from collections import deque
    
    result = []
    dq = deque()  # store indices
    
    for i, num in enumerate(nums):
        # remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # add to result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

nums = [1,3,-1,-3,5,3,6,7]
print("sliding window max k=3:", max_sliding_window(nums, 3))


# minimum window substring
def min_window(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_counts = {}
    
    left = right = 0
    ans = float('inf'), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

s = "ADOBECODEBANC"
t = "ABC"
print("minimum window:", min_window(s, t))
