from bisect import bisect_left


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        rIdx_lower = 0
        rIdx_upper = row
        while rIdx_lower != rIdx_upper:
            idx = (rIdx_lower + rIdx_upper) // 2
            if target < matrix[idx][0]:
                rIdx_upper = idx
            else:
                rIdx_lower = idx + 1

        for r_idx in range(rIdx_lower):
            # if target in matrix[r_idx]:
            c_idx = bisect_left(matrix[r_idx], target)
            if c_idx != col and matrix[r_idx][c_idx] == target:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    print(obj.searchMatrix(matrix, target))  # true

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    print(obj.searchMatrix(matrix, target))  # false
