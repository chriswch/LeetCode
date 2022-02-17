import bisect


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals_start = [item[0] for item in intervals]
        idx = bisect.bisect(intervals_start, newInterval[0])

        intervals_len = len(intervals)
        overlap_idx = idx
        remove_cnt = 0
        newInterval_end = newInterval[1]
        while (
            overlap_idx != intervals_len and intervals[overlap_idx][0] <= newInterval[1]
        ):
            remove_cnt += 1
            if intervals[overlap_idx][1] >= newInterval[1]:
                newInterval_end = intervals[overlap_idx][1]
                break
            overlap_idx += 1

        if idx != 0 and intervals[idx - 1][1] >= newInterval[0]:
            newInterval_start = intervals[idx - 1][0]
            if intervals[idx - 1][1] > newInterval_end:
                newInterval_end = intervals[idx - 1][1]

            del intervals[idx - 1 : idx + remove_cnt]
            intervals.insert(idx - 1, [newInterval_start, newInterval_end])
        else:
            del intervals[idx : idx + remove_cnt]
            intervals.insert(idx, [newInterval[0], newInterval_end])

        return intervals


if __name__ == "__main__":
    obj = Solution()

    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(obj.insert(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(obj.insert(intervals, newInterval))

    intervals = [[1, 5]]
    newInterval = [2, 3]
    print(obj.insert(intervals, newInterval))
