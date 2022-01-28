class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def wiggleSort_1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sorted_list = sorted(nums)

        idx_sorted = len(sorted_list) - 1
        idx_sorted_mid = (len(sorted_list) - 1) // 2

        idx = 1
        while idx_sorted > idx_sorted_mid:
            nums[idx] = sorted_list[idx_sorted]
            idx += 2
            idx_sorted -= 1
        idx = 0
        while idx_sorted >= 0:
            nums[idx] = sorted_list[idx_sorted]
            idx += 2
            idx_sorted -= 1

        print(nums)


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 5, 1, 1, 6, 4]
    print(obj.wiggleSort(nums))  # [1,6,1,5,1,4]

    nums = [1, 3, 2, 2, 3, 1]
    print(obj.wiggleSort(nums))  # [2,3,1,3,1,2]
