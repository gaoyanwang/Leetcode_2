# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Set up a pointer
        dummy = ListNode(None)
        dummy.next = head

        # Set up second pointer
        p1 = dummy
        p2 = dummy

        #  Set p2 ahead of p1 n steps
        for i in range(n):
            p2 = p2.next
            if p2 is None:  # n bigger than node numbers
                return 0

        # Remove the nth node
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next

        return dummy.next

# Time: O(n)
# Space: O(1)
