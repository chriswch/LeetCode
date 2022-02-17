# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """

        return max(self.dfs(root))

    def dfs(self, node: TreeNode):
        if not node:
            return 0, 0

        left_vals = self.dfs(node.left)
        right_vals = self.dfs(node.right)

        chooseNode = node.val + left_vals[1] + right_vals[1]
        skipNode = max(left_vals) + max(right_vals)
        return chooseNode, skipNode
