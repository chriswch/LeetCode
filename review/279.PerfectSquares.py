from math import floor, sqrt


class Solution(object):
    def isSquare(self, n):
        temp = int(n ** 0.5)
        return temp * temp == n

    # Based on Lagrange's Four Square theorem,
    # there are only 4 possible results: 1, 2, 3, 4.
    def numSquares(self, n):
        # If n is a perfect square, return 1.
        if self.isSquare(n):
            return 1

        # The result is 4 if and only if n can be written in the form of
        # 4^k*(8*m + 7).
        # Please refer to Legendre's three-square theorem.
        while (n & 3) == 0:  # n%4 == 0
            n >>= 2  # n /= 4

        if (n & 7) == 7:  # n % 8 == 7
            return 4

        # Check whether 2 is the result.
        sqrtN = int(n ** 0.5)
        for i in range(sqrtN + 1):
            if self.isSquare(n - i * i):
                return 2

        return 3

    def numSquares_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n_sqr = [0]
        self.len = 1

        while self.len <= n:
            i = 1
            minimum = float("inf")
            while i ** 2 <= self.len:
                minimum = min(minimum, self.n_sqr[self.len - i ** 2] + 1)
                i += 1

            self.n_sqr.append(minimum)
            self.len += 1

        # print(self.n_sqr)
        return self.n_sqr[n]


if __name__ == "__main__":
    obj = Solution()

    n = 12
    print(obj.numSquares(n))  # 3

    n = 13
    print(obj.numSquares(n))  # 2

    n = 42
    print(obj.numSquares(n))  # 3

    n = 48
    print(obj.numSquares(n))  # 3
