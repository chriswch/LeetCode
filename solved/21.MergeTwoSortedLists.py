# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node1 = list1
        node2 = list2

        dummy = ListNode()
        curr = dummy
        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                curr = node1

                node1 = node1.next
            else:
                curr.next = node2
                curr = node2

                node2 = node2.next

        curr.next = node1 if node1 else node2
        return dummy.next

