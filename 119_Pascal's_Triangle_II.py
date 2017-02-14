class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]

        for i in range(1, rowIndex + 1):
            cur = [1]
            for j in range(0, i - 1):
                cur.append(ret[j] + ret[j + 1])
            cur.append(1)
            ret = cur
        return ret
# Space: O(n)
# Time: O(n*n)
