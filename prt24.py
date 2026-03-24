# non overlapping intervals
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print("remove to make non-overlap:", erase_overlap_intervals(intervals))


#  meeting rooms II (min meeting rooms needed)
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    
    rooms = 0
    end_ptr = 0
    
    for start in start_times:
        if start < end_times[end_ptr]:
            rooms += 1
        else:
            end_ptr += 1
    
    return rooms

meetings = [[0,30],[5,10],[15,20]]
print("minimum rooms needed:", min_meeting_rooms(meetings))

# car fleet (cars reaching destination)
def car_fleet(target, position, speed):
    pairs = [(position[i], speed[i]) for i in range(len(position))]
    pairs.sort(reverse=True)  # sort by position descending
    
    stack = []
    for pos, sp in pairs:
        time = (target - pos) / sp
        if not stack or time > stack[-1]:
            stack.append(time)
    
    return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print("car fleets:", car_fleet(target, position, speed))

# -------------------------------------

# network delay time (dijkstra)
import heapq

def network_delay_time(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    
    distances = [float('inf')] * (n + 1)
    distances[k] = 0
    heap = [(0, k)]
    
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    max_dist = max(distances[1:])
    return max_dist if max_dist != float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
print("network delay time:", network_delay_time(times, 4, 2))
