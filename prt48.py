# shortest path in binary matrix
def shortest_path_binary_matrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    n = len(grid)
    queue = [(0, 0, 1)]  # row, col, distance
    grid[0][0] = 1  # mark visited
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    while queue:
        i, j, dist = queue.pop(0)
        
        if i == n-1 and j == n-1:
            return dist
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                grid[x][y] = 1
                queue.append((x, y, dist + 1))
    
    return -1

grid = [[0,1],[1,0]]
print("shortest path length:", shortest_path_binary_matrix(grid))


# number of connected components in undirected graph
def count_components(n, edges):
    parent = list(range(n))
    rank = [1] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return 0
        
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return 1
    
    components = n
    for u, v in edges:
        components -= union(u, v)
    
    return components

edges = [[0,1],[1,2],[3,4]]
print("connected components:", count_components(5, edges))


# minimum number of arrows to burst balloons
def find_min_arrow_shots(points):
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    
    for start, balloon_end in points[1:]:
        if start > end:
            arrows += 1
            end = balloon_end
    
    return arrows

points = [[10,16],[2,8],[1,6],[7,12]]
print("minimum arrows:", find_min_arrow_shots(points))
