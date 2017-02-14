# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):

        dummy = ListNode(None)
        dummy.next = head

        P0 = dummy  # initial P0
        while P0.next is not None and P0.next.next is not None:
            # Set new cycle of pointers
            P1 = P0.next
            P2 = P1.next
            P3 = P2.next
            # Swap two nodes
            P0.next = P2
            P2.next = P1
            P1.next = P3
            # Update P0, move forward two steps
            P0 = P1

        return dummy.next
# Time: O(n)
# Space: O(1)
