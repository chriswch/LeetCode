# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        opds = [l1, l2]

        head = ListNode()
        curr = head
        carry = 0
        while opds:
            next_opds = []
            for opd in opds:
                carry += opd.val

                if opd.next:
                    next_opds.append(opd.next)

            if carry < 10:
                val = carry
                carry = 0
            else:
                val = carry - 10
                carry = 1

            curr.next = ListNode(val)
            curr = curr.next

            opds = next_opds

        if carry:
            curr.next = ListNode(carry)

        return head.next
