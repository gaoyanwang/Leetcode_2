# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        p1 = dummy
        while p1.next is not None:
            if p1.next.val != val:
                p1 = p1.next
            else:
                p1.next = p1.next.next
        return dummy.next

# Time: O(n)
# Space: O(1)
