import collections
import heapq


def findAllPeople(n: int, meetings, firstPerson: int):
    q = [(0, 0), (0, firstPerson)]

    graph = collections.defaultdict(list)
    for person_i, person_ii, time in meetings:
        graph[person_i].append((person_ii, time))
        graph[person_ii].append((person_i, time))

    answer = set()
    while q:
        time, person_i = heapq.heappop(q)
        if person_i in answer:
            continue
        answer.add(person_i)
        for person_ii, meeting_time in graph[person_i]:
            if meeting_time >= time:
                heapq.heappush(q, (meeting_time, person_ii))
    return list(answer)


n = 5
meetings = [[3, 4, 2], [2, 3, 2], [1, 2, 1], ]
firstPerson = 1

print(findAllPeople(n, meetings, firstPerson))
