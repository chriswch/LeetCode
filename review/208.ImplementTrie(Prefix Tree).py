class Trie(object):
    def __init__(self):
        self.chars = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for char in word:
            if char not in node.chars:
                node.chars[char] = Trie()
            node = node.chars[char]
        node.chars["END"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self
        for char in word:
            if char in node.chars:
                node = node.chars[char]
            else:
                return False

        return "END" in node.chars

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self
        for char in prefix:
            if char in node.chars:
                node = node.chars[char]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    obj = Trie()

    obj.insert("apple")
    print(obj.search("apple"))  # true
    print(obj.search("app"))  # false
    print(obj.startsWith("app"))  # true
    obj.insert("app")
    print(obj.search("app"))  # true
