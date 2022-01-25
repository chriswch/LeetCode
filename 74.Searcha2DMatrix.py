from numpy import mat


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)

        idx_max = m - 1
        idx_min = 0
        idx = m // 2
        while idx >= 0 and idx < m:
            if target in matrix[idx]:
                return True
            elif target > matrix[idx][0]:
                idx_min = idx
                idx = (idx + idx_max) // 2

                if idx == idx_min:
                    return True if target in matrix[idx_max] else False
            else:
                idx_max = idx
                idx = (idx + idx_min) // 2

                if idx == idx_min:
                    return True if target in matrix[idx_min] else False


if __name__ == "__main__":
    obj = Solution()

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(obj.searchMatrix(matrix, target))  # True

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(obj.searchMatrix(matrix, target))  # False

    matrix = [[1], [3]]
    target = 1
    print(obj.searchMatrix(matrix, target))  # True

    matrix = [
        [-8, -7, -6, -6, -6],
        [-5, -4, -3, -1, -1],
        [0, 0, 1, 3, 3],
        [5, 5, 6, 6, 6],
        [7, 8, 8, 10, 12],
        [13, 15, 17, 17, 18],
        [20, 20, 20, 20, 20],
        [22, 22, 22, 22, 23],
    ]
    target = 4
    print(obj.searchMatrix(matrix, target))  # False

    matrix = [[1], [3], [5]]
    target = 5
    print(obj.searchMatrix(matrix, target))  # True
