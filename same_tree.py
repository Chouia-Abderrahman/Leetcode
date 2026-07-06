from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))







# -------- Test Code --------

# Tree 1:
#     1
#    / \
#   2   3
tree1 = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Tree 2:
#     1
#    / \
#   2   3
tree2 = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

# Tree 3:
#     1
#    / \
#   2   4
tree3 = TreeNode(
    1,
    TreeNode(2),
    TreeNode(4)
)

sol = Solution()

print(sol.isSameTree(tree1, tree2))  # Expected: True
print(sol.isSameTree(tree1, tree3))  # Expected: False
print(sol.isSameTree(None, None))    # Expected: True
print(sol.isSameTree(tree1, None))   # Expected: False