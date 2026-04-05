# smallest string with swaps
def smallest_string_with_swaps(s, pairs):
    from collections import defaultdict
    
    parent = list(range(len(s)))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # union connected indices
    for x, y in pairs:
        union(x, y)
    
    # group indices by root
    groups = defaultdict(list)
    for i in range(len(s)):
        groups[find(i)].append(i)
    
    # build result
    result = [''] * len(s)
    for indices in groups.values():
        chars = sorted(s[i] for i in indices)
        for idx, char in zip(sorted(indices), chars):
            result[idx] = char
    
    return ''.join(result)

s = "dcab"
pairs = [[0,3],[1,2]]
print("smallest string:", smallest_string_with_swaps(s, pairs))


# evaluate division
def calc_equation(equations, values, queries):
    from collections import defaultdict
    
    graph = defaultdict(dict)
    
    # build graph
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val
    
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        
        if start == end:
            return 1.0
        
        visited.add(start)
        for neighbor, val in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return val * result
        return -1.0
    
    results = []
    for a, b in queries:
        results.append(dfs(a, b, set()))
    
    return results

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"]]
print("evaluations:", calc_equation(equations, values, queries))
