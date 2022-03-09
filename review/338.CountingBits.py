class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= n:
            res += [i + 1 for i in res]

        return res[: n + 1]

    def countBits_1(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            result.append(self.count1s(i))

        return result

    def count1s(self, n):
        result = 0
        while n:
            result += n % 2
            n >>= 1

        return result


if __name__ == "__main__":
    obj = Solution()

    n = 2
    print(obj.countBits(n))  # [0,1,1]

    n = 5
    print(obj.countBits(n))  # [0,1,1,2,1,2]
