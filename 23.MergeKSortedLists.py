# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        value_nodes = {}
        for node in lists:
            curr = node
            while curr:
                if curr.val in value_nodes:
                    value_nodes[curr.val].append(curr)
                else:
                    value_nodes[curr.val] = [curr]
                curr = curr.next

        root = ListNode()
        curr = root
        for val in sorted(value_nodes.keys()):
            for node in value_nodes[val]:
                curr.next = node
                curr = curr.next

        return root.next

    def mergeKLists_1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = ListNode()
        curr = root
        while lists:
            minimum_val = float("inf")
            minimum_idx = -1
            remove_list = []
            for idx, node in enumerate(lists):
                if node:
                    if node.val < minimum_val:
                        minimum_val = node.val
                        minimum_idx = idx
                else:
                    remove_list.append(node)

            if minimum_idx != -1:
                curr.next = ListNode(minimum_val)
                curr = curr.next

                lists[minimum_idx] = lists[minimum_idx].next
                for node in remove_list:
                    lists.remove(node)
            else:
                if root.next:
                    return root.next
                else:
                    return None

        return None


if __name__ == "__main__":
    obj = Solution()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

    list1_1 = ListNode(1)

    list1_2 = ListNode(4)
    list1_1.next = list1_2

    list1_3 = ListNode(5)
    list1_2.next = list1_3

    list2_1 = ListNode(1)

    list2_2 = ListNode(3)
    list2_1.next = list2_2

    list2_3 = ListNode(4)
    list2_2.next = list2_3

    list3_1 = ListNode(2)

    list3_2 = ListNode(6)
    list3_1.next = list3_2

    root = obj.mergeKLists([list1_1, list2_1, list3_1])
    while root:
        print(root.val, end=" ")
        root = root.next
    print("")

