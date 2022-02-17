class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        bound_low = max(1, sum(piles) // h)
        bound_up = max(piles)

        while bound_low < bound_up:
            mid = (bound_low + bound_up) // 2

            enough = True
            cnt = 0
            for p in piles:
                cnt += p // mid
                cnt = cnt + 1 if p % mid else cnt
                if cnt > h:
                    enough = False
                    break

            if enough:
                bound_up = mid
            else:
                bound_low = mid + 1

        return bound_low


if __name__ == "__main__":
    obj = Solution()

    piles = [3, 6, 7, 11]
    h = 8
    print(obj.minEatingSpeed(piles, h))  # 4

    piles = [30, 11, 23, 4, 20]
    h = 5
    print(obj.minEatingSpeed(piles, h))  # 30

    piles = [30, 11, 23, 4, 20]
    h = 6
    print(obj.minEatingSpeed(piles, h))  # 23
