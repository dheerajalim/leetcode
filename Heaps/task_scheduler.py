import heapq
from collections import deque


def task_count(tasks):
    counts = {}
    for task in tasks:
        if counts.get(task):
            counts[task] += 1
        else:
            counts[task] = 1

    return list(counts.values())


def task_scheduler(tasks, n):
    dq = deque()
    time = 0

    # calculate the count of each task
    # for max heapify we negate the values
    pq = [-i for i in task_count(tasks)]

    # max heapify
    heapq.heapify(pq)

    # iterate until the heap or queue has some task
    while pq or dq:

        time += 1

        # taking the max count task from the heap
        if pq:
            task_executed = heapq.heappop(pq)

            # to check if the task_executed == 0
            # this makes sure that task is already over
            # we are adding + 1 because are values are negative
            if task_executed + 1:  # this means task_execute != 0
                dq.append([task_executed + 1, time + n])

        # if the time now and dq top has same time
        # we add the task back to queue
        if dq and time == dq[0][1]:
            new_task = dq.popleft()
            # push the new task to heap
            heapq.heappush(pq, new_task[0])

    return time


tasks = ["A", "A", "A", "B", "B", "C", "C"]
tasks = ["A", "A", "A", "B", "B", "B"]

n = 1
n = 2

print(task_scheduler(tasks, n))
