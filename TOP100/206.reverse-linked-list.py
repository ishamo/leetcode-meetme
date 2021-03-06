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

        if not head or not head.next: return head

        p, cur = None, head
        while cur:
            cur.next, cur, p = p, cur.next, cur

        return p
