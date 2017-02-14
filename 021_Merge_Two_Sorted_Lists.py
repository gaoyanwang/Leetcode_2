# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):

        # Initialize new list and pointer
        dummy = ListNode(None)
        p3 = dummy

        # Normal case:
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current = ListNode(l1.val)
                l1 = l1.next
            else:
                current = ListNode(l2.val)
                l2 = l2.next
            p3.next = current
            p3 = p3.next

        # if l1 reach end:
        if l1 is None:
            p3.next = l2
        else:
            p3.next = l1

        return dummy.next

# Time: O(n)
# Space: O(n)
