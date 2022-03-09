# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0

        curr_level = [(1, root)]
        while curr_level:
            result = max(result, curr_level[-1][0] - curr_level[0][0] + 1)
            curr_level = [
                child
                for idx, node in curr_level
                for child in enumerate((node.left, node.right), 2 * idx)
                if child[1]
            ]

        return result
