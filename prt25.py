# reorder data in log files
def reorder_log_files(logs):
    letters = []
    digits = []
    
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    # sort letters by content then identifier
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    
    return letters + digits

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print("reordered logs:", reorder_log_files(logs))


# maximum width of binary tree
def width_of_binary_tree(root):
    if not root:
        return 0
    
    queue = [(root, 0)]
    max_width = 0
    
    while queue:
        level_size = len(queue)
        first_idx = queue[0][1]
        
        for i in range(level_size):
            node, idx = queue.pop(0)
            if node.left:
                queue.append((node.left, 2 * idx))
            if node.right:
                queue.append((node.right, 2 * idx + 1))
        
        last_idx = idx
        max_width = max(max_width, last_idx - first_idx + 1)
    
    return max_width

# test tree
width_tree = TreeNode(1)
width_tree.left = TreeNode(3)
width_tree.right = TreeNode(2)
width_tree.left.left = TreeNode(5)
width_tree.left.right = TreeNode(3)
width_tree.right.right = TreeNode(9)

print("max width:", width_of_binary_tree(width_tree))
