# largest rectangle in histogram
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

heights = [2,1,5,6,2,3]
print("largest rectangle area:", largest_rectangle_area(heights))


# maximal rectangle (binary matrix)
def maximal_rectangle(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print("maximal rectangle:", maximal_rectangle(matrix))


# word search II (trie + backtracking)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_words(board, words):
    # build trie
    root = TrieNode()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    
    rows, cols = len(board), len(board[0])
    result = []
    
    def backtrack(i, j, node):
        if board[i][j] not in node.children:
            return
        
        char = board[i][j]
        node = node.children[char]
        
        if node.word:
            result.append(node.word)
            node.word = None  # avoid duplicates
        
        # mark as visited
        board[i][j] = '#'
        
        # explore neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and board[x][y] != '#':
                backtrack(x, y, node)
        
        # unmark
        board[i][j] = char
    
    for i in range(rows):
        for j in range(cols):
            backtrack(i, j, root)
    
    return result

board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
print("words found:", find_words(board, words))
