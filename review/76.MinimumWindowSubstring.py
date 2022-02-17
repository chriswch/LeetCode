from collections import Counter
import string


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        alphabets = string.ascii_lowercase + string.ascii_uppercase
        t_dict = {}
        for char in alphabets:
            t_dict[char] = 0

        for t_char in t:
            t_dict[t_char] += 1
        t_cnt = len(t)

        minimum = float("inf")
        j = 0
        for s_idx, s_char in enumerate(s):
            if t_dict[s_char] > 0:
                t_cnt -= 1
            t_dict[s_char] -= 1

            if t_cnt == 0:
                while t_cnt == 0:
                    t_dict[s[j]] += 1
                    if t_dict[s[j]] > 0:
                        t_cnt += 1
                    j += 1

                window_len = s_idx - (j - 1) + 1
                if window_len < minimum:
                    minimum = window_len
                    from_idx = j - 1

        return s[from_idx : from_idx + minimum] if minimum != float("inf") else ""

    def minWindow_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = Counter(t)
        t_cnt = len(list(t_dict.elements()))

        minimum = float("inf")
        j = 0
        for s_idx, s_char in enumerate(s):
            if t_dict[s_char] > 0:
                t_cnt -= 1
            t_dict[s_char] -= 1

            if t_cnt == 0:
                while t_cnt == 0:
                    t_dict[s[j]] += 1
                    if t_dict[s[j]] > 0:
                        t_cnt += 1
                    j += 1

                window_len = s_idx - (j - 1) + 1
                if window_len < minimum:
                    minimum = window_len
                    from_idx = j - 1

        return s[from_idx : from_idx + minimum] if minimum != float("inf") else ""


if __name__ == "__main__":
    obj = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    print(obj.minWindow(s, t))  # "BANC"

    s = "a"
    t = "a"
    print(obj.minWindow(s, t))  # "a"

    s = "a"
    t = "aa"
    print(obj.minWindow(s, t))  # ""
