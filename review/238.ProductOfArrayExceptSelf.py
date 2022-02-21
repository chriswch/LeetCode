class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_len = len(nums)

        result = [None] * n_len
        result[0] = 1
        for n_idx in range(1, n_len):
            result[n_idx] = result[n_idx - 1] * nums[n_idx - 1]

        postfix_product = 1
        for n_idx in range(n_len - 1, -1, -1):
            result[n_idx] *= postfix_product
            postfix_product *= nums[n_idx]

        return result

    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_len = len(nums)

        prefix_tmp = 1
        prefix_prod = []
        postfix_tmp = 1
        postfix_product = []
        for n_idx in range(n_len):
            prefix_prod.append(prefix_tmp)
            prefix_tmp *= nums[n_idx]
            postfix_product.insert(0, postfix_tmp)
            postfix_tmp *= nums[-n_idx - 1]

        result = []
        for n_idx in range(n_len):
            result.append(prefix_prod[n_idx] * postfix_product[n_idx])

        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4]
    print(obj.productExceptSelf(nums))  # [24,12,8,6]

    nums = [-1, 1, 0, -3, 3]
    print(obj.productExceptSelf(nums))  # [0,0,9,0,0]
