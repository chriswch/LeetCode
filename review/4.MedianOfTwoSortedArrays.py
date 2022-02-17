class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays(nums2, nums1)

        merged_halfLen = (nums1_len + nums2_len + 1) // 2

        nums1Cnt_lowerBound = 0
        nums1Cnt_upperBound = nums1_len

        while nums1Cnt_lowerBound < nums1Cnt_upperBound:
            nums1_cnt = (nums1Cnt_lowerBound + nums1Cnt_upperBound) // 2
            nums2_cnt = merged_halfLen - nums1_cnt
            if nums1[nums1_cnt] < nums2[nums2_cnt - 1]:
                nums1Cnt_lowerBound = nums1_cnt + 1
            else:
                nums1Cnt_upperBound = nums1_cnt

        nums1_cnt = nums1Cnt_lowerBound
        nums2_cnt = merged_halfLen - nums1_cnt

        if nums1_cnt and nums2_cnt:
            median = max(nums1[nums1_cnt - 1], nums2[nums2_cnt - 1])
        else:
            median = nums1[nums1_cnt - 1] if nums1_cnt else nums2[nums2_cnt - 1]

        if (nums1_len + nums2_len) % 2:  # odd
            return median
        else:  # even
            if nums1_cnt != nums1_len and nums2_cnt != nums2_len:
                return (median + min(nums1[nums1_cnt], nums2[nums2_cnt])) / float(2)
            else:
                return (
                    (median + nums2[nums2_cnt]) / float(2)
                    if nums1_cnt == nums1_len
                    else (median + nums1[nums1_cnt]) / float(2)
                )

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays(nums2, nums1)

        merged_halfLen = (nums1_len + nums2_len + 1) // 2

        nums1_left = 0
        nums1_right = nums1_len

        while nums1_left < nums1_right:
            nums1_halfLen = (nums1_left + nums1_right) // 2
            nums2_halfLen = merged_halfLen - nums1_halfLen
            if nums1[nums1_halfLen] < nums2[nums2_halfLen - 1]:
                nums1_left = nums1_halfLen + 1
            else:
                nums1_right = nums1_halfLen

        nums1_half = nums1_left
        nums2_half = merged_halfLen - nums1_half
        median = max(
            float("-inf") if nums1_half == 0 else nums1[nums1_half - 1],
            float("-inf") if nums2_half == 0 else nums2[nums2_half - 1],
        )

        if (nums1_len + nums2_len) % 2 == 1:
            return median

        median2 = min(
            float("inf") if nums1_half == nums1_len else nums1[nums1_half],
            float("inf") if nums2_half == nums2_len else nums2[nums2_half],
        )

        return float(median + median2) / 2


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    print(obj.findMedianSortedArrays(nums1, nums2))  # 2

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(obj.findMedianSortedArrays(nums1, nums2))  # 2.5
