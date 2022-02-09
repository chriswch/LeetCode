class minDistance(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = word1, word2
        opened = set()

        topens = [(w1, w2, 0)]
        while True:
            (w1, w2, value) = topens.pop(0)
            if (w1, w2) in opened:
                continue
            if w1 == w2:
                return value
            opened.add((w1, w2))
            while w1 and w2 and w1[0] == w2[0]:
                w1 = w1[1:]
                w2 = w2[1:]
            value = value + 1
            topens += [(w1[1:], w2, value), (w1, w2[1:], value), (w1[1:], w2[1:], value)]

    def minDistance_1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len = len(word1)
        word2_len = len(word2)

        dp_table = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]
        for r_idx in range(word1_len + 1):
            dp_table[r_idx][0] = r_idx
        for c_idx in range(word2_len + 1):
            dp_table[0][c_idx] = c_idx

        for r_idx in range(1, word1_len + 1):
            for c_idx in range(1, word2_len + 1):
                if word1[r_idx - 1] == word2[c_idx - 1]:
                    dp_table[r_idx][c_idx] = dp_table[r_idx - 1][c_idx - 1]
                else:
                    dp_table[r_idx][c_idx] = 1 + min(
                        dp_table[r_idx - 1][c_idx], dp_table[r_idx][c_idx - 1], dp_table[r_idx - 1][c_idx - 1]
                    )

        return dp_table[-1][-1]


if __name__ == "__main__":
    obj = minDistance()

    word1 = "horse"
    word2 = "ros"
    print(obj.minDistance(word1, word2))  # 3

    word1 = "intention"
    word2 = "execution"
    print(obj.minDistance(word1, word2))  # 5
