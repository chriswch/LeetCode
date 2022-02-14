class Solution(object):
    def decodeString(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.s_len = len(s)

        self.s_stack = []

        seg, _ = self.recursive(0)

        return seg

    def recursive(self, s_idx):
        k = ""
        seg = ""

        while s_idx < self.s_len:
            if self.s[s_idx].isdigit():
                k += self.s[s_idx]
                s_idx += 1

            elif self.s[s_idx] == "[":
                sub_seg, s_idx = self.recursive(s_idx + 1)
                seg = seg + sub_seg * int(k)

                k = ""

            elif self.s[s_idx] == "]":
                return seg, s_idx + 1

            else:
                seg += self.s[s_idx]
                s_idx += 1

        return seg, s_idx

    def decodeString_stack(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        s_stack = []
        k = ""
        seg = ""

        for char in s:
            if char.isdigit():
                k += char

            elif char == "[":
                s_stack.append([seg, k])

                k = ""
                seg = ""

            elif char == "]":
                last_seg, k = s_stack.pop()
                seg = last_seg + seg * int(k)

                k = ""
            else:
                seg += char

        return seg


if __name__ == "__main__":
    obj = Solution()

    s = "3[a]2[bc]"
    print(obj.decodeString(s))  # aaabcbc

    s = "3[a2[c]]"
    print(obj.decodeString(s))  # accaccacc

    s = "2[abc]3[cd]ef"
    print(obj.decodeString(s))  # abcabccdcdcdef
