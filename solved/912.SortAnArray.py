class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # self.bubble_sort(nums)
        # self.quick_sort(nums, 0, len(nums) - 1)
        # self.selection_sort(nums)
        self.insertion_sort(nums)

        return nums

    def insertion_sort(self, nums):
        nums_len = len(nums)
        for i in range(1, nums_len):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]

    def selection_sort(self, nums):
        nums_len = len(nums)
        for target_idx in range(nums_len - 1):
            minimum_idx = target_idx
            for idx in range(target_idx + 1, nums_len):
                if nums[idx] < nums[minimum_idx]:
                    minimum_idx = idx

            nums[target_idx], nums[minimum_idx] = nums[minimum_idx], nums[target_idx]

    def quick_sort(self, nums, left, right):  # Quick Sort
        if left >= right:
            return

        key = nums[left]
        i = left
        j = right

        while i != j:
            while nums[j] > key and j != i:
                j -= 1

            while nums[i] <= key and i != j:
                i += 1

            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left] = nums[i]
        nums[i] = key

        self.quick_sort(nums, left, i - 1)
        self.quick_sort(nums, i + 1, right)

    def bubble_sort(self, nums):  # Bubble Sort
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_len = len(nums)
        for i in range(n_len - 1):
            for j in range(0, n_len - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == "__main__":
    obj = Solution()

    nums = [0]
    print(obj.sortArray(nums))  # [0]

    nums = [1, 0]
    print(obj.sortArray(nums))  # [0, 1]

    nums = [5, 2, 3, 1]
    print(obj.sortArray(nums))  # [1,2,3,5]

    nums = [5, 1, 1, 2, 0, 0]
    print(obj.sortArray(nums))  # [0,0,1,1,2,5]
