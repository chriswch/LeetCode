class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        s_len = len(s)

        s_dict = {0: [""]}
        result = []
        while s_dict:
            curr_dict = {}
            for start_idx in s_dict:
                for word in wordDict:
                    end_idx = start_idx + len(word)
                    if end_idx <= s_len and word == s[start_idx:end_idx]:

                        if end_idx != len(s):
                            if end_idx in curr_dict:
                                curr_dict[end_idx].extend([parent_s + " " + word for parent_s in s_dict[start_idx]])
                            else:
                                curr_dict[end_idx] = [parent_s + " " + word for parent_s in s_dict[start_idx]]
                        else:
                            result.extend([parent_s + " " + word for parent_s in s_dict[start_idx]])

            s_dict = curr_dict

        for idx in range(len(result)):
            result[idx] = result[idx][1:]

        return result

    def wordBreak_1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        s_dict = {0: [""]}
        result = []
        while s_dict:
            curr_dict = {}
            for start_idx in s_dict:
                for end_idx in range(start_idx + 1, len(s) + 1):
                    curr_s = s[start_idx:end_idx]

                    if curr_s in wordDict:
                        if end_idx != len(s):
                            if end_idx in curr_dict:
                                curr_dict[end_idx].extend([parent_s + " " + curr_s for parent_s in s_dict[start_idx]])
                            else:
                                curr_dict[end_idx] = [parent_s + " " + curr_s for parent_s in s_dict[start_idx]]

                        else:
                            result.extend([parent_s + " " + curr_s for parent_s in s_dict[start_idx]])

            s_dict = curr_dict

        for idx in range(len(result)):
            result[idx] = result[idx][1:]

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(obj.wordBreak(s, wordDict))  # ["cats and dog", "cat sand dog"]

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(obj.wordBreak(s, wordDict))  # ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(obj.wordBreak(s, wordDict))  # []
