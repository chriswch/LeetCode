class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        result = curr_row = [poured]
        for r_idx in range(query_row + 1):
            col = r_idx + 1

            next_row = [0] * (col + 1)
            for c_idx in range(col):
                overflow = (curr_row[c_idx] - 1) / 2.0
                if overflow > 0:
                    next_row[c_idx] += overflow
                    next_row[c_idx + 1] += overflow

            result = curr_row
            curr_row = next_row

        return min(1, result[query_glass])


if __name__ == "__main__":
    obj = Solution()

    poured = 1
    query_row = 1
    query_glass = 1
    print(obj.champagneTower(poured, query_row, query_glass))  # 0

    poured = 2
    query_row = 1
    query_glass = 1
    print(obj.champagneTower(poured, query_row, query_glass))  # 0.5

    poured = 100000009
    query_row = 33
    query_glass = 17
    print(obj.champagneTower(poured, query_row, query_glass))  # 1
