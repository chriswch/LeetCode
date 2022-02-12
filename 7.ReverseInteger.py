class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_reversed = int(str(abs(x))[::-1])
        if -(2 ** 31) <= x_reversed <= 2 ** 31 - 1:
            return x_reversed if x >= 0 else -x_reversed
        else:
            return 0


if __name__ == "__main__":
    obj = Solution()

    x = 123
    print(obj.reverse(x))  # 321

    x = -123
    print(obj.reverse(x))  # -321

    x = 120
    print(obj.reverse(x))  # 21
