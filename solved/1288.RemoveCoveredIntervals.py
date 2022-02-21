class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()

        prev_intvl = intervals[0]
        result = 1
        for intvl in intervals[1:]:
            if intvl[1] <= prev_intvl[1]:  # Remove the current interval
                continue
            elif intvl[0] == prev_intvl[0]:  # Remove the previous interval
                prev_intvl = intvl
            else:
                prev_intvl = intvl
                result += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    intervals = [[1, 4], [3, 6], [2, 8]]
    print(obj.removeCoveredIntervals(intervals))  # 2

    intervals = [[1, 4], [2, 3]]
    print(obj.removeCoveredIntervals(intervals))  # 1

    intervals = [[1, 2], [1, 4], [3, 4]]
    print(obj.removeCoveredIntervals(intervals))  # 1
