# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Runtime: 188 ms, faster than 17.97% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1 and not l2:
            return None

        a, b = 0, 0

        if l1:
            a = l1.val

        if l2:
            b = l2.val


        s = a + b
        curry = s // 10
        s = s % 10

        root = ListNode(s)
        rest = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None)

        if curry:
            rest = self.addTwoNumbers(rest, ListNode(curry))

        root.next = rest

        return root
