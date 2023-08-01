class Stack:
    """Stack object"""
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        """Checking of stack is empty or not"""
        return len(self.stack) == 0

    def push(self, data):
        """Adding new element to stack"""
        self.stack.append(data)
        return True

    def pop(self):
        """Pop elements from stack"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        """See element which is situated in the peek"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]


stack = Stack()

print(stack.isEmpty())
print(stack.push(5))
print(stack.push(6))
print(stack.pop())
print(stack.peek())
