from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque_idx = deque()
        for n_idx, n in enumerate(nums[:k]):
            while deque_idx and n >= nums[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(n_idx)

        result = []
        for n_idx, n in enumerate(nums[k:], start=k):
            result.append(nums[deque_idx[0]])

            if n_idx - k == deque_idx[0]:
                deque_idx.popleft()

            while deque_idx and n >= nums[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(n_idx)

        result.append(nums[deque_idx[0]])
        return result

    def maxSlidingWindow_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque_idx = deque()
        result = []

        for n_idx, n in enumerate(nums[: k - 1]):
            while deque_idx and n >= nums[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(n_idx)

        for n_idx, n in enumerate(nums[k - 1 :], start=k - 1):
            while deque_idx and n >= nums[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(n_idx)

            result.append(nums[deque_idx[0]])

            if n_idx - k + 1 == deque_idx[0]:
                deque_idx.popleft()

        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(obj.maxSlidingWindow(nums, k))  # [3,3,5,5,6,7]

    nums = [1]
    k = 1
    print(obj.maxSlidingWindow(nums, k))  # [1]
