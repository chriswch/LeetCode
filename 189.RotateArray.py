class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums) - k  # faster than -k
        nums[:] = nums[n:] + nums[:n]

        print(nums)

    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        target = nums[-k:]
        del nums[-k:]
        nums[0:0] = target

        print(nums)


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(obj.rotate(nums, k))  # [5,6,7,1,2,3,4]

    nums = [-1, -100, 3, 99]
    k = 2
    print(obj.rotate(nums, k))  # [3,99,-1,-100]
