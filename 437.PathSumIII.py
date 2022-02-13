# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root: TreeNode, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.targetSum = targetSum

        self.ancient_sum = {0: 1}
        self.result = 0

        self.dfs(root, 0)

        return self.result

    def dfs(self, node: TreeNode, curr_sum):
        if not node:
            return

        curr_sum += node.val
        diff = curr_sum - self.targetSum
        if diff in self.ancient_sum:
            self.result += self.ancient_sum[diff]

        if curr_sum in self.ancient_sum:
            self.ancient_sum[curr_sum] += 1
        else:
            self.ancient_sum[curr_sum] = 1

        self.dfs(node.left, curr_sum)
        self.dfs(node.right, curr_sum)

        self.ancient_sum[curr_sum] -= 1

