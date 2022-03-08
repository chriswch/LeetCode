from collections import Counter
from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common()[-1][0]


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 2, 1]
    print(obj.singleNumber(nums))  # 1

    nums = [4, 1, 2, 1, 2]
    print(obj.singleNumber(nums))  # 4

    nums = [1]
    print(obj.singleNumber(nums))  # 1
