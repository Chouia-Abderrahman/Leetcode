# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        empty_list = ListNode()
        end_of_list = empty_list
        while list1 and list2:
            if list1.val < list2.val:
                end_of_list.next = list1
                list1 = list1.next
            else:
                end_of_list.next = list2
                list2 = list2.next

            end_of_list = end_of_list.next
        end_of_list.next = list1 if list1 else list2
        return empty_list.next



def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_list(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


# Test
list1 = build_list([1, 2, 4])
list2 = build_list([1, 3, 4])

solution = Solution()
result = solution.mergeTwoLists(list1, list2)

print_list(result)
