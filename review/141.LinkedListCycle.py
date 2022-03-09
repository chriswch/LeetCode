# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd Cycle Detection Algorithm
        # (Tortoise and Hare Algorithm)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False

    def hasCycle_1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = []

        curr = head
        while curr:
            if curr in nodes:
                return True
            else:
                nodes.append(curr)
                curr = curr.next

        return False
