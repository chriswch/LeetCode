# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def infix(tree, node):
            if node.left:
                infix(tree, node.left)

            tree.append(node.val)

            if node.right:
                infix(tree, node.right)

        tree = []
        if root1:
            infix(tree, root1)
        if root2:
            infix(tree, root2)

        return sorted(tree)

    def getAllElements_1(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def infix(sorted_tree, node):
            if node.left:
                infix(sorted_tree, node.left)

            sorted_tree.append(node.val)

            if node.right:
                infix(sorted_tree, node.right)

        sorted_tree1 = []
        sorted_tree2 = []
        if root1:
            infix(sorted_tree1, root1)
        if root2:
            infix(sorted_tree2, root2)

        m = len(sorted_tree1)
        n = len(sorted_tree2)
        idx_m = idx_n = 0
        result = []
        while idx_m != m and idx_n != n:
            if sorted_tree1[idx_m] == sorted_tree2[idx_n]:
                result.append(sorted_tree1[idx_m])
                result.append(sorted_tree2[idx_n])

                idx_m += 1
                idx_n += 1
            elif sorted_tree1[idx_m] < sorted_tree2[idx_n]:
                result.append(sorted_tree1[idx_m])
                idx_m += 1
            else:
                result.append(sorted_tree2[idx_n])
                idx_n += 1

        if idx_m == m:
            while idx_n != n:
                result.append(sorted_tree2[idx_n])
                idx_n += 1
        elif idx_n == n:
            while idx_m != m:
                result.append(sorted_tree1[idx_m])
                idx_m += 1

        return result

