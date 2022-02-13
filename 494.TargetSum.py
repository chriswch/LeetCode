class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sums = sum(nums)

        if (target + sums) % 2 or abs(target) > sums:
            return 0

        target = (target + sums) / 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for a in nums:
            for i in range(target, a - 1, -1):
                dp[i] += dp[i - a]
        return dp[target]

    def findTargetSumWays_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum_dict = {0: 1}
        for n in nums:
            next_dict = {}

            for curr_sum in sum_dict:
                for opd in [n, -n]:
                    add_n = curr_sum + opd

                    if add_n in next_dict:
                        next_dict[add_n] += sum_dict[curr_sum]
                    else:
                        next_dict[add_n] = sum_dict[curr_sum]

            sum_dict = next_dict

        return sum_dict[target] if target in sum_dict else 0


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 1, 1, 1]
    target = 3
    print(obj.findTargetSumWays(nums, target))  # 5

    nums = [1]
    target = 1
    print(obj.findTargetSumWays(nums, target))  # 1
