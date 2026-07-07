from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




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

print(sol.maxDepth(tree1))  # Expected: True
print(sol.maxDepth(tree3))  # Expected: False
print(sol.maxDepth(tree2))   # Expected: False