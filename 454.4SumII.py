import collections
from collections import Counter


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_1 = collections.defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                sum_1[n1 + n2] += 1

        cnt = 0
        for n3 in nums3:
            for n4 in nums4:
                cnt += sum_1[-n3 - n4]

        return cnt

    def fourSumCount_1(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_1 = Counter([n1 + n2 for n2 in nums2 for n1 in nums1])
        sum_2 = Counter([n3 + n4 for n4 in nums4 for n3 in nums3])

        cnt = 0
        for key_1 in sum_1.keys():
            for key_2 in sum_2.keys():
                if key_1 + key_2 == 0:
                    cnt += sum_1[key_1] * sum_2[key_2]

        return cnt


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(obj.fourSumCount(nums1, nums2, nums3, nums4))  # 2

    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    print(obj.fourSumCount(nums1, nums2, nums3, nums4))  # 1
