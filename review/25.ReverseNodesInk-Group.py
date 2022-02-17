# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if k == 1:
            return head

        dummy = ListNode(0, head)
        prev, end = dummy, dummy
        while True:
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next
            rhead, rtail = self.reverseList(prev.next, end.next)
            prev.next = rhead
            prev, end = rtail, rtail
        return dummy.next

    def reverseList(self, head, tail):
        curr, rhead = head, tail
        while curr is not tail:
            curr_next = curr.next
            curr.next = rhead
            rhead = curr
            curr = curr_next
        return rhead, head

    def reverseKGroup_1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        curr = head
        linked_list = []
        while curr:
            linked_list.append(curr)
            curr = curr.next

        list_len = len(linked_list)
        reverse_segments = list_len // k

        first_idx = 0
        curr_idx = 1
        for _ in range(reverse_segments):
            for _ in range(k - 1):
                linked_list[curr_idx].next = linked_list[curr_idx - 1]
                curr_idx += 1

            nextSegment_reversedHead_idx = first_idx + k * 2 - 1
            if nextSegment_reversedHead_idx < list_len:
                linked_list[first_idx].next = linked_list[nextSegment_reversedHead_idx]
            else:
                linked_list[first_idx].next = linked_list[curr_idx] if curr_idx < list_len else None

            first_idx = curr_idx
            curr_idx += 1

        return linked_list[k - 1]
