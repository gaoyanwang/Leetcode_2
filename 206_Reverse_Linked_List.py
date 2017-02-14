# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head

        ret = None

        while tmp is not None:
            p1 = tmp.next
            tmp.next = ret
            ret = tmp
            tmp = p1
        return ret

# Time: O(n)
# Space: O(1)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head.next
        ret = self.reverseList(head.next)
        p.next = head
        head.next = None
        return ret

# Time: O(n)
# Space: O(n)

