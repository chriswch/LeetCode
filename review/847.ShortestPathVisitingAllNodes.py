class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if len(graph) == 1:
            return 0

        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps

                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))

            steps += 1
            queue = next_queue
        
        return steps


if __name__ == "__main__":
    obj = Solution()

    graph = [[1, 2, 3], [0], [0], [0]]
    print(obj.shortestPathLength(graph))  # 4

    graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(obj.shortestPathLength(graph))  # 4
