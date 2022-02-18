class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1

                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1

            # If the current bit is more frequently set in nums than it is in
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask

        return duplicate

    def findDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        low = 1
        high = nums_len - 1

        while low <= high:
            curr = (low + high) // 2

            cnt = sum([n <= curr for n in nums])
            if cnt > curr:
                result = curr
                high = curr - 1
            else:
                low = curr + 1

        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 3, 4, 2, 2]
    print(obj.findDuplicate(nums))  # 2

    nums = [3, 1, 3, 4, 2]
    print(obj.findDuplicate(nums))  # 3

    nums = [2, 2, 2, 2, 2]
    print(obj.findDuplicate(nums))  # 2

    nums = [1, 1]
    print(obj.findDuplicate(nums))  # 1

    nums = [1, 2, 2]
    print(obj.findDuplicate(nums))  # 2
