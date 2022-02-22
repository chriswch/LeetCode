from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

    def majorityElement_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_count = Counter(nums)
        return n_count.most_common(1)[0][0]


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 2, 3]
    print(obj.majorityElement(nums))  # 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(obj.majorityElement(nums))  # 2
