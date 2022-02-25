# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        # Simply count the length of linked list
        def getSize(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next

            return cnt

        # Given the head & size, return the the start node of next chunk
        def split(start, size):
            for _ in range(size - 1):
                if not start:
                    break
                start = start.next

            if not start:
                return None
            next_start, start.next = start.next, None  # disconnect

            return next_start

        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            while curr.next:
                curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
            return curr

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1

        while size < total_length:
            dummy_start = dummy
            start = dummy.next
            while start:
                left = start
                right = split(left, size)  # start from left, cut with size=size
                start = split(right, size)  # start from right, cut with size=size
                dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start
            size *= 2
        return dummy.next
