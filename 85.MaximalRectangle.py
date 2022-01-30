class Solution(object):
    def maximalRectangle_dp_2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        heights = [0] * col
        leftLessMin = [-1] * col
        rightLessMin = [col] * col
        max_area = 0
        for r in range(row):
            for c in range(col):
                heights[c] = heights[c] + 1 if matrix[r][c] == "1" else 0

            boundary = -1
            for c in range(col):
                if matrix[r][c] == "1":
                    leftLessMin[c] = max(leftLessMin[c], boundary)
                else:
                    leftLessMin[c] = -1
                    boundary = c

            boundary = col
            for c in range(col - 1, -1, -1):
                if matrix[r][c] == "1":
                    rightLessMin[c] = min(rightLessMin[c], boundary)
                else:
                    rightLessMin[c] = col
                    boundary = c
                max_area = max(max_area, heights[c] * (rightLessMin[c] - leftLessMin[c] - 1))

        return max_area

    def maximalRectangle_dp_1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        dp_matrix = [[0] * col for _ in range(row)]
        for r in range(row):
            dp_matrix[r][0] = 1 if matrix[r][0] == "1" else 0

        for r in range(row):
            for c in range(1, col):
                if matrix[r][c] == "1":
                    dp_matrix[r][c] = (dp_matrix[r][c - 1] + 1) if dp_matrix[r][c - 1] else 1
                else:
                    dp_matrix[r][c] = 0

        max_area = 0
        for r in range(row):
            for c in range(col):
                width = float("inf")
                for k in range(r, row):
                    if dp_matrix[k][c]:
                        width = min(width, dp_matrix[k][c])
                        max_area = max(max_area, width * (k - r + 1))
                    else:
                        break

        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        # heights = [0] * (col + 1)
        heights = dict.fromkeys(range(col + 1), 0)
        max_area = 0
        for r in range(row):
            for c in range(col):
                heights[c] = heights[c] + 1 if matrix[r][c] == "1" else 0

            stack = [-1]
            for c in range(col + 1):
                while heights[c] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    max_area = max(max_area, h * (c - stack[-1] - 1))
                stack.append(c)

        return max_area

    def maximalRectangle_stack_1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        def largestRectangle(hist):
            heights = hist + [0]
            h_stack = [-1]  # monotonic stack
            local_max = 0
            for idx_h, h in enumerate(heights):
                while h_stack and h < heights[h_stack[-1]]:
                    idx_pop = h_stack.pop()
                    local_max = max(local_max, heights[idx_pop] * (idx_h - h_stack[-1] - 1))
                h_stack.append(idx_h)
            return local_max

        histogram = [0] * col
        max_area = 0
        for r in range(row):
            for c in range(col):
                histogram[c] = histogram[c] + 1 if matrix[r][c] == "1" else 0

            max_area = max(max_area, largestRectangle(histogram))
        return max_area


if __name__ == "__main__":
    obj = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(obj.maximalRectangle(matrix))  # 6

    matrix = [["0"]]
    print(obj.maximalRectangle(matrix))  # 0

    matrix = [["1"]]
    print(obj.maximalRectangle(matrix))  # 1
