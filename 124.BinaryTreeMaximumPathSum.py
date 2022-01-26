# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree_max = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def DFS(node):
            node_sum = node.val

            next_sum = []
            for next_node in [node.left, node.right]:
                if next_node:
                    tmp = DFS(next_node)
                    if tmp > 0:
                        next_sum.append(tmp)

            if len(next_sum):
                max_sum = max(next_sum)
                node_max = node_sum + sum(next_sum)

                if node_max > self.tree_max:
                    self.tree_max = node_max
                return node_sum + max_sum

            else:
                if node_sum > self.tree_max:
                    self.tree_max = node_sum
                return node_sum

        DFS(root)

        return self.tree_max

    def maxPathSum_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree_sum = []

        def DFS(node):
            node_sum = node.val

            next_sum = []
            for next_node in [node.left, node.right]:
                if next_node:
                    tmp = DFS(next_node)
                    if tmp > 0:
                        next_sum.append(tmp)

            if len(next_sum):
                max_sum = max(next_sum)
                tree_sum.append(node_sum + sum(next_sum))
                return node_sum + max_sum

            else:
                tree_sum.append(node_sum)
                return node_sum

        DFS(root)

        return max(tree_sum)
