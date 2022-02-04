class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_sum = 0
        sum_dict = {0: -1}

        max_len = 0
        for n_idx, n in enumerate(nums):
            n_sum += 1 if n else -1

            if n_sum in sum_dict:
                max_len = max(max_len, n_idx - sum_dict[n_sum])
            else:
                sum_dict[n_sum] = n_idx

        return max_len


if __name__ == "__main__":
    obj = Solution()

    nums = [0, 1]
    print(obj.findMaxLength(nums))  # 2

    nums = [0, 1, 0]
    print(obj.findMaxLength(nums))  # 2
