class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        right = {}

        for i, c in enumerate(s):
            right[c] = i
        ans = []

        cl = 0
        last = -1

        # seen = set()
        for i, c in enumerate(s):
            last = max(last, right[c])
            cl += 1

            if i == last:
                ans.append(cl)
                cl = 0

            # print(i,str(c),last)
        return ans

    def partitionLabels_1(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s_len = len(s)
        s_idx = 0

        result = []
        while s_idx < s_len:
            e_idx = s_idx + 1

            sub_str = s[s_idx:e_idx]
            char_set = set(sub_str)
            char_checked = set()
            while char_set:
                char = char_set.pop()
                char_checked.add(char)

                if char in s[-1 : e_idx - 1 : -1]:
                    e_idx = s_len - s[-1 : e_idx - 1 : -1].index(char)

                    sub_str = s[s_idx:e_idx]
                    char_set = set(sub_str) - char_checked

            result.append(e_idx - s_idx)
            s_idx = e_idx

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "ababcbacadefegdehijhklij"
    print(obj.partitionLabels(s))  # [9,7,8]

    s = "eccbbbbdec"
    print(obj.partitionLabels(s))  # [10]
