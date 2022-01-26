class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def DFS(x, y):
            grid[x][y] = "0"

            for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == "1":
                    DFS(next_x, next_y)

        cnt = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    cnt += 1

                    DFS(x, y)

        return cnt


if __name__ == "__main__":
    obj = Solution()

    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(obj.numIslands(grid))  # 1

    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(obj.numIslands(grid))  # 3
