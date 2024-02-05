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


arr = [3, 1, 10, 2]
arr = [10, 15, 50, 4, 20]
arr = [1,2,3,4,5,6]
heap = MaxHeap(arr)

print(arr)
