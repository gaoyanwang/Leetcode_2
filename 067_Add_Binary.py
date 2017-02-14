class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        s = ""

        # a, b common numbers
        if len(a) >= len(b):
            for i in range(1, len(a) + 1):
                if i <= len(b):
                    digit = (int(a[-i]) + int(b[-i]) + carry) % 2
                    carry = (int(a[-i]) + int(b[-i]) + carry) // 2
                else:
                    digit = (int(a[-i]) + carry) % 2
                    carry = (int(a[-i]) + carry) // 2
                s = str(digit) + s
        else:
            for i in range(1, len(b) + 1):
                if i <= len(a):
                    digit = (int(a[-i]) + int(b[-i]) + carry) % 2
                    carry = (int(a[-i]) + int(b[-i]) + carry) // 2
                else:
                    digit = (int(b[-i]) + carry) % 2
                    carry = (int(b[-i]) + carry) // 2
                s = str(digit) + s

        if carry == 1:
            s = '1' + s

        return s

# Space =  max(a, b)
# Time = max(a, b)

class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        s = ""

        # a, b common numbers
        if len(b) > len(a):
            return self.addBinary(b, a)

        for i in range(-1, -len(a) - 1, -1):
            if abs(i) <= len(b):
                digit = (int(a[i]) + int(b[i]) + carry) % 2
                carry = (int(a[i]) + int(b[i]) + carry) // 2
            else:
                digit = (int(a[i]) + carry) % 2
                carry = (int(a[i]) + carry) // 2
            s = str(digit) + s

        if carry == 1:
            s = '1' + s

        return s

# Space =  max(a, b)
# Time = max(a, b)
