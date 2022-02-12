class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        seen = {}  # letter to index
        start = -1
        for c_idx, char in enumerate(s):
            if char in seen and start < seen[char]:
                result = max(result, c_idx - 1 - start)

                start = seen[char]
            seen[char] = c_idx

        result = max(result, len(s) - 1 - start)
        return result

    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        left_idx = 0
        for right_idx in range(len(s)):
            if s[right_idx] in s[left_idx:right_idx]:
                result = max(result, right_idx - left_idx)

                while s[right_idx] in s[left_idx:right_idx]:
                    loc_idx = s[left_idx:right_idx].index(s[right_idx])
                    left_idx += loc_idx + 1

        result = max(result, len(s) - left_idx)
        return result


if __name__ == "__main__":
    obj = Solution()

    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))  # 3

    s = "bbbbb"
    print(obj.lengthOfLongestSubstring(s))  # 1

    s = "pwwkew"
    print(obj.lengthOfLongestSubstring(s))  # 3

    s = "dvdf"
    print(obj.lengthOfLongestSubstring(s))  # 3
