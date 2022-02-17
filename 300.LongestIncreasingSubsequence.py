from bisect import bisect_left


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)

    def lengthOfLIS_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_len = len(nums)
        dp = [1] * n_len
        for i in range(n_len):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == "__main__":
    obj = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(obj.lengthOfLIS(nums))  # 4

    nums = [0, 1, 0, 3, 2, 3]
    print(obj.lengthOfLIS(nums))  # 4

    nums = [7, 7, 7, 7, 7, 7, 7]
    print(obj.lengthOfLIS(nums))  # 1
