# count number of teams (3 soldiers increasing/decreasing)
def num_teams(rating):
    n = len(rating)
    count = 0
    
    for j in range(n):
        left_small = left_large = 0
        right_small = right_large = 0
        
        for i in range(j):
            if rating[i] < rating[j]:
                left_small += 1
            elif rating[i] > rating[j]:
                left_large += 1
        
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_small += 1
            elif rating[k] > rating[j]:
                right_large += 1
        
        count += left_small * right_large + left_large * right_small
    
    return count

ratings = [2,5,3,4,1]
print("number of teams:", num_teams(ratings))


# max sum of subarray after removing one element
def max_sum_after_removal(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    forward = [0] * n
    backward = [0] * n
    
    # max sum ending at i
    forward[0] = arr[0]
    for i in range(1, n):
        forward[i] = max(arr[i], forward[i-1] + arr[i])
    
    # max sum starting at i
    backward[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        backward[i] = max(arr[i], backward[i+1] + arr[i])
    
    # try removing each element
    max_sum = max(forward)  # without removing any
    for i in range(n):
        if i == 0:
            max_sum = max(max_sum, backward[1])
        elif i == n-1:
            max_sum = max(max_sum, forward[n-2])
        else:
            max_sum = max(max_sum, forward[i-1] + backward[i+1])
    
    return max_sum

arr = [1,-2,0,3]
print("max sum after removal:", max_sum_after_removal(arr))


# longest increasing subsequence (binary search version)
def length_of_lis(nums):
    tails = []
    
    for num in nums:
        # binary search for position to insert
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

nums = [10,9,2,5,3,7,101,18]
print("LIS length:", length_of_lis(nums))


# number of longest increasing subsequence
def find_number_of_lis(nums):
    if not nums:
        return 0
    
    n = len(nums)
    length = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    
    max_len = max(length)
    total = sum(count[i] for i in range(n) if length[i] == max_len)
    
    return total

nums = [1,3,5,4,7]
print("number of LIS:", find_number_of_lis(nums))
