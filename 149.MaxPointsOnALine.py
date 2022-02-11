class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        if len(points) <= 2:
            return len(points)

        # A line is determined by two factors,say y=ax+b
        # a = (y2-y1)/(x2-x1) a is a rational

        # The map tracks slopes for the current point only.
        # So parallel lines do not sum up points.
        res = 0
        for i in range(len(points)):
            d = {"inf": 1}  # vertical line; horizontal line's slope will be 0
            for j in range(i + 1, len(points)):
                # check for vertical line
                if points[i][0] == points[j][0]:  # they share the same x-value -> vertical line
                    d["inf"] += 1
                else:
                    slope = float(points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    if slope not in d:
                        d[slope] = 1  # Add itself
                    d[slope] += 1
            res = max(res, max(d.values()))  # For every point, check the largest possible res
        return res

    def maxPoints_1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points_len = len(points)
        if points_len <= 2:
            return points_len

        result = 0
        for base_idx in range(points_len - 1):
            curr_dict = {}
            for p_idx in range(base_idx + 1, points_len):
                x_diff = points[p_idx][0] - points[base_idx][0]
                y_diff = points[p_idx][1] - points[base_idx][1]

                if x_diff == 0:  # y-axis
                    y_diff = 1
                elif y_diff == 0:  # x-axis
                    x_diff = 1
                else:
                    xy_gcd = self.generateGCD(x_diff, y_diff)
                    x_diff = int(x_diff / xy_gcd)
                    y_diff = int(y_diff / xy_gcd)

                    if x_diff <= 0 and y_diff <= 0:
                        x_diff = -x_diff
                        y_diff = -y_diff
                    elif x_diff <= 0 and y_diff >= 0:
                        x_diff = -x_diff
                        y_diff = -y_diff

                if x_diff in curr_dict:
                    if y_diff in curr_dict[x_diff]:
                        curr_dict[x_diff][y_diff] += 1
                    else:
                        curr_dict[x_diff][y_diff] = 2
                else:
                    curr_dict[x_diff] = {y_diff: 2}

            maximum = 0
            for key_x in curr_dict:
                for key_y in curr_dict[key_x]:
                    maximum = max(maximum, curr_dict[key_x][key_y])
            result = max(result, maximum)

        return result

    def generateGCD(self, a, b):
        if b == 0:
            return a
        else:
            return self.generateGCD(b, a % b)


if __name__ == "__main__":
    obj = Solution()

    points = [[1, 1], [2, 2], [3, 3]]
    print(obj.maxPoints(points))  # 3

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(obj.maxPoints(points))  # 4

    points = [[0, 0], [1, -1], [1, 1]]
    print(obj.maxPoints(points))  # 2

    points = [[0, 1], [0, 0], [0, 4], [0, -2], [0, -1], [0, 3], [0, -4]]
    print(obj.maxPoints(points))  # 7
