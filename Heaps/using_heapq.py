import heapq

# create a heap

pq = [5, 20, 1, 30, 4]

# creates a min heap
heapq.heapify(pq)
print(pq)

# push an item to heap , maintaining the min heap
heapq.heappush(pq, 3)
print(pq)

# pop the min element form the heap
heapq.heappop(pq)
print(pq)

# get the n largest element form the heap
print(heapq.nlargest(2, pq))

# get the n smallest element from the heap
print(heapq.nsmallest(2, pq))

# push and pop fromt the heap
# first it will push the element, then pop the smallest element
print(heapq.heappushpop(pq, 11))
print(pq)

# if a pushpop is given a number smaller than root, then we get the
# same heap
print(heapq.heappushpop(pq, 0))
print(pq)

print("--")
# heap replace : Pop and return the current smallest value, and add the new item.
print(heapq.heapreplace(pq, 50))
print(pq)
