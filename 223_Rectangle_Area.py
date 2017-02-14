class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1 = max(A, E)
        x2 = min(C, G)
        y1 = max(B, F)
        y2 = min(D, H)
        overlap = (x2 - x1) * (y2 - y1)
        if x1 > x2 or y1 > y2:
            overlap = 0
        ret = (D - B) * (C - A) + (G - E) * (H - F) - overlap
        return ret
# Time: O(1)
# Space: O(1)
