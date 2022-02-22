class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        base = 26
        for char in columnTitle:
            result = result * base + ord(char) - ord("A") + 1

        return result


if __name__ == "__main__":
    obj = Solution()

    columnTitle = "A"
    print(obj.titleToNumber(columnTitle))  # 1

    columnTitle = "AB"
    print(obj.titleToNumber(columnTitle))  # 28

    columnTitle = "ZY"
    print(obj.titleToNumber(columnTitle))  # 701
