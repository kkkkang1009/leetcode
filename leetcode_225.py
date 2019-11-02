# 225. Implement Stack using Queues
class MyStack:
    stack = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        del self.stack[:]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        num = self.stack[len(self.stack) - 1]
        self.stack.remove(num)
        return num

    def top(self) -> int:
        """
        Get the top element.
        """
        num = self.stack[len(self.stack) - 1]
        return num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.stack) > 0:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()