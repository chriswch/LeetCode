from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n_dict = Counter(nums)

        return [item[0] for item in n_dict.most_common(k)]


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(obj.topKFrequent(nums, k))  # [1,2]

    nums = [1]
    k = 1
    print(obj.topKFrequent(nums, k))  # [1]

    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(obj.topKFrequent(nums, k))  # [-1,2]
