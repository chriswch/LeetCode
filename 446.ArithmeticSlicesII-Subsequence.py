class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        arr_table = [[None] * nums_len for _ in range(nums_len)]

        for i in range(nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                diff = nums[j] - nums[i]
                third_value = nums[j] + diff

                if third_value in nums[j + 1 :]:
                    third_index = nums.index(third_value, j + 1)
                    arr_table[i][j] = {
                        "spacing": diff,
                        "index": [third_index],
                        "counter": 1,
                    }

                    search_from = third_index
                    while third_value in nums[search_from + 1 :]:
                        search_from = nums.index(third_value, search_from + 1)

                        arr_table[i][j]["counter"] += 1
                        arr_table[i][j]["index"].append(search_from)

        for i in range(nums_len - 3, -1, -1):
            for j in range(nums_len - 2, i, -1):
                if arr_table[i][j]:

                    for third_index in arr_table[i][j]["index"]:
                        if arr_table[j][third_index]:
                            arr_table[i][j]["counter"] += arr_table[j][third_index]["counter"]

        cnt = 0
        for i in range(nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                if arr_table[i][j]:
                    cnt += arr_table[i][j]["counter"]

        return cnt


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 4, 6, 8, 10]
    print(obj.numberOfArithmeticSlices(nums))

    nums = [7, 7, 7, 7, 7]
    print(obj.numberOfArithmeticSlices(nums))

    nums = [
        79,
        20,
        64,
        28,
        67,
        81,
        60,
        58,
        97,
        85,
        92,
        96,
        82,
        89,
        46,
        50,
        15,
        2,
        36,
        44,
        54,
        2,
        90,
        37,
        7,
        79,
        26,
        40,
        34,
        67,
        64,
        28,
        60,
        89,
        46,
        31,
        9,
        95,
        43,
        19,
        47,
        64,
        48,
        95,
        80,
        31,
        47,
        19,
        72,
        99,
        28,
        46,
        13,
        9,
        64,
        4,
        68,
        74,
        50,
        28,
        69,
        94,
        93,
        3,
        80,
        78,
        23,
        80,
        43,
        49,
        77,
        18,
        68,
        28,
        13,
        61,
        34,
        44,
        80,
        70,
        55,
        85,
        0,
        37,
        93,
        40,
        47,
        47,
        45,
        23,
        26,
        74,
        45,
        67,
        34,
        20,
        33,
        71,
        48,
        96,
    ]
    print(obj.numberOfArithmeticSlices(nums))
