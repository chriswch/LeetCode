class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_sum = sum([ord(char) for char in s])
        t_sum = sum([ord(char) for char in t])

        return chr(t_sum - s_sum)

    def findTheDifference_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        t_idx = 0
        for s_char in s_sorted:
            if s_char != t_sorted[t_idx]:
                break
            else:
                t_idx += 1

        return t_sorted[t_idx]


if __name__ == "__main__":
    obj = Solution()

    s = "abcd"
    t = "abcde"
    print(obj.findTheDifference(s, t))  # e

    s = ""
    t = "y"
    print(obj.findTheDifference(s, t))  # y
