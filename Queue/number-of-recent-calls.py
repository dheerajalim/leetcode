"""https://leetcode.com/problems/number-of-recent-calls/description/"""

from collections import deque


class RecentCounter:

    def __init__(self):
        # initializing the DEQUE
        self.deq = deque()
        # the list to store the time range
        self.range = []

    def ping(self, t: int) -> int:
        # we append the new pint to the queue
        self.deq.append(t)
        # calculate the range for this queue
        self.range = [t - 3000, t]
        while self.deq:
            # check if the front of queue is not falling in the
            # time range, if it does not, then pop the front of queue
            if self.deq[0] < self.range[0]:
                self.deq.popleft()
                continue
            # if the front of queue is falling or equal to front of queue
            # then this si a valid queue and we just return the
            # length of queue
            elif self.deq[0] >= self.range[0]:
                return len(self.deq)


rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))