from heapq import heappop, heappush


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap_queue = []
        for n in nums:
            heappush(heap_queue, -n)

        for _ in range(k):
            result = heappop(heap_queue)

        return -result


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(obj.findKthLargest(nums, k))  # 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(obj.findKthLargest(nums, k))  # 4
