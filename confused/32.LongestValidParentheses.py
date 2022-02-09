class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest

    def longestValidParentheses_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        stack = []
        for s_idx in range(len(s)):
            if s[s_idx] == "(":
                stack.append(s_idx)
            else:
                if stack:
                    p = stack.pop()
                    dp[s_idx + 1] = dp[p] + s_idx - p + 1
        return max(dp)


if __name__ == "__main__":
    obj = Solution()

    s = "(()"
    print(obj.longestValidParentheses(s))  # 2

    s = ")()())"
    print(obj.longestValidParentheses(s))  # 4

    s = ""
    print(obj.longestValidParentheses(s))  # 0

    s = "(()()"
    print(obj.longestValidParentheses(s))  # 4
