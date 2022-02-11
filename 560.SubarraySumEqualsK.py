class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_dict = {0: 1}  # accumulative sum from index 0
        acc_sum = 0  # accumulative sum

        result = 0
        for n in nums:
            acc_sum += n

            diff = acc_sum - k
            if diff in sum_dict:
                result += sum_dict[diff]

            if acc_sum in sum_dict:
                sum_dict[acc_sum] += 1
            else:
                sum_dict[acc_sum] = 1
        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 1]
    k = 2
    print(obj.subarraySum(nums, k))  # 2

    nums = [1, 2, 3]
    k = 3
    print(obj.subarraySum(nums, k))  # 2

    nums = [1]
    k = 0
    print(obj.subarraySum(nums, k))  # 0
