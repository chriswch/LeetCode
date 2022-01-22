class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        cnt_list = [0] * nums_len

        if nums_len >= 3:
            idx_second = nums_len - 2
            diff_latter = nums[-1] - nums[-2]

        for i in range(nums_len - 3, -1, -1):
            diff_former = nums[idx_second] - nums[i]

            if diff_former == diff_latter:
                cnt_list[i] += 1

                if cnt_list[idx_second]:
                    cnt_list[i] += cnt_list[idx_second]

            idx_second = i
            diff_latter = diff_former

        return sum(cnt_list)


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4]
    print(obj.numberOfArithmeticSlices(nums))

    nums = [1]
    print(obj.numberOfArithmeticSlices(nums))
