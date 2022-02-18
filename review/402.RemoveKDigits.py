class Solution(object):
    def removeKdigits(self, num: str, k: int):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n_stack = []

        for n in num:
            while k and n_stack and n_stack[-1] > n:
                n_stack.pop()
                k -= 1

            n_stack.append(n)

        result = n_stack[:-k] if k else n_stack
        return "".join(result).lstrip("0") or "0"

    def removeKdigits_1(self, num: str, k: int):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        while k:
            if k >= len(num):
                return "0"

            elif "0" in num and num.index("0") <= k:
                k -= num.index("0")
                num = num[num.index("0") + 1 :]

                if num:
                    num = str(int(num))

            else:
                n_len = len(num)
                for i in range(len(num) - 1):
                    if num[i] > num[i + 1]:
                        num = num[:i] + num[i + 1 :]
                        break

                if n_len == len(num):
                    num = num[:-1]

                k -= 1

        return num if num else "0"


if __name__ == "__main__":
    obj = Solution()

    num = "1432219"
    k = 3
    print(obj.removeKdigits(num, k))  # "1219"

    num = "10200"
    k = 1
    print(obj.removeKdigits(num, k))  # "200"

    num = "10"
    k = 2
    print(obj.removeKdigits(num, k))  # "0"

    num = "10"
    k = 1
    print(obj.removeKdigits(num, k))  # "0"

    num = "112"
    k = 1
    print(obj.removeKdigits(num, k))  # "11"

    num = "10001"
    k = 1
    print(obj.removeKdigits(num, k))  # "1"
