class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0]) + 1

        max_width = 0
        prev_width = [0] * col
        for r_idx in range(row):
            curr_width = [0] * col

            for c_idx, val in enumerate(matrix[r_idx], start=1):
                if val == "1":
                    tmp = min(prev_width[c_idx], min(prev_width[c_idx - 1], curr_width[c_idx - 1]))
                    curr_width[c_idx] = 1 + tmp

                    max_width = max(max_width, curr_width[c_idx])

            prev_width = curr_width

        return max_width ** 2


if __name__ == "__main__":
    obj = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(obj.maximalSquare(matrix))  # 4

    matrix = [["0", "1"], ["1", "0"]]
    print(obj.maximalSquare(matrix))  # 1

    matrix = [["0"]]
    print(obj.maximalSquare(matrix))  # 0

    matrix = [
        ["0", "0", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"],
    ]
    print(obj.maximalSquare(matrix))  # 9
