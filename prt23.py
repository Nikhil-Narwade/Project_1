# find the celebrity (knows matrix)
def find_celebrity(n, knows_func):
    candidate = 0
    
    # find potential celebrity
    for i in range(1, n):
        if knows_func(candidate, i):
            candidate = i
    
    # verify candidate
    for i in range(n):
        if i != candidate:
            if knows_func(candidate, i) or not knows_func(i, candidate):
                return -1
    
    return candidate

# example knows function (just for demo)
def knows(a, b):
    matrix = [[0,1,1],[0,0,1],[0,0,0]]
    return matrix[a][b] == 1

print("celebrity in 3 people:", find_celebrity(3, knows))


# partition labels (split string into parts)
def partition_labels(s):
    last_occurrence = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    
    for i, c in enumerate(s):
        end = max(end, last_occurrence[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    
    return result

print("partition 'ababcbacadefegdehijhklij':", 
      partition_labels("ababcbacadefegdehijhklij"))


# interval list intersections
def interval_intersection(first_list, second_list):
    result = []
    i = j = 0
    
    while i < len(first_list) and j < len(second_list):
        # find overlap
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])
        
        if start <= end:
            result.append([start, end])
        
        # move pointer for interval that ends first
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    
    return result

first = [[0,2],[5,10],[13,23],[24,25]]
second = [[1,5],[8,12],[15,24],[25,26]]
print("intersections:", interval_intersection(first, second))


#  insert interval
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    
    # add all intervals that end before new starts
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    
    # add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

intervals = [[1,3],[6,9]]
new = [2,5]
print("insert [2,5]:", insert_interval(intervals, new))
