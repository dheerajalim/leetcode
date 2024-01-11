from collections import deque


class MyQueue:

    def __init__(self):
        self.deq = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.deq.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.deq.popleft()

    def peek(self) -> int:
        return self.deq[0]

    def empty(self) -> bool:
        return 'false' if self.size else 'true'


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
