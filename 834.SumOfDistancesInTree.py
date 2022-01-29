class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.n = n

        tree_node = {i: [] for i in range(n)}
        for a, b in edges:
            tree_node[a].append(b)
            tree_node[b].append(a)

        nodes_cnt = {}  # root to number of nodes in this sub-tree
        sub_dist = [0] * n  # root to distance from root to nodes in this sub-tree

        def dfs(curr, parent):
            nodes_cnt[curr] = 1
            for child in tree_node[curr]:
                if child != parent:
                    dfs(child, curr)
                    nodes_cnt[curr] += nodes_cnt[child]
                    sub_dist[curr] += sub_dist[child] + nodes_cnt[child]

        def dp(curr, parent):
            for child in tree_node[curr]:
                if child != parent:
                    sub_dist[child] = sub_dist[curr] - nodes_cnt[child] + (self.n - nodes_cnt[child])
                    dp(child, curr)

        dfs(0, -1)
        dp(0, -1)

        return sub_dist


if __name__ == "__main__":
    obj = Solution()

    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(obj.sumOfDistancesInTree(n, edges))  # [8,12,6,10,10,10]

    n = 1
    edges = []
    print(obj.sumOfDistancesInTree(n, edges))  # [0]

    n = 2
    edges = [[1, 0]]
    print(obj.sumOfDistancesInTree(n, edges))  # [1,1]
