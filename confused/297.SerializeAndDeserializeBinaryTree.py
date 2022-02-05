from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
class MyTreeNode(TreeNode):
    def __init__(self, x, parent=None, isLeft=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = parent
        self.isLeft = isLeft


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        que = deque()
        encode = str(root.val)
        if root.left:
            que.append(root.left)
        else:
            que.append(None)
        if root.right:
            que.append(root.right)
        else:
            que.append(None)
        while que:
            cur = que.popleft()
            if cur:
                encode += "," + str(cur.val)
                if cur.left:
                    que.append(cur.left)
                else:
                    que.append(None)
                if cur.right:
                    que.append(cur.right)
                else:
                    que.append(None)
            else:
                encode += ",null"
        return encode

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        else:
            que = deque()
            data = data.split()  # wtf is it not data.split(",")
            r = TreeNode(data[0])
            que.append((0, r))
            while que:
                (i, cur) = que.popleft()
                if i < len(data) - 2 and data[i + 1] != "null":
                    cur.left = TreeNode(data[i + 1])
                    que.append((i + 1, cur.left))
                if i < len(data) - 1 and data[i + 2] != "null":
                    cur.right = TreeNode(data[i + 2])
                    que.append((i + 2, cur.right))
                i += 3
            return r

    def serialize_1(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = ""
        nodes_queue = [root]
        while nodes_queue:
            node = nodes_queue.pop(0)

            if node:
                result += str(node.val) + ","

                nodes_queue.append(node.left)
                nodes_queue.append(node.right)
            else:
                result += "#,"

        return result

    def deserialize_1(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        root = MyTreeNode(-1)
        nodes_queue = [root]
        for val in data.split(",")[:-1]:
            node = nodes_queue.pop(0)

            if val != "#":
                node.val = int(val)
                node.left = MyTreeNode(-1, node, True)
                node.right = MyTreeNode(-1, node, False)
                nodes_queue.extend([node.left, node.right])
            else:
                if node.isLeft:
                    node.parent.left = None
                else:
                    node.parent.right = None

        while nodes_queue:
            node = nodes_queue.pop(0)
            if node.isLeft:
                node.parent.left = None
            else:
                node.parent.right = None

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
