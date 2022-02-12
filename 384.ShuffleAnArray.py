import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        nums = self.nums[:]
        random.shuffle(nums)
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution()
    print(obj.shuffle())
    print(obj.reset())  # [1, 2, 3]
    print(obj.shuffle())
