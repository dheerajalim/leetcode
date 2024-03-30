# creating the stack
# perform push, pop, min operations


# Method 1 : using supporting stack ; Extra Space

class Stack:

    def __init__(self):
        self.stack = []
        self.supporting_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.supporting_stack:
            self.supporting_stack.append(item)
        elif item <= self.supporting_stack[-1]:
            self.supporting_stack.append(item)

    def pop(self):
        if not self.stack:
            print(-1)
            return
        item = self.stack.pop()

        if item == self.supporting_stack[-1]:
            print(self.supporting_stack.pop())
            return

    def find_min(self):
        print(self.supporting_stack[-1] if self.supporting_stack else -1)

    def print_stack(self):
        print(self.stack)
        print(self.supporting_stack)


# Method 2 : Using constant space

class StackNoSpace:

    def __init__(self):
        self.stack = []
        self.minvalue = float('inf')

    def push(self, item):
        if not self.stack:
            # in case the stack is empty
            self.stack.append(item)
            # the first element is set as the min value
            self.minvalue = item

        # if the new item is less than current min value
        elif item < self.minvalue:
            # add the value from formula as top of stack
            self.stack.append((2 * item) - self.minvalue)
            # pass the current item as the current min value
            self.minvalue = item
        else:
            # otherwise jus add to the top of stack
            self.stack.append(item)

    def pop(self):
        if not self.stack:
            print(-1)
            return

        # this means this was the min item, hence we need to
        # update the minvalue variable
        # if the top of stack is less than current min, this is a flag
        if self.stack[-1] < self.minvalue:
            print(self.minvalue)
            # we update the min value to the older min using formula
            self.minvalue = (2 * self.minvalue) - self.stack.pop()
            return

        print(self.stack.pop())
        return

    def find_min(self):
        print(self.minvalue)
        return

    def top(self):
        # if the stack top is less than current min, this is a flag
        # hence the current min value is returned as stacks top
        # has a formula driven value
        if self.stack[-1] < self.minvalue:
            print(self.minvalue)
        else:
            # otherwise just return the top of stack
            print(self.stack[-1])

    def print_stack(self):
        print(self.stack)


stack_obj = StackNoSpace()
stack_obj.push(-2)
stack_obj.push(0)
stack_obj.push(-1)
stack_obj.find_min()
stack_obj.top()
stack_obj.pop()

stack_obj.find_min()

# stack_obj = StackNoSpace()
# stack_obj.pop()
# stack_obj.find_min()
# stack_obj.push(18)
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.push(19)
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.push(29)
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.pop()
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.push(15)
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.pop()
# stack_obj.print_stack()
# stack_obj.push(30)
# stack_obj.print_stack()
# stack_obj.find_min()
# stack_obj.push(16)
# stack_obj.print_stack()
# stack_obj.find_min()
