class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1 = version1.split('.')
        list2 = version2.split('.')

        n = max(len(list1), len(list2))
        m = min(len(list1), len(list2))
        i = 0
        while i < n:
            if i < m:
                if int(list1[i]) > int(list2[i]):
                    return 1
                if int(list1[i]) < int(list2[i]):
                    return -1
            else:
                if len(list1) > m:
                    if int(list1[i]) > 0:
                        return 1
                else:
                    if int(list2[i]) > 0:
                        return -1
            i = i + 1
        return 0


# Time: O(n)
# Space: O(n)
