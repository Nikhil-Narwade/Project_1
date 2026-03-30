
# alien dictionary
def alien_order(words):
    from collections import defaultdict, deque
    
    # build graph
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        min_len = min(len(word1), len(word2))
        
        # check for invalid case
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    
    # topological sort
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    
    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in graph[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ''.join(result) if len(result) == len(in_degree) else ""

words = ["wrt","wrf","er","ett","rftt"]
print("alien order:", alien_order(words))

# reconstruct itinerary
def find_itinerary(tickets):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)
    
    route = []
    
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)
    
    dfs("JFK")
    return route[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print("itinerary:", find_itinerary(tickets))

# palindrome pairs
def palindrome_pairs(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    result = []
    word_dict = {word: i for i, word in enumerate(words)}
    
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            if is_palindrome(prefix):
                rev_suffix = suffix[::-1]
                if rev_suffix in word_dict and word_dict[rev_suffix] != i:
                    result.append([word_dict[rev_suffix], i])
            
            if j != len(word) and is_palindrome(suffix):
                rev_prefix = prefix[::-1]
                if rev_prefix in word_dict and word_dict[rev_prefix] != i:
                    result.append([i, word_dict[rev_prefix]])
    
    return result

words = ["abcd","dcba","lls","s","sssll"]
print("palindrome pairs:", palindrome_pairs(words))
