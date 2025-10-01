class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return "Stack is empty!"
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return "Stack is empty!"
    def is_empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
s = Stack()
print("Is empty?", s.is_empty())

for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())