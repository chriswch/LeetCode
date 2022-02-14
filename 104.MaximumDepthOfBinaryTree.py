# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.depth = 0
        self.dfs(root, 0)

        return self.depth

    def dfs(self, node, level):
        if not node:
            return

        level += 1
        if level > self.depth:
            self.depth = level

        self.dfs(node.left, level)
        self.dfs(node.right, level)
