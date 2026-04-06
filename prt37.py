# most stones removed with same row or column
def remove_stones(stones):
    # union find for rows and columns
    parent = {}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent.setdefault(x, x)
        parent.setdefault(y, y)
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    for i, (x, y) in enumerate(stones):
        # use negative for columns to avoid collision
        union(x, ~y)
    
    roots = set(find(x) for x in parent)
    return len(stones) - len(roots)

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print("stones removed:", remove_stones(stones))


# accounts merge
def accounts_merge(accounts):
    from collections import defaultdict
    
    parent = list(range(len(accounts)))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # map email to index
    email_to_index = {}
    
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_index:
                union(i, email_to_index[email])
            else:
                email_to_index[email] = i
    
    # group emails by root index
    index_to_emails = defaultdict(set)
    for email, idx in email_to_index.items():
        root = find(idx)
        index_to_emails[root].add(email)
    
    # build result
    result = []
    for idx, emails in index_to_emails.items():
        result.append([accounts[idx][0]] + sorted(emails))
    
    return result

accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
print("merged accounts:", accounts_merge(accounts))


# count sub islands
def count_sub_islands(grid1, grid2):
    rows, cols = len(grid1), len(grid1[0])
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid2[i][j] == 0:
            return True
        
        grid2[i][j] = 0  # mark visited
        is_sub = grid1[i][j] == 1
        
        # check all 4 directions
        is_sub &= dfs(i+1, j)
        is_sub &= dfs(i-1, j)
        is_sub &= dfs(i, j+1)
        is_sub &= dfs(i, j-1)
        
        return is_sub
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid2[i][j] == 1 and dfs(i, j):
                count += 1
    
    return count

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print("sub islands:", count_sub_islands(grid1, grid2))
