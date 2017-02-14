# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(None)
        dummy.next = head

        p1 = dummy
        p2 = dummy

        # P2 move to last node, p1 move to middle
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        
        # Reverse p1.next no matter odd or even
        p2 = self.reverseList(p1.next)

        p1.next = None

        # compare p1 and p2 val of each node
        while p1 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    # helper function
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head.next
        ret = self.reverseList(head.next)  # ret?
        p.next = head  # p location did not change
        head.next = None
        return ret
