# 002_Add_Two_Numbers
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        temp = dummy
        carry = 0

        # Both are not None
        while l1 is not None and l2 is not None:
            digit = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next
            temp.next = digit
            temp = digit

        while l2 is not None:
            digit = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            l2 = l2.next
            temp.next = digit
            temp = digit

        while l1 is not None:
            digit = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            l1 = l1.next
            temp.next = digit
            temp = digit

        # process possible left carry
        if carry != 0:
            temp.next = ListNode(carry)

        return dummy.next
# Time: O(n)
# Space:O(1)