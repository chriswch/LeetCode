class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1

            if j == i:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i]) + "->" + str(nums[j]))

            i = j + 1
        return ans

    def summaryRanges_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = [[nums[0]]]
        for n in nums[1:]:
            if n == (result[-1][-1] + 1):
                result[-1].append(n)
            else:
                if result[-1][0] == result[-1][-1]:
                    result[-1] = f"{result[-1][0]}"
                else:
                    result[-1] = f"{result[-1][0]}->{result[-1][-1]}"

                result.append([n])

        if result[-1][0] == result[-1][-1]:
            result[-1] = f"{result[-1][0]}"
        else:
            result[-1] = f"{result[-1][0]}->{result[-1][-1]}"
        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [0, 1, 2, 4, 5, 7]
    print(obj.summaryRanges(nums))  # ["0->2","4->5","7"]

    nums = [0, 2, 3, 4, 6, 8, 9]
    print(obj.summaryRanges(nums))  # ["0","2->4","6","8->9"]
