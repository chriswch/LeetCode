# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        prev_n = dummy
        former_n = head
        while former_n:
            latter_n = former_n.next

            if latter_n:
                next_n = latter_n.next

                prev_n.next = latter_n
                latter_n.next = former_n

                prev_n = former_n
                former_n = next_n

                prev_n.next = None
            else:
                prev_n.next = former_n
                break

        return dummy.next


if __name__ == "__main__":
    obj = Solution()

    list1_1 = ListNode(1)

    list1_2 = ListNode(2)
    list1_1.next = list1_2

    list1_3 = ListNode(3)
    list1_2.next = list1_3

    list1_4 = ListNode(4)
    list1_3.next = list1_4

    root = obj.swapPairs(list1_1)
    while root:
        print(root.val, end=" ")
        root = root.next
    print("")  # [2,1,4,3]

    list2_1 = None

    root = obj.swapPairs(list2_1)
    while root:
        print(root.val, end=" ")
        root = root.next
    print("")  #

    list3_1 = ListNode(1)
    list3_1.next = None

    root = obj.swapPairs(list3_1)
    while root:
        print(root.val, end=" ")
        root = root.next
    print("")  # 1
