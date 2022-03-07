from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        nums_key = sorted(nums_counter)

        prev_n = None
        prev_pt = avoid = using = 0
        for k in nums_key:
            if k - 1 != prev_n:
                avoid, using = prev_pt, k * nums_counter[k] + prev_pt
            else:
                avoid, using = prev_pt, k * nums_counter[k] + avoid

            prev_n = k
            prev_pt = max(avoid, using)

        return prev_pt

    def deleteAndEarn_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        nums_key = sorted(list(nums_counter.keys()))

        n = nums_key[0]
        n_cnt = nums_counter[n]
        dp = [0, n * n_cnt]
        for idx in range(1, len(nums_key)):
            n = nums_key[idx]
            n_cnt = nums_counter[n]
            curr_points = n * n_cnt

            if n == (nums_key[idx - 1] + 1):
                dp.append(max(dp[-1], dp[-2] + curr_points))
            else:
                dp.append(dp[-1] + curr_points)

        return dp[-1]


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 4, 2]
    print(obj.deleteAndEarn(nums))  # 6

    nums = nums = [2, 2, 3, 3, 3, 4]
    print(obj.deleteAndEarn(nums))  # 9
