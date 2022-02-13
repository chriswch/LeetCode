class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        hottest = 0
        answer = [0] * n

        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue

            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer

    def dailyTemperatures_1(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        t_stack = []  # monotonically decreasing stack
        result = [0] * len(temperatures)

        for t_idx, t in enumerate(temperatures):
            while t_stack and t > temperatures[t_stack[-1]]:
                pop_idx = t_stack.pop()
                result[pop_idx] = t_idx - pop_idx

            t_stack.append(t_idx)

        return result


if __name__ == "__main__":
    obj = Solution()

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(obj.dailyTemperatures(temperatures))  # [1,1,4,2,1,1,0,0]

    temperatures = [30, 40, 50, 60]
    print(obj.dailyTemperatures(temperatures))  # [1,1,1,0]

    temperatures = [30, 60, 90]
    print(obj.dailyTemperatures(temperatures))  # [1,1,0]
