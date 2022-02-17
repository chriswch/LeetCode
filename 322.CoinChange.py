class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # BFS
        res = -1
        queue = [(amount, 0)]
        while queue:
            curr_amount, curr_count = queue.pop(0)

            if curr_amount == 0:
                res = curr_count if res == -1 else min(res, curr_count)
            else:
                for c in coins[::-1]:
                    if c <= curr_amount:
                        if res < 0:
                            queue.append([curr_amount - c, curr_count + 1])
                        elif res > curr_count + 1:
                            queue.append([curr_amount - c, curr_count + 1])
                    else:
                        break

        return res

    def coinChange_dp(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP
        c_dp = [float("inf")] * (amount + 1)
        c_dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    c_dp[i] = min(c_dp[i], c_dp[i - c] + 1)

        return -1 if c_dp[amount] == float("inf") else c_dp[amount]

    def coinChange_dfs(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        self.coins = coins

        self.c_dp = [None] * (amount + 1)
        self.c_dp[0] = 0

        self.dfs(amount)

        return self.c_dp[amount]

    def dfs(self, amount):
        candidates = []
        for c in self.coins:
            diff = amount - c

            if diff >= 0:
                # Don't use 'if not self.c_dp[diff]',
                # self.c_dp[diff] may be 0
                if self.c_dp[diff] == None:
                    self.dfs(diff)

                if self.c_dp[diff] != -1:
                    candidates.append(self.c_dp[diff])

        self.c_dp[amount] = min(candidates) + 1 if candidates else -1


if __name__ == "__main__":
    obj = Solution()

    coins = [1, 2, 5]
    amount = 11
    print(obj.coinChange(coins, amount))  # 3

    coins = [2]
    amount = 3
    print(obj.coinChange(coins, amount))  # -1

    coins = [1]
    amount = 0
    print(obj.coinChange(coins, amount))  # 0
