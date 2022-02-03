class Solution(object):
    def trap_stack(self, height):
        """
        :type height: List[int]
        :rtype: 
        """
        h_stack = []  # descending monotonic stack
        result = 0
        for h_idx, h in enumerate(height):
            while h_stack and h >= height[h_stack[-1]]:
                target_idx = h_stack.pop()
                if h_stack:
                    left_idx = h_stack[-1]
                    area = (min(h, height[left_idx]) - height[target_idx]) * (h_idx - left_idx - 1)
                    result += area
            h_stack.append(h_idx)

        return result

    def trap_dp(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h_len = len(height)

        left_max = [0] * h_len
        left_max[0] = height[0]
        for h_idx in range(1, h_len):
            left_max[h_idx] = max(left_max[h_idx - 1], height[h_idx])

        right_max = 0
        result = 0
        for h_idx in range(h_len - 1, -1, -1):
            right_max = max(right_max, height[h_idx])
            min_height = min(left_max[h_idx], right_max)

            trap = min_height - height[h_idx]
            if trap > 0:
                result += trap

        return result


if __name__ == "__main__":
    obj = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(obj.trap(height))  # 6

    height = [4, 2, 0, 3, 2, 5]
    print(obj.trap(height))  # 9
