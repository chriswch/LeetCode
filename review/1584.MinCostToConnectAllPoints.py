import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # create the heap with one distance as 0,
        # so it is arbitrarily popped first from the heap
        vertices = [(float("inf"), (x, y)) for x, y in points]
        vertices[0] = ((0), tuple(points[0]))
        heapq.heapify(vertices)

        # initalize the total weight of MST to 0
        total_weight = 0
        while vertices:
            # heapify since modifications to heap may have disrupted the heap structure
            heapq.heapify(vertices)

            # get the distance and coordinates of the vertex closest to visited set
            d, (x, y) = heapq.heappop(vertices)

            # add it to the visited set and add its distance to MST
            # visited.add((x,y))
            total_weight += d

            # update distances for vertices now that the visited set includes (x,y)
            for idx, vertex in enumerate(vertices):

                # get the distance and coordinates of adjacent vertex
                dd, (xx, yy) = vertex

                # calculate the distance from adjacent vertex (xx,yy) to the vertex (x,y),
                # (x,y) being the vertex that we just added to visited set
                new_dist = abs(xx - x) + abs(yy - y)

                # if its smaller than the old distnace, update it
                if new_dist < dd:
                    vertices[idx] = (new_dist, (xx, yy))

        # return the total weight of the MST we built
        return total_weight

    def minCostConnectPoints_2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n_points = len(points)
        nodes_idx = set(range(n_points))
        dist = [float("inf")] * n_points  # Distances between current MST to others points

        ### root ###
        dist[0] = 0

        result = 0
        for _ in range(n_points):
            target = -1
            min_dist = float("inf")
            for p_idx in nodes_idx:
                if dist[p_idx] < min_dist:
                    target = p_idx
                    min_dist = dist[p_idx]
            nodes_idx.remove(target)
            result += min_dist

            for other in nodes_idx:
                new_dist = abs(points[target][0] - points[other][0]) + abs(points[target][1] - points[other][1])
                if new_dist < dist[other]:
                    dist[other] = new_dist

        return result

    def minCostConnectPoints_1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n_points = len(points)
        visit = [False] * n_points
        dist = [float("inf")] * n_points  # Distances between current MST to others points
        parent = [None] * n_points

        ### root ###
        dist[0] = 0
        parent[0] = 0

        result = 0
        for _ in range(n_points):
            target = -1
            min_dist = float("inf")
            for p_idx in range(n_points):
                if not visit[p_idx] and dist[p_idx] < min_dist:
                    target = p_idx
                    min_dist = dist[p_idx]

            if target == -1:
                break
            result += min_dist

            visit[target] = True
            for other in range(n_points):
                if not visit[other]:
                    new_dist = abs(points[target][0] - points[other][0]) + abs(points[target][1] - points[other][1])
                    if new_dist < dist[other]:
                        dist[other] = new_dist
                        parent[other] = target

        return result


if __name__ == "__main__":
    obj = Solution()

    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(obj.minCostConnectPoints(points))  # 20

    points = [[3, 12], [-2, 5], [-4, 1]]
    print(obj.minCostConnectPoints(points))  # 18
