from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(sub_str, k) for sub_str in s.split(char))
        return len(s)

    def longestSubstring_1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        strings = [s]
        candidates = []

        while strings:
            next_strings = []

            for sub_str in strings:
                s_counter = Counter(sub_str)
                next_subStr = []

                for char in s_counter:
                    if s_counter[char] < k:

                        for seg in sub_str.split(char):
                            if seg:
                                next_subStr.append(seg)

                        # Avoid to append sub_str
                        # which only containing the same letters and the amount is less than k
                        # to candidates
                        sub_str = ""
                        break

                if next_subStr:
                    next_strings.extend(next_subStr)
                else:
                    candidates.append(sub_str)
            strings = next_strings

        result = 0
        for sub_str in candidates:
            result = max(result, len(sub_str))

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "aaabb"
    k = 3
    print(obj.longestSubstring(s, k))  # 3

    s = "ababbc"
    k = 2
    print(obj.longestSubstring(s, k))  # 5
