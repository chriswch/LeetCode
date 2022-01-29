class charNode:
    def __init__(self):
        self.chars = {}  # char to charNode of next char
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.rootChar = charNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        next = self.rootChar

        for char in word:
            curr = next
            if char in curr.chars:
                next = curr.chars[char]
            else:
                curr.chars[char] = charNode()
                next = curr.chars[char]
        if word:
            curr.isWord = True

    def search(self, word, root=None):
        """
        :type word: str
        :rtype: bool
        """
        if not root:
            root = self.rootChar

        next = root
        for idx, char in enumerate(word):
            curr = next

            if char in curr.chars:
                next = curr.chars[char]
            elif char == ".":
                if idx == len(word) - 1:
                    return True if curr.isWord else False

                for next in curr.chars:
                    if self.search(word[idx + 1 :], curr.chars[next]):
                        return True
                return False
            else:
                return False

        return True if curr.isWord else False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == "__main__":
    obj = WordDictionary()

    obj.addWord("a")
    obj.addWord("ba")
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")

    print(obj.search("a."))
    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
    print(obj.search("b.."))
