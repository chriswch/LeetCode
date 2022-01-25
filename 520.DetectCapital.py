class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return len(word) == 1 or word.isupper() or word[1:].islower()

    def detectCapitalUse_3(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word.isupper()) or (word.islower()) or (word[0].isupper() and word[1:].islower())

    def detectCapitalUse_2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        elif word[0].islower() and word[1].isupper():
            return False
        else:
            for i in range(1, len(word) - 1):
                if word[i].islower() and word[i + 1].isupper():
                    return False
                elif word[i].isupper() and word[i + 1].islower():
                    return False

        return True

    def detectCapitalUse_1(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upper_cnt = 0
        for char in word:
            if char.isupper():
                upper_cnt += 1

        if upper_cnt == 0:
            return True
        elif upper_cnt == 1:
            return True if word[0].isupper() else False
        else:
            return True if upper_cnt == len(word) else False

    def detectCapitalUse_myself_2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capital = True if word[0].isupper() else False
        if len(word) > 1 and word[1].isupper():
            if capital:
                upper = True
            else:
                return False
        else:
            upper = False

        for char in word[2:]:
            if char.isupper() and not upper:
                return False
            elif char.islower() and upper:
                return False

        return True

    def detectCapitalUse_myself_1(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word_capital = word.capitalize()
        word_upper = word.upper()
        word_lower = word.lower()

        if word != word_capital and word != word_upper and word != word_lower:
            return "false"
        else:
            return "true"


if __name__ == "__main__":
    obj = Solution()

    word = "USA"
    print(obj.detectCapitalUse(word))

    word = "FlaG"
    print(obj.detectCapitalUse(word))
