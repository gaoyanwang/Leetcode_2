class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        l = [0 for i in range(10)]

        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if l[int(secret[i])] < 0:
                    B += 1
                if l[int(guess[i])] > 0:
                    B += 1
                l[int(secret[i])] += 1
                l[int(guess[i])] -= 1
        return str(A) + "A" + str(B) + "B"
# Time: O(n)
# Space: O(1)
