# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode()
        prev = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while True:
                    curr = curr.next
                    if not curr.next or curr.val != curr.next.val:
                        break
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        prev.next = curr

        return dummy.next
