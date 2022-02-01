class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        possible_idx = [-1]

        p_idx = 0
        while p_idx < p_len:
            target = p[p_idx]
            tmp_idx = []

            if p_idx + 1 < p_len and p[p_idx + 1] == "*":
                p_idx += 1

                if target == ".":
                    possible_idx = list(range(possible_idx[0], s_len))
                else:
                    for prev_idx in possible_idx:
                        tmp_idx.append(prev_idx)

                        cont_idx = prev_idx + 1
                        while cont_idx < s_len and s[cont_idx] == target:
                            tmp_idx.append(cont_idx)
                            cont_idx += 1

                    possible_idx = tmp_idx
            else:
                if target == ".":
                    for prev_idx in possible_idx:
                        if prev_idx + 1 < s_len:
                            tmp_idx.append(prev_idx + 1)

                    possible_idx = tmp_idx
                else:
                    for prev_idx in possible_idx:
                        if prev_idx + 1 < s_len and s[prev_idx + 1] == target:
                            tmp_idx.append(prev_idx + 1)

                    possible_idx = tmp_idx

            print(possible_idx)

            if not possible_idx:
                return False
            else:
                possible_idx = sorted(list(set(possible_idx)))
                p_idx += 1

        return True if (s_len - 1 in possible_idx) else False


if __name__ == "__main__":
    obj = Solution()

    # s = "aa"
    # p = "a"
    # print(obj.isMatch(s, p))  # False

    # s = "aa"
    # p = "a*"
    # print(obj.isMatch(s, p))  # True

    # s = "ab"
    # p = ".*"
    # print(obj.isMatch(s, p))  # True

    # s = "aab"
    # p = "c*a*b"
    # print(obj.isMatch(s, p))  # True

    # s = "aaaaaaaaaaaaab"
    # p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
    # print(obj.isMatch(s, p))  # True

    s = "aasdfasdfasdfasdfas"
    p = "aasdf.*asdf.*asdf.*asdf.*s"
    print(obj.isMatch(s, p))  # True
