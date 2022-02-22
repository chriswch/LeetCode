# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
        return None

    def lowestCommonAncestor_1(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.target = [p, q]
        self.paths = []

        self.dfs(root, [])

        result = None
        for a_p, a_q in zip(self.paths[0], self.paths[1]):
            if a_p == a_q:
                result = a_p
            else:
                break

        return result

    def dfs(self, node, path):
        if not self.target or not node:
            return

        path.append(node)

        if node in self.target:
            self.paths.append(path[:])
            self.target.remove(node)

        self.dfs(node.left, path)
        self.dfs(node.right, path)
        path.remove(node)


if __name__ == "__main__":
    obj = Solution()

    node = TreeNode(3)
    root = node

    p = TreeNode(5)
    root.left = p
    q = TreeNode(1)
    root.right = q

    print(obj.lowestCommonAncestor(root, p, q).val)  # 3

