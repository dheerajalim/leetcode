"""
Since TOPO sort is only valid for DAG, hence we use it to check
if the directed graph is cyclic or acyclic

If the indegree of all items become 0, then this is acyclice
else cyclic
"""

from collections import deque


def create_adj_matrix(numCourses, prerequisites):
    adj_matrix = [[] for _ in range(numCourses)]
    # since for pait (u,v), v needs to be completed before u
    # it is and edge from v ---> u
    for i in prerequisites:
        adj_matrix[i[1]].append(i[0])

    return adj_matrix


def get_indegree(adj_matrix):
    indegree_list = [0] * len(adj_matrix)

    for nodes in adj_matrix:
        for node in nodes:
            indegree_list[node] += 1

    return indegree_list


def can_finish_all_courses(num_courses, prerequisites):

    # create adj matrix:
    adj = create_adj_matrix(num_courses, prerequisites)

    # get the indegree of each node , pass the adj matrix
    # this will help to get the indegree
    indegree_list = get_indegree(adj)

    # adding the 0 indegree nodes to queue
    # finding the nodes with 0 indegree and pushing them to queue
    # as they are the starting point of topo sort
    dq = deque()

    for i in range(len(indegree_list)):
        if indegree_list[i] == 0:
            dq.append(i)

    # to keep track of all the items that we pop out from queue
    # this is basically the nodes whose in-degree became 0
    count = 0
    # now dq will have all nodes that have 0 in degree
    while dq:
        # take the left item from queue and print
        current_node = dq.popleft()
        # update count by 1 after each pop action
        count += 1
        # now we will reduce the indegree for all the connected nodes
        # if the indegree becomes 0, then append it to the queue
        for node in adj[current_node]:
            indegree_list[node] -= 1
            if indegree_list[node] == 0:
                dq.append(node)

    # if all the nodes were able to get indegree 0, then
    # we return TRUE else we return FALSE
    # this means if count == num_courses: can finish all courses
    return count == num_courses


numCourses = 2
prerequisites = [[1, 0]]
prerequisites = []

print(can_finish_all_courses(numCourses, prerequisites))
