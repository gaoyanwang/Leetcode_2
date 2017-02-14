# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        p1 = headA
        p2 = headB

        # 1
        while p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next

        if p1 is None:
            p1 = headB
        else:
            p2 = headA

        # 2
        while p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next

        if p1 is None:
            p1 = headB
        else:
            p2 = headA

        # 3
        while p1 is not None and p2 is not None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None

# Time: O(max(m,n))
# Space: O(1)
