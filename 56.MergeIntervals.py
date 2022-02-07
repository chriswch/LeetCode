class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = [intervals[0]]

        for intvl in intervals[1:]:
            if intvl[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intvl[1])
            else:
                result.append(intvl)

        return result

    def merge_1(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        intvl_len = len(intervals)

        intvl_idx = 1
        while intvl_idx < intvl_len:
            if intervals[intvl_idx][0] <= intervals[intvl_idx - 1][1]:
                intervals[intvl_idx - 1][1] = max(intervals[intvl_idx - 1][1], intervals[intvl_idx][1])

                del intervals[intvl_idx : intvl_idx + 1]
                intvl_len -= 1
            else:
                intvl_idx += 1

        return intervals


if __name__ == "__main__":
    obj = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(obj.merge(intervals))  # [[1,6],[8,10],[15,18]]

    intervals = [[1, 4], [4, 5]]
    print(obj.merge(intervals))  # [[1,5]]
