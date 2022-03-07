class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, 2 * n + 1):
            ans = ans * i

            # We only need to divide the result by 2 n-times.
            # To prevent decimal results we divide after multiplying an even number.
            if not i % 2:
                ans = ans // 2
            ans %= MOD

        return ans

    def countOrders_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, n + 1):
            # Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i
            # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1)
            ans %= MOD

        return ans


if __name__ == "__main__":
    obj = Solution()

    n = 1
    print(obj.countOrders(n))  # 1

    n = 2
    print(obj.countOrders(n))  # 6

    n = 3
    print(obj.countOrders(n))  # 9
