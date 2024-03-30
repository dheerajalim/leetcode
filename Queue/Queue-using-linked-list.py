# A linked list (LL) node
# to store a queue entry
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    # Function to push an element into the queue.
    def push(self, item):

        # Add code here
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Function to pop front element from the queue.
    def pop(self):

        # add code here
        if self.front is None or self.rear is None:
            return -1

        if self.front.next is None:
            self.rear = None
            return self.front

        temp = self.front
        self.front = self.front.next

        return temp.data


queue_obj = MyQueue()

queue_obj.push(2)
queue_obj.push(3)
print(queue_obj.pop())
queue_obj.push(4)
print(queue_obj.pop())
