class Trie:
    def __init__(self):
        self.left = None
        self.right = None


class Solution(object):
    def findMaximumXOR_Trie(self, nums):  # TLE
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Trie()
        RIGHT_SHIFT = 30

        def add(num):
            curr = root
            for k in range(RIGHT_SHIFT, -1, -1):
                bit = (num >> k) & 1
                if bit:
                    if not curr.right:
                        curr.right = Trie()
                    curr = curr.right
                else:
                    if not curr.left:
                        curr.left = Trie()
                    curr = curr.left

        def check(num):
            curr = root
            maximum = 0
            for k in range(RIGHT_SHIFT, -1, -1):
                bit = (num >> k) & 1
                if bit:
                    maximum = (maximum << 1) + 1 if curr.left else maximum << 1
                    curr = curr.left if curr.left else curr.right
                else:
                    maximum = (maximum << 1) + 1 if curr.right else maximum << 1
                    curr = curr.right if curr.right else curr.left

            return maximum

        maximum = 0
        for i in range(1, len(nums)):
            add(nums[i - 1])
            maximum = max(maximum, check(nums[i]))

        return maximum

    def findMaximumXOR_hashTable(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        RIGHT_SHIFT = 30

        x = 0
        for k in range(RIGHT_SHIFT, -1, -1):
            pre_bits = set()

            for num in nums:
                pre_bits.add(num >> k)

            x_next = (x << 1) + 1  # bitwise operators have the lower priority
            found = False
            for num in pre_bits:
                if x_next ^ num in pre_bits:
                    found = True
                    break

            x = x_next if found else x << 1

        return x


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 10, 5, 25, 2, 8]
    print(obj.findMaximumXOR(nums))  # 28

    nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
    print(obj.findMaximumXOR(nums))  # 127
