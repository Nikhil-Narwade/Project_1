# maximum points on a line
def max_points(points):
    if len(points) <= 2:
        return len(points)
    
    from collections import defaultdict
    
    max_count = 0
    
    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicate = 0
        vertical = 0
        
        for j in range(i+1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            
            if dx == 0 and dy == 0:
                duplicate += 1
            elif dx == 0:
                vertical += 1
            else:
                # reduce fraction
                from math import gcd
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                slopes[(dx, dy)] += 1
        
        max_count = max(max_count, vertical + duplicate + 1)
        for count in slopes.values():
            max_count = max(max_count, count + duplicate + 1)
    
    return max_count

points = [[1,1],[2,2],[3,3]]
print("max points on line:", max_points(points))


# race car (hard bfs)
def racecar(target):
    from collections import deque
    
    queue = deque([(0, 1, 0)])  # position, speed, steps
    visited = set([(0, 1)])
    
    while queue:
        pos, speed, steps = queue.popleft()
        
        if pos == target:
            return steps
        
        # accelerate
        new_pos = pos + speed
        new_speed = speed * 2
        if (new_pos, new_speed) not in visited:
            visited.add((new_pos, new_speed))
            queue.append((new_pos, new_speed, steps + 1))
        
        # reverse
        new_speed = -1 if speed > 0 else 1
        if (pos, new_speed) not in visited:
            visited.add((pos, new_speed))
            queue.append((pos, new_speed, steps + 1))
    
    return -1

print("racecar to target 3:", racecar(3))
