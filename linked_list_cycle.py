# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Your solution goes here
        hashmap = {}
        while head:
            if head in hashmap:
                return True
            hashmap[head] = head
            head = head.next
        return False

        pass


def build_linked_list(values, pos):
    """
    values: list of node values
    pos: index where the tail connects (-1 for no cycle)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# --------------------
# Test cases
# --------------------
sol = Solution()

# Example 1: [3,2,0,-4], cycle at index 1
head1 = build_linked_list([3, 2, 0, -4], 1)
print(sol.hasCycle(head1))  # Expected: True

# Example 2: [1,2], cycle at index 0
head2 = build_linked_list([1, 2], 0)
print(sol.hasCycle(head2))  # Expected: True

# Example 3: [1], no cycle
head3 = build_linked_list([1], -1)
print(sol.hasCycle(head3))  # Expected: False

# Empty list
head4 = build_linked_list([], -1)
print(sol.hasCycle(head4))  # Expected: False

# Longer list without cycle
head5 = build_linked_list([1, 2, 3, 4, 5], -1)
print(sol.hasCycle(head5))  # Expected: False