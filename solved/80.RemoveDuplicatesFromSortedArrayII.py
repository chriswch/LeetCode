class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_len = len(nums)

        from_idx = 0
        curr_cnt = 1
        curr_idx = 1
        while curr_idx < n_len:
            if nums[curr_idx] == nums[curr_idx - 1]:
                curr_cnt += 1
            else:
                if curr_cnt > 2:
                    del nums[from_idx + 2 : curr_idx]
                    n_len -= curr_cnt - 2
                    curr_idx -= curr_cnt - 2

                from_idx = curr_idx
                curr_cnt = 1

            curr_idx += 1

        if curr_cnt > 2:
            del nums[from_idx + 2 :]
            n_len -= curr_cnt - 2

        print(nums)
        return n_len


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    print(obj.removeDuplicates(nums))  # 5, nums = [1,1,2,2,3,_]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(obj.removeDuplicates(nums))  # 7, nums = [0,0,1,1,2,3,3,_,_]

    nums = [1, 1, 1]
    print(obj.removeDuplicates(nums))  # 2, nums = [1,1,_]
