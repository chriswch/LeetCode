from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        ascii_a = ord("a")  # 97

        p_dict = [0] * 26  # Only lowercase English letters
        for p_char in p:
            p_dict[ord(p_char) - ascii_a] += 1

        window_dict = [0] * 26
        for s_char in s[:p_len]:
            window_dict[ord(s_char) - ascii_a] += 1

        result = [0] if p_dict == window_dict else []
        for s_idx in range(1, s_len - p_len + 1):
            window_dict[ord(s[s_idx - 1]) - ascii_a] -= 1
            window_dict[ord(s[s_idx + p_len - 1]) - ascii_a] += 1

            if window_dict == p_dict:
                result.append(s_idx)

        return result

    def findAnagrams_dict(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        p_dict = {chr(ascii_c): 0 for ascii_c in range(ord("a"), ord("z") + 1)}
        for p_char in p:
            p_dict[p_char] += 1

        window_dict = {chr(ascii_c): 0 for ascii_c in range(ord("a"), ord("z") + 1)}
        for s_char in s[:p_len]:
            window_dict[s_char] += 1

        result = [0] if p_dict == window_dict else []
        for s_idx in range(1, s_len - p_len + 1):
            window_dict[s[s_idx - 1]] -= 1
            window_dict[s[s_idx + p_len - 1]] += 1

            if window_dict == p_dict:
                result.append(s_idx)

        return result

    def findAnagrams_counter(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        result = []
        p_dict = Counter(p)

        curr_window = Counter(s[:p_len])
        if not (curr_window - p_dict):
            result.append(0)

        for s_idx in range(1, s_len - p_len + 1):
            curr_window[s[s_idx - 1]] -= 1
            curr_window[s[s_idx + p_len - 1]] += 1

            if not (curr_window - p_dict):
                result.append(s_idx)

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "cbaebabacd"
    p = "abc"
    print(obj.findAnagrams(s, p))  # [0,6]

    s = "abab"
    p = "ab"
    print(obj.findAnagrams(s, p))  # [0,1,2]
