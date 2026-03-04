# invert binary tree (max meme potential lol)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    
    # swap children
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# making a simple tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("tree inverted ")



# palindrome linked list
def isPalindrome(head):
    # convert to list 
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]

pal_list = ListNode(1)
pal_list.next = ListNode(2)
pal_list.next.next = ListNode(2)
pal_list.next.next.next = ListNode(1)

print("linked list palindrome?", isPalindrome(pal_list))


# lowest common ancestor of binary search tree
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None

# bst for testing
bst = TreeNode(6)
bst.left = TreeNode(2)
bst.right = TreeNode(8)
bst.left.left = TreeNode(0)
bst.left.right = TreeNode(4)
bst.right.left = TreeNode(7)
bst.right.right = TreeNode(9)
bst.left.right.left = TreeNode(3)
bst.left.right.right = TreeNode(5)

print("lca of 2 and 8 should be 6 ")


#  two sum II (sorted array)
def twoSumSorted(numbers, target):
    left, right = 0, len(numbers)-1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left+1, right+1]  # 1-indexed
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

print("two sum in [2,7,11,15] target 9:", 
      twoSumSorted([2,7,11,15], 9))



# excel sheet column number (like A=1, B=2, ... Z=26, AA=27)
def titleToNumber(columnTitle):
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

print("AB ->", titleToNumber("AB"))
print("ZY ->", titleToNumber("ZY"))



# number of 1 bits
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print("1 bits in 11 (1011):", hammingWeight(11))

