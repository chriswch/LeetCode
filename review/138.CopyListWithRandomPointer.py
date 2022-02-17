# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # step 0: edge case
        if not head:
            return None

        # step 1: create shadow nodes
        current_node = head
        while current_node:
            shadow_node = Node(current_node.val)
            temp = current_node.next
            current_node.next = shadow_node
            shadow_node.next = temp
            current_node = temp

        # step 2: copy random pointer
        current_node = head
        shadow_node = head.next
        while current_node and shadow_node:
            if current_node.random:
                shadow_node.random = current_node.random.next
            current_node = shadow_node.next
            if current_node:
                shadow_node = shadow_node.next.next

        # step 3: split
        # current_node = head
        # shadow_node = head.next
        # while current_node and shadow_node:
        #     if shadow_node.next:
        #         next_node = shadow_node.next
        #         current_node.next = next_node
        #         shadow_node.next = next_node.next
        #         current_node = next_node
        #         shadow_node = next_node.next
        #     else:
        #         current_node.next = None
        # return head.next
        newHead = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            if tmp.next:
                tmp.next = tmp.next.next
        return newHead

    def copyRandomList_1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        curr_idx = 0
        origin_list = {}  # Node to index
        new_list = {}  # index to Node
        random_node = {}  # origin node to indices of past nodes

        # Initialization of root node
        origin_list[head] = curr_idx
        new_list[curr_idx] = Node(head.val)
        if random_node != {} and head in random_node:
            for prev_index in random_node[head]:
                new_list[prev_index].random = new_list[curr_idx]
        if head.random:
            if head.random in origin_list:
                idx_random = origin_list[head.random]
                new_list[curr_idx].random = new_list[idx_random]
            else:
                if head.random in random_node:
                    random_node[head.random].append(curr_idx)
                else:
                    random_node[head.random] = [curr_idx]
        curr_idx += 1

        curr = head.next
        while curr:
            origin_list[curr] = curr_idx
            new_list[curr_idx] = Node(curr.val)
            if random_node != {} and curr in random_node:
                for prev_index in random_node[curr]:
                    new_list[prev_index].random = new_list[curr_idx]
            if curr.random:
                if curr.random in origin_list:
                    idx_random = origin_list[curr.random]
                    new_list[curr_idx].random = new_list[idx_random]
                else:
                    if curr.random in random_node:
                        random_node[curr.random].append(curr_idx)
                    else:
                        random_node[curr.random] = [curr_idx]

            new_list[curr_idx - 1].next = new_list[curr_idx]
            curr = curr.next

            curr_idx += 1

        return new_list[0]
