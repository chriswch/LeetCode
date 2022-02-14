class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 1:
            return False

        nums.sort()

        mid = length / 2

        L, R = nums[:mid], nums[mid:]

        sumL = sum(L)
        sumR = sum(R)

        while sumL < sumR:
            if (sumR - sumL) / 2 in R:
                print((sumL - sumR) * 2)
                R.remove((sumR - sumL) / 2)
                L.append((sumR - sumL) / 2)
                break
            else:
                el = R[0]
                L.append(el)
                R.pop(0)
                sumL += el
                sumR -= el
        while sumL > sumR:
            if (sumL - sumR) / 2 in L:
                print((sumL - sumR) * 2)
                L.remove((sumL - sumR) / 2)
                R.append((sumL - sumR) / 2)
                break
            el = L[0]
            R.append(el)
            L.pop(0)
            sumL -= el
            sumR += el

        if sum(L) == sum(R):
            return True
        return False

    def canPartition_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2:
            return False

        target = total_sum // 2
        sum_set = set([0])
        for n in nums:
            if n > target:
                continue

            next_sum = set()
            for item in sum_set:
                item += n

                if item > target:
                    continue
                elif item == target:
                    return True
                else:
                    next_sum.add(item)

            sum_set = sum_set.union(next_sum)

        return False


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 5, 11, 5]
    print(obj.canPartition(nums))  # True

    nums = [1, 2, 3, 5]
    print(obj.canPartition(nums))  # False
