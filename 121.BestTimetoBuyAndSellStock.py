class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        low = prices[0]
        high = 0
        best = 0
        for price in prices:
            if price < low:
                low = price
                high = 0
            if price > high:
                high = price
                profit = high - low
                best = max(best, profit)

        if (best) < 0:
            return 0
        else:
            return best

    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        maximum = 0
        profit_sum = 0
        for idx in range(len(prices) - 1, 0, -1):
            profit = prices[idx] - prices[idx - 1]
            profit_sum += profit
            if profit >= 0:
                maximum = max(maximum, profit_sum)
            else:
                profit_sum = max(profit_sum, 0)

        return maximum


if __name__ == "__main__":
    obj = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(obj.maxProfit(prices))  # 5

    prices = [7, 6, 4, 3, 1]
    print(obj.maxProfit(prices))  # 0
