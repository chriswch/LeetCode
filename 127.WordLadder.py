import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        s_len = len(beginWord)
        wordList = set(wordList)

        words_1 = {beginWord}
        words_2 = {endWord}
        cnt = 0
        while words_1:
            cnt += 1
            wordList -= words_1

            tmp = set()
            for str in words_1:
                for idx in range(s_len):
                    for char in string.ascii_lowercase:
                        next_word = str[:idx] + char + str[idx + 1 :]
                        if next_word in words_2:
                            return cnt + 1
                        elif next_word in wordList:
                            tmp.add(next_word)

            words_1 = tmp
            if len(words_1) > len(words_2):
                words_1, words_2 = words_2, words_1

        return 0

    def ladderLength_1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        s_len = len(beginWord)
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 0

        wordList.remove(endWord)

        words_1 = {beginWord}
        words_2 = {endWord}
        cnt = 0
        while words_1 and words_2:
            cnt += 1

            if len(words_1) > len(words_2):
                words_1, words_2 = words_2, words_1

            tmp = set()
            for str in words_1:
                next_words = [
                    str[:idx] + char + str[idx + 1 :] for char in string.ascii_lowercase for idx in range(s_len)
                ]

                for next_word in next_words:
                    if next_word in words_2:
                        return cnt + 1
                    elif next_word in wordList:
                        tmp.add(next_word)
                        wordList.remove(next_word)

            words_1 = tmp

        return 0


if __name__ == "__main__":
    obj = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(obj.ladderLength(beginWord, endWord, wordList))  # 5

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(obj.ladderLength(beginWord, endWord, wordList))  # 0
