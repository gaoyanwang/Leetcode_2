class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'

        for i in range(1, n):
            j = 1
            count = 1
            ret = ''
            while j < len(result):
                if int(result[j]) == int(result[j - 1]):
                    count = count + 1
                    j = j + 1
                else:
                    ret += str(count) + result[j - 1]  # wrap up previous
                    count = 1  # Setup new
                    j = j + 1  # Move forward
            result = ret + str(count) + result[-1]  # update result

        return result

# Space = len(str)
# Time = en(str) * n
