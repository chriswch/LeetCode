class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.result = []

        self.dfs(target, [])
        return self.result

    def dfs(self, target, sum_list):
        if target == 0:
            self.result.append(sum_list)
            return

        for n in self.candidates:
            if n > target:
                break
            elif not sum_list or n >= sum_list[-1]:
                self.dfs(target - n, sum_list + [n])

    def combinationSum_1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum_dict = {0: [[]]}
        for n in candidates:
            next_dict = {}

            for prev_sum in sum_dict:
                if prev_sum not in next_dict:
                    next_dict[prev_sum] = sum_dict[prev_sum]
                else:
                    next_dict[prev_sum].extend(sum_dict[prev_sum])

                print(f"candidate: {n}, prev_sum: {prev_sum}, next_dict: {next_dict[prev_sum]}")

                curr_sum = prev_sum + n
                while curr_sum <= target:
                    if curr_sum not in next_dict:
                        next_dict[curr_sum] = [prev_list + [n] for prev_list in next_dict[prev_sum]]
                    else:
                        next_dict[curr_sum].extend([prev_list + [n] for prev_list in next_dict[prev_sum]])

                    prev_sum = curr_sum
                    curr_sum += n

            sum_dict = next_dict

        return [list(item) for item in set(tuple(row) for row in sum_dict[target])] if target in sum_dict else []


if __name__ == "__main__":
    obj = Solution()

    candidates = [2, 3, 6, 7]
    target = 7
    print(obj.combinationSum(candidates, target))  # [[2,2,3],[7]]

    candidates = [2, 3, 5]
    target = 8
    print(obj.combinationSum(candidates, target))  # [[2,2,2,2],[2,3,3],[3,5]]

    candidates = [2]
    target = 1
    print(obj.combinationSum(candidates, target))  # []

    candidates = [1, 2]
    target = 4
    print(obj.combinationSum(candidates, target))  # [[1,1,1,1],[1,1,2],[2,2]]
