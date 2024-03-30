"""
Sorting in Ascending order
1. Build a Max heap
2. Swap the root and last element
3. Then apply max heapify
4. repeat step 2-3 until

"""

class MaxHeap:

    def __init__(self, arr=[]):

        self.arr = arr

        self.build_heap()

    def build_heap(self):

        arr = self.arr
        n = len(arr) - 1
        i = (n - 1) // 2

        while i >= 0:
            self.max_heapify(len(arr), i)
            i -= 1

    def max_heapify(self, n, i=0):
        arr = self.arr

        max_i = n

        while i < max_i:

            left = (2 * i) + 1
            right = (2 * i) + 2
            largest = i

            if left < max_i and arr[left] > arr[largest]:
                largest = left

            if right < max_i and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]

            else:
                return

            i = largest

    # sort in ascending order: Max heap
    def heap_sort(self):
        # we assume that the heap given is max heapified
        arr = self.arr
        # the elements in the given heap
        n = len(arr) - 1

        # iterate all the elements
        while n > 0:
            # simce the heap is max heapified, the top is maximum
            # hence we swap it with the last element and apply max heapification
            arr[0], arr[n] = arr[n], arr[0]
            self.max_heapify(n, 0)
            # the heap again now has the max element at top
            # keep on reducing the heap size
            n -= 1


arr = [3, 1, 10, 2]
arr = [10, 15, 50, 4, 20]
heap = MaxHeap(arr)
heap.heap_sort()
print(arr)
