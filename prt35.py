# pacific atlantic water flow
def pacific_atlantic(matrix):
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]
    
    def dfs(i, j, ocean):
        ocean[i][j] = True
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if (0 <= x < rows and 0 <= y < cols and 
                not ocean[x][y] and matrix[x][y] >= matrix[i][j]):
                dfs(x, y, ocean)
    
    # from borders
    for i in range(rows):
        dfs(i, 0, pacific)  # left border
        dfs(i, cols-1, atlantic)  # right border
    
    for j in range(cols):
        dfs(0, j, pacific)  # top border
        dfs(rows-1, j, atlantic)  # bottom border
    
    result = []
    for i in range(rows):
        for j in range(cols):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    
    return result

ocean_matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print("pacific atlantic cells:", pacific_atlantic(ocean_matrix)[:5])  # first 5


# regions cut by slashes
def regions_by_slashes(grid):
    n = len(grid)
    # upscale to 3x3 for each cell to handle slashes
    size = n * 3
    matrix = [[0] * size for _ in range(size)]
    
    # mark cells
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '/':
                matrix[i*3][j*3+2] = 1
                matrix[i*3+1][j*3+1] = 1
                matrix[i*3+2][j*3] = 1
            elif grid[i][j] == '\\':
                matrix[i*3][j*3] = 1
                matrix[i*3+1][j*3+1] = 1
                matrix[i*3+2][j*3+2] = 1
    
    # dfs to count regions
    def dfs(i, j):
        if i < 0 or i >= size or j < 0 or j >= size or matrix[i][j] == 1:
            return
        matrix[i][j] = 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                count += 1
                dfs(i, j)
    
    return count

grid = [" /","/ "]
print("regions by slashes:", regions_by_slashes(grid))
