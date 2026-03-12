# number of islands (dfs)
def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'  # mark as visited
        
        # check all 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    
    return count

island_grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]
print("number of islands:", num_islands(island_grid))


# course schedule (cycle detection)
def can_finish(num_courses, prerequisites):
    # build graph
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * num_courses
    
    def has_cycle(course):
        if visited[course] == 1:  # currently visiting -> cycle
            return True
        if visited[course] == 2:  # already processed
            return False
        
        visited[course] = 1  # mark as visiting
        
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        
        visited[course] = 2  # mark as visited
        return False
    
    for course in range(num_courses):
        if has_cycle(course):
            return False
    
    return True

print("can finish 2 courses with [[1,0]]?", 
      can_finish(2, [[1,0]]))


# kth largest element in array
def find_kth_largest(nums, k):
    # quick select or just sort for simplicity
    nums.sort(reverse=True)
    return nums[k-1]

print("3rd largest in [3,2,1,5,6,4]:", 
      find_kth_largest([3,2,1,5,6,4], 3))


# top k frequent elements
def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

print("top 2 frequent in [1,1,1,2,2,3]:", 
      top_k_frequent([1,1,1,2,2,3], 2))

# valid binary search tree
def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
    
    return validate(root, float('-inf'), float('inf'))

bst = TreeNode(2)
bst.left = TreeNode(1)
bst.right = TreeNode(3)
print("is valid bst?", is_valid_bst(bst))
