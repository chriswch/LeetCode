class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        longest_table = [[None] * n for _ in range(m)]

        def DFS(i, j):
            dist_list = []
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    if longest_table[x][y] == None:
                        DFS(x, y)
                        dist_list.append(longest_table[x][y] + 1)
                    else:
                        dist_list.append(longest_table[x][y] + 1)

            if dist_list:
                longest_table[i][j] = max(dist_list)
            else:
                longest_table[i][j] = 1

        longest = 0
        for i in range(m):
            for j in range(n):
                if longest_table[i][j] == None:
                    DFS(i, j)

                if longest_table[i][j] > longest:
                    longest = longest_table[i][j]
        return longest


if __name__ == "__main__":
    obj = Solution()

    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(obj.longestIncreasingPath(matrix))  # 4

    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print(obj.longestIncreasingPath(matrix))  # 4

    matrix = [[1]]
    print(obj.longestIncreasingPath(matrix))  # 1
