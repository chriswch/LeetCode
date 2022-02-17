import bisect


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        seq = "123456789"
        res = []

        for l in range(2, 10):
            for i in range(len(seq) - l + 1):
                num = int(seq[i : i + l])

                if num > high:
                    return res
                if num >= low:
                    res.append(num)
        return res

    def sequentialDigits_myself_2(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        sequential_digits = "123456789"

        length_min = len(str(low))
        length_max = min(len(str(high)) + 1, len(sequential_digits) + 1)

        results = []
        for length in range(length_min, length_max):
            for idx in range(0, 9):
                if idx + length > len(sequential_digits):
                    continue

                number = int(sequential_digits[idx : idx + length])
                if number >= low and number <= high:
                    results.append(number)
                elif number > high:
                    break

        return results

    def sequentialDigits_myself(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        candidates = [
            12,
            23,
            34,
            45,
            56,
            67,
            78,
            89,
            123,
            234,
            345,
            456,
            567,
            678,
            789,
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
            23456,
            34567,
            45678,
            56789,
            123456,
            234567,
            345678,
            456789,
            1234567,
            2345678,
            3456789,
            12345678,
            23456789,
            123456789,
        ]

        idx_start = bisect.bisect_left(candidates, low)
        idx_end = bisect.bisect_right(candidates, high)

        return candidates[idx_start:idx_end]


if __name__ == "__main__":
    obj = Solution()

    ### Example ###

    low = 100
    high = 300
    print(obj.sequentialDigits(low, high))

    low = 1000
    high = 13000
    print(obj.sequentialDigits(low, high))

    ### low is the smallest value

    low = 10
    high = 10
    print(obj.sequentialDigits(low, high))

    low = 10
    high = 12
    print(obj.sequentialDigits(low, high))

    low = 10
    high = 125
    print(obj.sequentialDigits(low, high))

    low = 10
    high = 123456780
    print(obj.sequentialDigits(low, high))

    low = 10
    high = 123456789
    print(obj.sequentialDigits(low, high))

    low = 10
    high = pow(10, 9)
    print(obj.sequentialDigits(low, high))

    ### low is 12 ###

    low = 12
    high = 12
    print(obj.sequentialDigits(low, high))

    low = 12
    high = 125
    print(obj.sequentialDigits(low, high))

    low = 12
    high = 123456780
    print(obj.sequentialDigits(low, high))

    low = 12
    high = 123456789
    print(obj.sequentialDigits(low, high))

    low = 12
    high = pow(10, 9)
    print(obj.sequentialDigits(low, high))

    ### low is 123456780 ###

    low = 123456780
    high = 123456780
    print(obj.sequentialDigits(low, high))

    low = 123456780
    high = 123456789
    print(obj.sequentialDigits(low, high))

    low = 123456780
    high = pow(10, 9)
    print(obj.sequentialDigits(low, high))

    ### low is 123456789 ###

    low = 123456789
    high = 123456789
    print(obj.sequentialDigits(low, high))

    low = 123456789
    high = pow(10, 9)
    print(obj.sequentialDigits(low, high))

    ### low is 123456789 + 1 ###

    low = 123456790
    high = 123456790
    print(obj.sequentialDigits(low, high))

    low = 123456790
    high = pow(10, 9)
    print(obj.sequentialDigits(low, high))
