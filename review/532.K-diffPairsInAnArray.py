from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_dict = {}

        result = 0
        if k:
            for n in nums:
                if n not in nums_dict:
                    nums_dict[n] = 1
                    if n - k in nums_dict:
                        result += 1
                    if n + k in nums_dict:
                        result += 1
        else:
            n_counter = Counter(nums)
            for n in n_counter:
                if n_counter[n] > 1:
                    result += 1

        return result

    def findPairs_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n_counter = Counter(nums)

        if k:
            result = set()
            for n in n_counter:
                if n - k in n_counter:
                    result.add((n - k, n))
                if n + k in n_counter:
                    result.add((n, n + k))

            return len(result)

        else:
            result = 0
            for n in n_counter:
                if n_counter[n] > 1:
                    result += 1

            return result


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 1, 4, 1, 5]
    k = 2
    print(obj.findPairs(nums, k))  # 2

    nums = [1, 2, 3, 4, 5]
    k = 1
    print(obj.findPairs(nums, k))  # 4

    nums = [1, 3, 1, 5, 4]
    k = 0
    print(obj.findPairs(nums, k))  # 1
