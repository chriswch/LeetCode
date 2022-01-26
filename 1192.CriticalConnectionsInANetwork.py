class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        node_edge = {}
        for pair in connections:
            node_edge[pair[0]].append(pair[1])
            node_edge[pair[1]].append(pair[0])

        dfn = [-1] * n
        low = [-1] * n
        results = []

        def tarjan(node, parent, depth):
            dfn[node] = low[node] = depth

            for adj_node in node_edge[node]:
                if adj_node == parent:
                    continue

                if dfn[adj_node] == -1:
                    tarjan(adj_node, node, depth + 1)

                    if dfn[node] < low[adj_node]:
                        results.append([node, adj_node])

                low[node] = min(low[node], low[adj_node])

        tarjan(0, -1, 0)
        return results


if __name__ == "__main__":
    obj = Solution()

    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(obj.criticalConnections(n, connections))  # [[1,3]]

    n = 2
    connections = [[0, 1]]
    print(obj.criticalConnections(n, connections))  # [[0,1]]
