# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



# ---------- Test boilerplate ----------

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a tree from a list in level-order (LeetCode style), None = missing node."""
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


def tree_to_list(root):
    """Convert tree back to level-order list (with None for missing nodes, trimmed at the end)."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def print_tree(root, level=0, prefix="Root: "):
    """Quick visual sanity check."""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


if __name__ == "__main__":
    test_cases = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3],
        [],
        [1],
    ]

    sol = Solution()
    for values in test_cases:
        root = build_tree(values)
        print(f"Input:    {values}")
        result = sol.invertTree(root)
        print(f"Output:   {tree_to_list(result)}")
        print("-" * 40)