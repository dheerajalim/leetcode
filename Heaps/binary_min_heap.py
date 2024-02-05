"""
A binary heap is a complete Binary Tree Structure.
A complete Binary tree is a tree whose all levels are complete (i.e all nodes have 2 children)
Except the leaf nodes, who will be filled in order i.e. left to right

Formula :
parent = (i - 1) // 2 : floor value
left = 2*i + 1
right = 2 * i + 2
"""

"""
Min Heap : The descendants should be greater than parent
"""


class MinHeap:

    def __init__(self, arr=[]):
        self.arr = arr
        # build heap
        self.build_heap()

    def build_heap(self):
        arr = self.arr
        n = len(arr) - 1
        # the last parent, after this i all will be leaf nodes
        i = (n - 1) // 2

        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def insert(self, value):

        self.arr.append(value)
        i = len(self.arr) - 1

        while i > 0 and self.arr[(i - 1) // 2] > value:
            parent = (i - 1) // 2
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            i = parent

    def extract_min(self):
        """Removes the min element and returns the min element"""
        # for a min heap, the root is the
        # the minimum element
        # hence we remove root and then follow
        # min_heapify to create a valid min heap again

        arr = self.arr

        # edge case:

        if len(arr) == 0:
            return "Empty heap"
        # this brings the top element to last
        # hence we can remove the min element in
        # O(1) time
        result = arr[0]
        # change the 0th element with last element
        arr[0] = arr[-1]
        # removes the last element, as this is already move to 0th index
        arr.pop()

        # need to min_heapify the arr, so that min heap is
        # no disturbed
        self.min_heapify()
        return result

    def min_heapify(self, i=0):
        arr = self.arr
        # the max possible value of i
        max_i = len(arr)

        # iterate until the i is a valid value
        # so that the arr index out of error is not encountered
        while i < max_i:
            # calculate the left and right child indexes
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            # assuming initially that the root is the smallest
            smallest = i
            # if the left index is valid and smaller that smallest; swap
            # update smallest to left index
            if left_child < max_i and arr[left_child] < arr[smallest]:
                smallest = left_child
            # if the right index is valid and smaller that the smallest; swap
            # update the smallest to right index
            if right_child < max_i and arr[right_child] < arr[smallest]:
                smallest = right_child

            # if the smallest is not equal to i (initial value),
            # then either left /right were smaller, hence swap
            # the root with smallest
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
            # otherwise the root was already smallest , we return
            else:
                return
            # update the i to the new smallest and iterate
            i = smallest

    def decrease_key(self, i, value):

        """Replace the item at index i with value and maintain min heap """
        arr = self.arr
        n = len(arr) - 1
        if i > n:
            return "Invalid Index"

        # updating the index i with given value
        arr[i] = value
        # use the same concept o f insert .
        # compare with parent, if parent is greater, swap
        # and update i to parent index
        while i > 0 and arr[(i - 1) // 2] > arr[i]:
            parent = (i - 1) // 2
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = parent

    def delete_key(self, i):
        """To delete the key at index i"""

        # we replace the value at index i with -inf
        # then run the decrease_key on it
        # this way the -inf will be the root of the heap
        # then run extract_min, this way the -inf will be removed
        # and we will have a valid min heap
        arr = self.arr
        # edge case
        if i < 0 or i > len(arr) - 1:
            return "Invalid Index"

        # decreasing the key at given index to -inf
        self.decrease_key(i, float('-inf'))
        # after the above operation the -inf will be the root

        # now call extract min to remove -inf and produce min heap

        self.extract_min()


arr = [20, 25, 30, 35, 40, 80, 32, 100, 70, 60]
arr = [10, 20, 30, 40, 50, 35, 38, 45]
arr = [10, 5, 2, 20, 1, 40, 15, 5, 11]
arr = [8,10,2,3,4,5]
heap = MinHeap(arr)
# print(heap.extract_min())
# heap.min_heapify()
# heap.decrease_key(3, 5)
# heap.delete_key(i=3)
print(arr)
