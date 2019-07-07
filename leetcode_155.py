# 155. Min Stack
class MinStack(object):
    stack = []
    size = 0
    low = float('inf')

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.low = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.size += 1
        if self.low > x:
            self.low = x

    def pop(self):
        """
        :rtype: None
        """
        self.size -= 1
        if self.stack[self.size] == self.low:
            self.stack.pop(self.size)
            self.low = float('inf')
            for i in range(0, self.size):
                if self.low > self.stack[i]:
                    self.low = self.stack[i]
        else:
            self.stack.pop(self.size)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.size - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.low

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()