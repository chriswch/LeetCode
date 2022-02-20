import heapq


class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pq = []
        for a in nums:
            heapq.heappush(pq, [a / (a & -a), a])

        res = float("inf")
        ma = max(a for a, a0 in pq)

        while len(pq) == len(nums):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])

        return res

    def minimumDeviation_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pq = []
        for a in nums:
            heapq.heappush(pq, -a * 2 if a % 2 else -a)

        res = float("inf")
        mi = -max(pq)

        while len(pq) == len(nums):
            a = -heapq.heappop(pq)
            res = min(res, a - mi)
            if a % 2 == 0:
                mi = min(mi, a / 2)
                heapq.heappush(pq, -a / 2)

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4]
    print(obj.minimumDeviation(nums))  # 1

    nums = [4, 1, 5, 20, 3]
    print(obj.minimumDeviation(nums))  # 3

    nums = [2, 10, 8]
    print(obj.minimumDeviation(nums))  # 3
