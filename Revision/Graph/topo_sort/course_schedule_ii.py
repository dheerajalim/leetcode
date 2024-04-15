"""
https://leetcode.com/problems/course-schedule-ii/description/
"""
from collections import deque


def convert_to_adj_list(prerequisites, n):
    adj = [[] for _ in range(n)]

    for i, j in prerequisites:
        adj[j].append(i)

    return adj


def get_in_degree(adj):
    in_degree_count = [0] * len(adj)

    for i in range(len(adj)):

        for node in adj[i]:
            in_degree_count[node] += 1

    return in_degree_count


def find_order(num_courses, prerequisites):
    adj = convert_to_adj_list(prerequisites, num_courses)
    in_degree_count = get_in_degree(adj)

    dq = deque()

    for i in range(len(in_degree_count)):
        if in_degree_count[i] == 0:
            dq.append(i)

    result = []
    while dq:

        source = dq.popleft()
        result.append(source)
        for vertex in adj[source]:

            in_degree_count[vertex] -= 1
            if in_degree_count[vertex] == 0:
                dq.append(vertex)

    return result if len(result) == num_courses else []


numCourses = 2
prerequisites = [[1,0]]

print(find_order(numCourses, prerequisites))