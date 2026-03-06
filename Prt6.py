# climbing stairs (using array)
def climb_stairs_array(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print("ways to climb 5 stairs:", climb_stairs_array(5))

# remove duplicates from sorted list (linked list)
def delete_duplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# test
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print("list before removing duplicates:")
printList(head)
result = delete_duplicates(head)
print("after removing duplicates:")
printList(result)

# merge sorted array (in-place)
def merge_sorted(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print("merged:", merge_sorted(nums1, 3, nums2, 3))

# inorder traversal (binary tree)
def inorder_traversal(root):
    result = []
    
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print("inorder traversal:", inorder_traversal(tree))

# symmetric tree
def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    
    return is_mirror(root, root)

sym_tree = TreeNode(1)
sym_tree.left = TreeNode(2)
sym_tree.right = TreeNode(2)
sym_tree.left.left = TreeNode(3)
sym_tree.left.right = TreeNode(4)
sym_tree.right.left = TreeNode(4)
sym_tree.right.right = TreeNode(3)

print("is tree symmetric?", is_symmetric(sym_tree))

# maximum depth of binary tree
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

print("max depth:", max_depth(sym_tree))

# convert sorted array to binary search tree
def sorted_array_to_bst(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root

arr = [-10, -3, 0, 5, 9]
bst_root = sorted_array_to_bst(arr)
print("bst created from sorted array")

# balanced binary tree
def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left = check_height(node.left)
        right = check_height(node.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    return check_height(root) != -1

print("is tree balanced?", is_balanced(sym_tree))
