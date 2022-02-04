class TrieNode:
    def __init__(self):
        self.chars = {}
        self.end = None
        self.count = 0

    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.chars:
                curr.chars[char] = TrieNode()
                curr.count += 1

            curr.count += 1
            curr = curr.chars[char]

        curr.end = word


class Solution(object):
    def dfs(self, r, c, node):
        self.visit.add((r, c))

        child = node.chars[self.board[r][c]]

        if child.end:
            print(f"Found {child.end} in child of {self.board[r][c]}")
            self.result.append(child.end)
            child.end = None

        for next_r, next_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (
                0 <= next_r < self.row
                and 0 <= next_c < self.col
                and (next_r, next_c) not in self.visit
                and self.board[next_r][next_c] in child.chars
                and child.count
            ):
                print(f"Current:{self.board[r][c]} Visit:{self.board[next_r][next_c]}")
                self.dfs(next_r, next_c, child)

        self.visit.remove((r, c))

        if child.count == 0:
            node.count -= 1

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.row = len(board)
        self.col = len(board[0])
        self.board = board

        root = TrieNode()
        for word in words:
            root.addWord(word)

        self.visit = set()
        self.result = []
        for r in range(self.row):
            for c in range(self.col):
                if self.board[r][c] in root.chars:
                    self.dfs(r, c, root)

        return self.result

    def dfs_1(self, r_idx, c_idx, curr_word, curr_trie):
        char = self.board[r_idx][c_idx]
        curr_word += char

        curr_trie = curr_trie[char]
        if "END" in curr_trie:
            self.self.result.add(curr_word)

        self.board[r_idx][c_idx] = 0
        for next_r, next_c in [(r_idx - 1, c_idx), (r_idx + 1, c_idx), (r_idx, c_idx - 1), (r_idx, c_idx + 1)]:
            if 0 <= next_r < self.row and 0 <= next_c < self.col:
                next_char = self.board[next_r][next_c]
                if next_char and next_char in curr_trie:
                    self.dfs_1(next_r, next_c, curr_word, curr_trie)

        # restore
        self.board[r_idx][c_idx] = char

    def findWords_1(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        self.self.result = set()

        board_char = []
        for board_row in board:
            board_char.extend(board_row)
        board_char = list(set(board_char))

        trie_head = {}
        for word in words:
            node = trie_head

            skip = False
            for char in word:
                if char not in board_char:
                    skip = True
                    break
            if skip:
                continue

            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["END"] = 1

        for r_idx in range(self.row):
            for c_idx in range(self.col):
                if board[r_idx][c_idx] in trie_head:
                    self.dfs_1(r_idx, c_idx, "", trie_head)

        return list(self.self.result)


if __name__ == "__main__":
    obj = Solution()

    # board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    # words = ["oath", "pea", "eat", "rain"]
    # print(obj.findWords(board, words))  # ["eat","oath"]

    # board = [["a", "b"], ["c", "d"]]
    # words = ["abcb"]
    # print(obj.findWords(board, words))  # []

    board = [
        ["a", "a", "a"],
        ["b", "b", "b"],
        ["a", "a", "a"],
        ["b", "a", "b"],
        ["b", "b", "a"],
        ["a", "a", "a"],
        ["a", "a", "b"],
        ["a", "a", "a"],
        ["b", "b", "b"],
    ]
    words = ["bbabb", "baaa"]
    print(obj.findWords(board, words))  # ["baaa","bbabb"]
