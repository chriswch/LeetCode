class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            tmp = num % 9
            return 9 if not tmp else tmp

    def addDigits_1(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        n_len = len(num)
        while n_len > 1:
            n = 0
            for n_idx in range(n_len):
                n += int(num[n_idx])
            num = str(n)
            n_len = len(num)

        return num


if __name__ == "__main__":
    obj = Solution()

    num = 38
    print(obj.addDigits(num))  # 2

    num = 0
    print(obj.addDigits(num))  # 0
