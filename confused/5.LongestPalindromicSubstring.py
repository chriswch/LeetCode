class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or s == s[::-1]:
            return s
        else:
            maxlen = 1
            start = 0
            for i in range(1, len(s)):
                plustwo = s[i - maxlen - 1 : i + 1]
                plustone = s[i - maxlen : i + 1]
                if i - maxlen - 1 >= 0 and plustwo == plustwo[::-1]:
                    start = i - maxlen - 1
                    maxlen = maxlen + 2
                    continue
                if plustone == plustone[::-1]:
                    start = i - maxlen
                    maxlen = maxlen + 1
            return s[start : start + maxlen]

    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.s_len = len(s)

        maximum = 0
        for s_idx in range(self.s_len):
            for c_len in [0, 1]:
                sub_left, sub_right = self.expandCenter(s_idx, s_idx + c_len)
                sub_len = sub_right - sub_left - 1
                if sub_len > maximum:
                    maximum = sub_len
                    left_idx, right_idx = sub_left + 1, sub_right

        return s[left_idx:right_idx]

    def expandCenter(self, left_idx, right_idx):
        while left_idx >= 0 and right_idx < self.s_len and self.s[left_idx] == self.s[right_idx]:
            left_idx -= 1
            right_idx += 1

        return left_idx, right_idx


if __name__ == "__main__":
    obj = Solution()

    s = "babad"
    print(obj.longestPalindrome(s))  # "bab"

    s = "cbbd"
    print(obj.longestPalindrome(s))  # "bb"

    s = "a"
    print(obj.longestPalindrome(s))  # "a"
