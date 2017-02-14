class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l = [0 for i in range(26)]
        for i in range(len(magazine)):
            l[ord(magazine[i]) - ord('a')] += 1
        for i in range(len(ransomNote)):
            l[ord(ransomNote[i]) - ord('a')] -= 1
            if l[ord(ransomNote[i]) - ord('a')] < 0:
                return False
        return True
# Time: O(n)
# Space: O(1)
