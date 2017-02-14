class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if self.stack2 == [] or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack1 == []:
            raise IndexError("pop from empty list")
        else:
            x = self.stack1.pop()
            if x == self.stack2[-1]:
                self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack1 == []:
            raise IndexError("pop from empty list")
        else:
            return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack2 == []:
            raise IndexError("pop from empty list")
        else:
            return self.stack2[-1]

# Space: O(n)
# Time: O(1)
