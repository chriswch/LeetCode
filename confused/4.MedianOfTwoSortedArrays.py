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

        nums1_left = 0
        nums1_right = nums1_len

        while nums1_left < nums1_right:
            nums1_halfLen = nums1_left + (nums1_right - nums1_left) // 2
            nums2_halfLen = merged_halfLen - nums1_halfLen
            if nums1[nums1_halfLen] < nums2[nums2_halfLen - 1]:
                nums1_left = nums1_halfLen + 1
            else:
                nums1_right = nums1_halfLen

        nums1_half = nums1_left
        nums2_half = merged_halfLen - nums1_half
        median = max(
            float("-inf") if nums1_half <= 0 else nums1[nums1_half - 1],
            float("-inf") if nums2_half <= 0 else nums2[nums2_half - 1],
        )

        if (nums1_len + nums2_len) % 2 == 1:
            return median

        median2 = min(
            float("inf") if nums1_half >= nums1_len else nums1[nums1_half],
            float("inf") if nums2_half >= nums2_len else nums2[nums2_half],
        )

        return (median + median2) / 2


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    print(obj.findMedianSortedArrays(nums1, nums2))  # 2

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(obj.findMedianSortedArrays(nums1, nums2))  # 2.5
