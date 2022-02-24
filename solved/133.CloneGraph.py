# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        graph = {1: Node(node.val)}

        queue = [node]
        seen = [node.val]
        while queue:
            curr = queue.pop(0)

            for nbr in curr.neighbors:
                if nbr.val not in graph:
                    graph[nbr.val] = Node(nbr.val)

                graph[curr.val].neighbors.append(graph[nbr.val])

                if nbr.val not in seen:
                    queue.append(nbr)
                    seen.append(nbr.val)

        return graph[1]

    def cloneGraph_1(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.graph = {0: Node(0)}
        self.dfs(0, node)

        if self.graph[0].neighbors:
            self.graph[1].neighbors.remove(self.graph[0])
            return self.graph[1]
        else:
            return None

    def dfs(self, prev_val, curr_node):
        if not curr_node:
            return

        curr_val = curr_node.val
        if curr_val in self.graph:
            if self.graph[curr_val] not in self.graph[prev_val].neighbors:
                self.graph[prev_val].neighbors.append(self.graph[curr_val])
                self.graph[curr_val].neighbors.append(self.graph[prev_val])

        else:
            copy = Node(curr_val)
            self.graph[curr_val] = copy

            self.graph[prev_val].neighbors.append(self.graph[curr_val])
            self.graph[curr_val].neighbors.append(self.graph[prev_val])

            for nbr in curr_node.neighbors:
                self.dfs(curr_val, nbr)
