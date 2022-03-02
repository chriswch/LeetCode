class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for char in t:
            if idx < len(s) and char == s[idx]:
                idx += 1

        return idx == len(s)

    def isSubsequence_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = 0
        for char in s:
            idx = t.find(char)
            if idx == -1:
                break

            t = t[idx + 1 :]
            cnt += 1
            if not t:
                break

        return True if cnt == len(s) else False


if __name__ == "__main__":
    obj = Solution()

    s = "abc"
    t = "ahbgdc"
    print(obj.isSubsequence(s, t))  # true

    s = "axc"
    t = "ahbgdc"
    print(obj.isSubsequence(s, t))  # false
