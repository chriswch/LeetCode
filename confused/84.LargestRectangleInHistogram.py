class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heights.append(0)
        maxarea = 0
        stack = [-1]
        for idx, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                i = stack.pop()
                maxarea = max(heights[i] * (idx - stack[-1] - 1), maxarea)
            stack.append(idx)

        return maxarea

    def largestRectangleArea_1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack_idx = []  # monotonic stack
        max_area = 0

        for idx, h in enumerate(heights):
            while stack_idx and heights[stack_idx[-1]] >= h:
                last_idx = stack_idx.pop()
                width = idx - stack_idx[-1] - 1 if stack_idx else idx

                new_area = width * heights[last_idx]
                if new_area > max_area:
                    max_area = new_area
            stack_idx.append(idx)

        return max_area


if __name__ == "__main__":
    obj = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    print(obj.largestRectangleArea(heights))  # 10

    heights = [2, 4]
    print(obj.largestRectangleArea(heights))  # 4
