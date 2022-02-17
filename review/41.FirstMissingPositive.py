class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = filter(lambda n: n > 0, nums)
        nums = list(set(nums))
        if nums == []:
            return 1

        n_max = max(nums)
        n_min = min(nums)
        cont_sum = (n_max + n_min) * (n_max - n_min + 1) // 2
        list_sum = sum(nums)
        if cont_sum == list_sum:
            return n_max + 1 if n_min == 1 else 1

        nums_len = len(nums)
        for idx, n in enumerate(nums, start=1):
            tmp = n
            while tmp - 1 < len(nums) and tmp != nums[tmp - 1]:
                nums[tmp - 1], nums[idx - 1] = tmp, nums[tmp - 1]
                tmp = nums[idx - 1]

        for idx, n in enumerate(nums, start=1):
            if n != idx:
                return idx

        return nums_len + 1

    def firstMissingPositive_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = filter(lambda n: n > 0, nums)
        nums = list(set(nums))
        if nums == []:
            return 1

        n_max = max(nums)
        n_min = min(nums)

        cont_sum = (n_max + n_min) * (n_max - n_min + 1) // 2
        list_sum = sum(nums)
        if cont_sum == list_sum:
            return n_max + 1 if n_min == 1 else 1

        nums.sort()
        minimum = 1
        for n in nums:
            if n != minimum:
                break
            minimum += 1

        return minimum

    def firstMissingPositive_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = filter(lambda n: n > 0, nums)
        if nums == []:
            return 1

        nums = set(nums)

        n_max = max(nums)
        n_min = min(nums)

        cont_sum = (n_max + n_min) * (n_max - n_min + 1) // 2
        list_sum = sum(nums)
        if cont_sum == list_sum:
            return n_max + 1 if n_min == 1 else 1

        diff = cont_sum - list_sum
        minimum = 1
        while minimum <= diff:
            if minimum not in nums:
                return minimum
            minimum += 1

        return diff


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 0]
    print(obj.firstMissingPositive(nums))  # 3

    nums = [3, 4, -1, 1]
    print(obj.firstMissingPositive(nums))  # 2

    nums = [7, 8, 9, 11, 12]
    print(obj.firstMissingPositive(nums))  # 1

    # print(obj.firstMissingPositive(range(1, 2147483647)))  # 1
