# all possible full binary trees
def all_possible_fbt(n):
    if n % 2 == 0:
        return []
    if n == 1:
        return [TreeNode(0)]
    
    result = []
    for i in range(1, n, 2):
        left_trees = all_possible_fbt(i)
        right_trees = all_possible_fbt(n - 1 - i)
        
        for left in left_trees:
            for right in right_trees:
                root = TreeNode(0)
                root.left = left
                root.right = right
                result.append(root)
    
    return result

fbt_trees = all_possible_fbt(7)
print("number of full binary trees with 7 nodes:", len(fbt_trees))


# graph valid tree
def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor, node):
                    return False
            elif neighbor != parent:
                return False
        return True
    
    if not dfs(0, -1):
        return False
    
    return all(visited)

edges = [[0,1],[0,2],[0,3],[1,4]]
print("is valid tree?", valid_tree(5, edges))

# clone graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None
    
    visited = {}
    
    def dfs(original):
        if original in visited:
            return visited[original]
        
        clone = Node(original.val)
        visited[original] = clone
        
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)

# test graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned = clone_graph(node1)
print("graph cloned! original value:", node1.val, "cloned value:", cloned.val)
