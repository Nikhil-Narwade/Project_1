# lowest common ancestor
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right

# test lca
lca_tree = TreeNode(3)
lca_tree.left = TreeNode(5)
lca_tree.right = TreeNode(1)
lca_tree.left.left = TreeNode(6)
lca_tree.left.right = TreeNode(2)
lca_tree.right.left = TreeNode(0)
lca_tree.right.right = TreeNode(8)
lca_tree.left.right.left = TreeNode(7)
lca_tree.left.right.right = TreeNode(4)

p = lca_tree.left  # node 5
q = lca_tree.left.right.right  # node 4
lca = lowest_common_ancestor(lca_tree, p, q)
print("LCA value:", lca.val if lca else None)


# serialize and deserialize binary tree
class Codec:
    def serialize(self, root):
        if not root:
            return "null"
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
    
    def deserialize(self, data):
        if data == "null":
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1
        
        while queue and i < len(nodes):
            node = queue.pop(0)
            
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root

codec = Codec()
serialized = codec.serialize(right_tree)
print("serialized:", serialized)
deserialized = codec.deserialize(serialized)
print("deserialized root value:", deserialized.val)


# binary tree cameras
def min_camera_cover(root):
    # 0: not covered, 1: covered, 2: has camera
    cameras = 0
    
    def dfs(node):
        nonlocal cameras
        if not node:
            return 1  # covered
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if left == 0 or right == 0:
            cameras += 1
            return 2  # has camera
        
        if left == 2 or right == 2:
            return 1  # covered
        
        return 0  # not covered
    
    if dfs(root) == 0:
        cameras += 1
    
    return cameras

camera_tree = TreeNode(0)
camera_tree.left = TreeNode(0)
camera_tree.left.left = TreeNode(0)
camera_tree.left.right = TreeNode(0)
print("min cameras needed:", min_camera_cover(camera_tree))
