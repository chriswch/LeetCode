from itertools import combinations


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for amt in range(len(nums) + 1):
            result.extend([list(subset) for subset in combinations(nums, amt)])

        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3]
    print(obj.subsets(nums))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    # nums = [0]
    # print(obj.subsets(nums))  # [[],[0]]
