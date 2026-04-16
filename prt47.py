# basic calculator (with +, -, parentheses)
def calculate(s):
    stack = []
    current_num = 0
    result = 0
    sign = 1
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '+':
            result += sign * current_num
            current_num = 0
            sign = 1
        elif char == '-':
            result += sign * current_num
            current_num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * current_num
            current_num = 0
            result *= stack.pop()  # sign
            result += stack.pop()  # previous result
    
    result += sign * current_num
    return result

print("calculate '1 + 1':", calculate("1 + 1"))
print("calculate '2-1 + 2':", calculate("2-1 + 2"))
print("calculate '(1+(4+5+2)-3)+(6+8)':", calculate("(1+(4+5+2)-3)+(6+8)"))


# serialize and deserialize n-ary tree
class NaryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

def serialize_nary(root):
    if not root:
        return ""
    
    result = [str(root.val)]
    
    for child in root.children:
        result.append(serialize_nary(child))
    
    result.append("#")  # end marker
    return ','.join(result)

def deserialize_nary(data):
    if not data:
        return None
    
    def helper(queue):
        val = queue.pop(0)
        if val == "#":
            return None
        
        node = NaryNode(int(val))
        while queue and queue[0] != "#":
            child = helper(queue)
            if child:
                node.children.append(child)
        
        queue.pop(0)  # remove "#"
        return node
    
    queue = data.split(',')
    return helper(queue)

nary_root = NaryNode(1)
child1 = NaryNode(3)
child2 = NaryNode(2)
child3 = NaryNode(4)
child1.children = [NaryNode(5), NaryNode(6)]
nary_root.children = [child1, child2, child3]

serialized = serialize_nary(nary_root)
print("n-ary serialized:", serialized)


# critical connections in network (tarjan)
def critical_connections(n, connections):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    ids = [-1] * n
    low = [0] * n
    visited = [False] * n
    bridges = []
    id_counter = 0
    
    def dfs(at, parent):
        nonlocal id_counter
        visited[at] = True
        id_counter += 1
        ids[at] = low[at] = id_counter
        
        for to in graph[at]:
            if to == parent:
                continue
            if not visited[to]:
                dfs(to, at)
                low[at] = min(low[at], low[to])
                if ids[at] < low[to]:
                    bridges.append([at, to])
            else:
                low[at] = min(low[at], ids[to])
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    
    return bridges

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print("critical connections:", critical_connections(n, connections))
