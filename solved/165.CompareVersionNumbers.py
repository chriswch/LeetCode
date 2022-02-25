from itertools import zip_longest


class Solution(object):
    def compareVersion(self, version1: str, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        splitted_1 = version1.split(".")
        splitted_2 = version2.split(".")
        for rev_1, rev_2 in zip_longest(splitted_1, splitted_2, fillvalue=0):
            rev_1 = int(rev_1)
            rev_2 = int(rev_2)
            if rev_1 < rev_2:
                return -1
            elif rev_1 > rev_2:
                return 1

        return 0


if __name__ == "__main__":
    obj = Solution()

    version1 = "1.01"
    version2 = "1.001"
    print(obj.compareVersion(version1, version2))  # 0

    version1 = "1.0"
    version2 = "1.0.0"
    print(obj.compareVersion(version1, version2))  # 0

    version1 = "0.1"
    version2 = "1.1"
    print(obj.compareVersion(version1, version2))  # -1
