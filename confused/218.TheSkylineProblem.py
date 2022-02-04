import bisect
import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort()

        ans = [(0, 0)]
        live = [(0, float("inf"))]

        for L, negH, R in events:
            if negH:
                heapq.heappush(live, (negH, R))

            while live[0][1] <= L:
                heapq.heappop(live)

            if -live[0][0] != ans[-1][1]:
                ans += [[L, -live[0][0]]]

        return ans[1:]

    def getSkyline_2(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, 0) for _, R, _ in buildings}))

        res = [[0, 0]]
        heap = [[0, float("inf")]]
        for x, H, R in events:
            while x >= heap[0][1]:
                heapq.heappop(heap)

            if H:
                heapq.heappush(heap, [H, R])

            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])

        return res[1:]

    def getSkyline_1(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[0, 0]]

        pos = []
        for l, r, h in buildings:
            pos.append([l, -h])
            pos.append([r, h])
        pos.sort()

        heap = [0]
        for x, h in pos:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)

            min_h = -heap[0]
            if result[-1][1] != min_h:
                result.append([x, min_h])

        return result[1:]


if __name__ == "__main__":
    obj = Solution()

    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(obj.getSkyline(buildings))  # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    buildings = [[0, 2, 3], [2, 5, 3]]
    print(obj.getSkyline(buildings))  # [[0,3],[5,0]]
