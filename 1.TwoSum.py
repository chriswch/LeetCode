class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], idx]

            hash_map[num] = idx

    def twoSum_myself(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted) - 1):
            diff = target - nums_sorted[i]

            if diff in nums_sorted[i + 1 :]:
                diff_sorted_index = nums_sorted.index(diff)

                minuend_idx = nums.index(nums_sorted[i])
                subtrahend_idx = (
                    nums.index(nums_sorted[diff_sorted_index])
                    if diff != nums_sorted[i]
                    else nums.index(nums_sorted[diff_sorted_index], minuend_idx + 1)
                )

                return [minuend_idx, subtrahend_idx]


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(obj.twoSum(nums, target))  # [0,1]

    nums = [3, 2, 4]
    target = 6
    print(obj.twoSum(nums, target))  # [1,2]

    nums = [3, 3]
    target = 6
    print(obj.twoSum(nums, target))  # [0,1]
