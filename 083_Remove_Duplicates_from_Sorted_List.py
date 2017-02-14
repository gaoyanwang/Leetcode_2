# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head

        pointer1 = dummy
        pointer2 = head

        while pointer2 is not None:
            if pointer2.val != pointer1.val:
                pointer1.next = pointer2
                pointer1 = pointer2
            pointer2 = pointer2.next
        pointer1.next = pointer2
        return dummy.next

# Space: O(1)
# Time: O(n)
