# course schedule II
def find_order(num_courses, prerequisites):
    from collections import deque
    
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return order if len(order) == num_courses else []

prereqs = [[1,0],[2,0],[3,1],[3,2]]
print("course order:", find_order(4, prereqs))


# minimum height trees
def find_min_height_trees(n, edges):
    if n == 1:
        return [0]
    
    graph = [[] for _ in range(n)]
    degrees = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    leaves = [i for i in range(n) if degrees[i] == 1]
    
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            degrees[neighbor] -= 1
            if degrees[neighbor] == 1:
                new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves

mht_edges = [[1,0],[1,2],[1,3]]
print("minimum height trees:", find_min_height_trees(4, mht_edges))


# word ladder (shortest transformation sequence)
def ladder_length(begin_word, end_word, word_list):
    from collections import deque
    
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    
    queue = deque([(begin_word, 1)])
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    
    return 0

begin = "hit"
end = "cog"
word_list = ["hot","dot","dog","lot","log","cog"]
print("word ladder length:", ladder_length(begin, end, word_list))
