class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_length = len(arr)
        if arr_length < 3:
            return False

        idx = 1
        while idx < arr_length:
            if arr[idx - 1] < arr[idx]:
                idx += 1
            elif arr[idx - 1] == arr[idx]:
                return False
            else:
                break

        if idx == 1 or idx == arr_length:
            return False

        idx += 1
        while idx < arr_length:
            if arr[idx - 1] > arr[idx]:
                idx += 1
            else:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    arr = [2, 1]
    print(obj.validMountainArray(arr))

    arr = [3, 5, 5]
    print(obj.validMountainArray(arr))

    arr = [0, 3, 2, 1]
    print(obj.validMountainArray(arr))
