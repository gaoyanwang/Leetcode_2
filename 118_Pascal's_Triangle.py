class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[1]]

        for i in range(2, numRows + 1):  # if 5 rows, i: 2, 3, 4
            # head and middle part
            cur = [1]
            for j in range(0, i - 2):
                cur.append(ret[i - 2][j] + ret[i - 2][j + 1])
            # add 1 to tail
            cur.append(1)
            ret.append(cur)
        return ret
# Space: O(n*n)
# Time: O(n*n)
