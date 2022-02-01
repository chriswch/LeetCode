class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0
        for customer in accounts:
            maximum = max(maximum, sum(customer))

        return maximum


if __name__ == "__main__":
    obj = Solution()

    accounts = [[1, 2, 3], [3, 2, 1]]
    print(obj.maximumWealth(accounts))  # 6

    accounts = [[1, 5], [7, 3], [3, 5]]
    print(obj.maximumWealth(accounts))  # 10

    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(obj.maximumWealth(accounts))  # 17
