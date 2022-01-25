class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        si, pi, match_i, star_i = 0, 0, 0, -1
        while si < len(s):
            # advance both pointers
            if pi < pn and (p[pi] == "?" or s[si] == p[pi]):
                si += 1
                pi += 1

            # found a wildcard, advance pattern pointer
            elif pi < pn and p[pi] == "*":
                star_i = pi
                match_i = si
                pi += 1

            # last pattern pointer was *, advance string pointer
            elif star_i != -1:
                pi = star_i + 1
                match_i += 1
                si = match_i

            # current pattern pointer is not star, last pattern pointer was not *
            else:
                return False

        # check for remaining characters in pattern
        while pi < pn and p[pi] == "*":
            pi += 1

        return pi == pn

    def isMatch_1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)

        candidate_list = [(0, 0)]
        current_result = []
        for p_idx in range(p_len):
            if p[p_idx] == "*":
                if len(candidate_list):
                    candidate = candidate_list[0]
                else:
                    return False

                candidate_list = []
                for s_idx in range(candidate[1], s_len + 1):
                    candidate_list.append((p_idx + 1, s_idx))  # (0, 0) is the position for initialization

            elif p[p_idx] == "?":
                for candidate in candidate_list:
                    current_result.append((p_idx + 1, candidate[1] + 1))

                candidate_list = current_result
                current_result = []

            else:
                for candidate in candidate_list:
                    if candidate[1] < s_len and p[p_idx] == s[candidate[1]]:
                        current_result.append((p_idx + 1, candidate[1] + 1))

                candidate_list = current_result
                current_result = []

        return True if (p_len, s_len) in candidate_list else False


if __name__ == "__main__":
    obj = Solution()

    # s = "aa"
    # p = "a"
    # print(obj.isMatch(s, p))  # False

    # s = "aa"
    # p = "*"
    # print(obj.isMatch(s, p))  # True

    # s = "cb"
    # p = "?a"
    # print(obj.isMatch(s, p))  # False

    s = "aab"
    p = "c*a*b"
    print(obj.isMatch(s, p))  # False
