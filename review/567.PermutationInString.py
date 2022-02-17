import string


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False

        s1_dict = {}
        s2_dict = {}
        for c in string.ascii_lowercase:
            s1_dict[c] = 0
            s2_dict[c] = 0
        for s1_idx in range(s1_len):
            s1_dict[s1[s1_idx]] += 1
            s2_dict[s2[s1_idx]] += 1

        if s1_dict == s2_dict:
            return True

        for s2_idx in range(s1_len, s2_len):
            char_right = s2[s2_idx]
            char_left = s2[s2_idx - s1_len]

            s2_dict[char_right] += 1
            s2_dict[char_left] -= 1

            if s1_dict == s2_dict:
                return True

        return False

    def checkInclusion_1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False

        s1_dict = {}
        s2_dict = {}
        for i in range(26):
            s1_dict[i] = 0
            s2_dict[i] = 0

        for idx in range(s1_len):
            s1_dict[ord(s1[idx]) - ord("a")] += 1
            s2_dict[ord(s2[idx]) - ord("a")] += 1

        cnt = 0
        for i in range(26):
            if s1_dict[i] == s2_dict[i]:
                cnt += 1

        for i in range(s2_len - s1_len):
            r = ord(s2[i + s1_len]) - ord("a")
            l = ord(s2[i]) - ord("a")

            if cnt == 26:
                return True

            s2_dict[r] += 1
            if s2_dict[r] == s1_dict[r]:
                cnt += 1
            elif s2_dict[r] == s1_dict[r] + 1:
                cnt -= 1

            s2_dict[l] -= 1
            if s2_dict[l] == s1_dict[i]:
                cnt += 1
            elif s2_dict[l] == s1_dict[l] - 1:
                cnt -= 1

        return cnt == 26


if __name__ == "__main__":
    obj = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    print(obj.checkInclusion(s1, s2))  # true

    s1 = "ab"
    s2 = "eidboaoo"
    print(obj.checkInclusion(s1, s2))  # false
