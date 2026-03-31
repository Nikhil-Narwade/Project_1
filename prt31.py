# binary tree maximum path sum
def max_path_sum(root):
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # path through current node
        current_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path)
        
        # return max path starting at this node
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

# test tree
path_tree = TreeNode(-10)
path_tree.left = TreeNode(9)
path_tree.right = TreeNode(20)
path_tree.right.left = TreeNode(15)
path_tree.right.right = TreeNode(7)
print("max path sum:", max_path_sum(path_tree))


# binary tree right side view
def right_side_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

right_tree = TreeNode(1)
right_tree.left = TreeNode(2)
right_tree.right = TreeNode(3)
right_tree.left.right = TreeNode(5)
right_tree.right.right = TreeNode(4)
print("right side view:", right_side_view(right_tree))

# binary tree level order traversal (bottom up)
def level_order_bottom(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.insert(0, level)
    
    return result

print("bottom up level order:", level_order_bottom(right_tree))


# zigzag level order traversal
def zigzag_level_order(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    left_to_right = True
    
    while queue:
        level = []
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    
    return result

print("zigzag traversal:", zigzag_level_order(right_tree))
