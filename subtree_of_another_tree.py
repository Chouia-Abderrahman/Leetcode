# Definition for a binary tree node.
from operator import truediv


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return False
        if self.same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return self.same_tree(a.left, b.left) and self.same_tree(a.right, b.right)



# ---------- Helpers ----------

def build_tree(values):
    """Build a tree from a LeetCode-style level-order list (None = null)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
    return root


def print_tree(node, indent=0):
    """Quick visual check of a tree, sideways."""
    if node is not None:
        print_tree(node.right, indent + 4)
        print(" " * indent + str(node.val))
        print_tree(node.left, indent + 4)


# ---------- Test cases ----------

test_cases = [
    # (root list, subRoot list, expected)
    ([3,4,5,1,2], [4,1,2], True),
    ([3,4,5,1,2,None,None,None,None,0], [4,1,2], False),
    ([1,1], [1], True),
    ([1], [1], True),
    ([1,2], [2,3], False),
]

sol = Solution()

for i, (root_list, sub_list, expected) in enumerate(test_cases):
    root = build_tree(root_list)
    subRoot = build_tree(sub_list)
    result = sol.isSubtree(root, subRoot)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i+1}: {status} (got {result}, expected {expected})")