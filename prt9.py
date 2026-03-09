# find mode in binary search tree
def find_mode(root):
    if not root:
        return []
    

    def inorder(node, vals):
        if not node:
            return
        inorder(node.left, vals)
        vals.append(node.val)
        inorder(node.right, vals)
    
    vals = []
    inorder(root, vals)
    

    freq = {}
    max_freq = 0
    for val in vals:
        freq[val] = freq.get(val, 0) + 1
        max_freq = max(max_freq, freq[val])
    

    return [val for val, f in freq.items() if f == max_freq]

bst = TreeNode(1)
bst.right = TreeNode(2)
bst.right.left = TreeNode(2)
print("mode in bst:", find_mode(bst))



# relative ranks (medal for top 3)
def find_relative_ranks(score):
    sorted_scores = sorted(score, reverse=True)
    rank_map = {}
    
    for i, s in enumerate(sorted_scores):
        if i == 0:
            rank_map[s] = "Gold Medal"
        elif i == 1:
            rank_map[s] = "Silver Medal"
        elif i == 2:
            rank_map[s] = "Bronze Medal"
        else:
            rank_map[s] = str(i + 1)
    
    return [rank_map[s] for s in score]

scores = [5,4,3,2,1]
print("ranks:", find_relative_ranks(scores))


# detect capital (check if word capitalization is correct)
def detect_capital_use(word):

    return (word.isupper() or 
            word.islower() or 
            (word[0].isupper() and word[1:].islower()))

print("USA correct?", detect_capital_use("USA"))
print("Google correct?", detect_capital_use("Google"))
print("FlaG correct?", detect_capital_use("FlaG"))

# -------------------------------------

# repeated substring pattern
def repeated_substring_pattern(s):


    doubled = (s + s)[1:-1]
    return s in doubled

print("'abab' repeated pattern?", repeated_substring_pattern("abab"))
print("'aba' repeated pattern?", repeated_substring_pattern("aba"))


# hamming distance (bits differ)
def hamming_distance(x, y):

    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

print("hamming distance between 1 (01) and 4 (100):", 
      hamming_distance(1, 4))
