from os import WCONTINUED


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        if head.next is None:
            return head

        nav = head.next
        prev = head
        prev.next = None
        while nav.next:
            temp = nav.next
            nav.next = prev
            prev = nav
            nav = temp
        # nav = prev
        nav.next = prev
        return nav






def create_linked_list(values):
    """Create a linked list from a Python list."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    """Print a linked list as: 1 -> 2 -> 3"""
    values = []
    current = head

    while current:
        values.append(str(current.val))
        current = current.next

    print(" -> ".join(values))


# Test it
values = [1, 2, 3, 4, 5]

head = create_linked_list(values)

print("Before:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("After:")
print_linked_list(reversed_head)
