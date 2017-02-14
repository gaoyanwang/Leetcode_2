class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u')  # vowels in a set

        ls = list(s)  # bigO?
        l, r = 0, len(s) - 1

        while l < r:  # Do not need to consider =
            while l < r and ls[l].lower() not in VOWELS:
                l += 1
            while l < r and ls[r].lower() not in VOWELS:
                r -= 1
            if l < r:  # check updated l, r index
                ls[l], ls[r] = ls[r], ls[l]
                l += 1  # update l, r
                r -= 1
        return "".join(ls)

# Time: O(n)
# Space: O(n)