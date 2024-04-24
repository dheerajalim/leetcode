"""
https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-04-22
"""

from collections import deque


def open_lock(dead_ends, target):
    dq = deque()
    dq.append("0000")
    level = 0

    dead_ends = set(dead_ends)

    # for ege case where the starting combination is already in dead ends
    if "0000" in dead_ends:
        return -1

        # dead_ends.add("0000")
    while dq:
        size = len(dq)

        for _ in range(size):

            current_lock = dq.popleft()

            if current_lock == target:
                return level

            for i in range(4):
                clockwise = int(current_lock[i]) + 1 if int(current_lock[i]) < 9 else "0"
                anti_clockwise = int(current_lock[i]) - 1 if int(current_lock[i]) > 0 else "9"

                clockwise_lock = current_lock[0: i] + str(clockwise) + current_lock[i + 1:]
                anti_clockwise_lock = current_lock[0: i] + str(anti_clockwise) + current_lock[i + 1:]

                if clockwise_lock not in dead_ends:
                    dq.append(clockwise_lock)
                    dead_ends.add(clockwise_lock)
                if anti_clockwise_lock not in dead_ends:
                    dq.append(anti_clockwise_lock)
                    dead_ends.add(anti_clockwise_lock)


        level += 1

    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

# deadends = ["8888"]
# target = "0009"
#
#
# deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
# target = "8888"
from time import time
start = time()
print(open_lock(deadends, target))
end = time() -start
print(end)