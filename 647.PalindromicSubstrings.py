class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        l, r = 0, -1
        d1 = [0] * n
        for i in range(n):
            if i >= r:
                k = 1
            else:
                k = min(r - i + 1, d1[l + r - i])
            while 0 <= i - k and n > i + k and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                r = i + k
                l = i - k

        l, r = 0, -1
        d2 = [0] * n
        for i in range(n):
            if i > r:
                k = 0
            else:
                k = min(r - i + 1, d2[l + r - i + 1])
            while 0 <= i - k - 1 and n > i + k and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            k -= 1
            if i + k > r:
                r = i + k
                l = i - k - 1

        return sum(d1) + sum(d2)

    def countSubstrings_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.s_len = len(s)

        result = 0
        for s_idx in range(self.s_len):
            result += self.aroundCenter(s_idx, s_idx)
            result += self.aroundCenter(s_idx, s_idx + 1)

        return result

    def aroundCenter(self, left_idx, right_idx):
        cnt = 0
        while left_idx >= 0 and right_idx < self.s_len and self.s[left_idx] == self.s[right_idx]:
            cnt += 1

            left_idx -= 1
            right_idx += 1

        return cnt


if __name__ == "__main__":
    obj = Solution()

    s = "abc"
    print(obj.countSubstrings(s))  # 3

    s = "aaa"
    print(obj.countSubstrings(s))  # 6
