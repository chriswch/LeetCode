import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def query(bitTree, index):
            # index += 1
            result = 0

            while index > 0:
                result += bitTree[index]
                index -= index & (-index)
            return result

        def update(bitTree, value, index, n):
            index += 1

            while index < n:
                bitTree[index] += value
                index += index & (-index)

        n = 2 * 10 ** 4 + 2
        bitTree = [0] * n
        offset = 10 ** 4
        ans = []

        for i in reversed(nums):
            update(bitTree, 1, i + offset, n)
            ans.append(query(bitTree, i + offset))

        return reversed(ans)

    def countSmaller_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.reverse()

        tmp = []
        result = []
        for n in nums:
            result.append(bisect.bisect_left(tmp, n))
            bisect.insort_left(tmp, n)

        result.reverse()
        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [5, 2, 6, 1]
    print(obj.countSmaller(nums))  # [2,1,1,0]

    nums = [-1]
    print(obj.countSmaller(nums))  # [0]

    nums = [-1, -1]
    print(obj.countSmaller(nums))  # [0, 0]
