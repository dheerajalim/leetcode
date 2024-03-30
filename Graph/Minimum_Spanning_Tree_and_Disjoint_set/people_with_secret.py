### Better solution :
# https://leetcode.com/problems/find-all-people-with-secret/solutions/4773980/python3-heap/?envType=daily-question&envId=2024-02-24
# from disjoint_set_by_rank import *
import heapq


class Disjoint:

    def __init__(self, n: int):
        # the number of vertices
        self.n = n
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):

        # if the ultimate parent is same then they are already connected
        up_u = self.find_uparent(u)
        up_v = self.find_uparent(v)

        if up_u == up_v:
            return

        else:
            # modification in the union operation here,
            # if one of the parent is 0, then we always make it the parent of other, so that
            # we always have 0 as the highest ranked node

            if up_u == 0:
                self.parent[up_v] = up_u
                self.rank[up_u] += 1
                return
            elif up_v == 0:
                self.parent[up_u] = up_v
                self.rank[up_v] += 1
                return

            # if rank of ultimate parent of u is less than ultimate parent of v,
            # then update the up_u as up_v, and no need to increment
            # rank as up_v is already higher rank
            if self.rank[up_u] < self.rank[up_v]:
                self.parent[up_u] = up_v

            # similar case as above just the up_u has higher rank than up_v
            elif self.rank[up_v] < self.rank[up_u]:
                self.parent[up_v] = up_u

            elif self.rank[up_v] == self.rank[up_u]:
                # in this case we can attach anyone to anyone
                self.parent[up_v] = up_u
                self.rank[up_u] += 1


def find_people(n, meetings, first_person):
    # we will recreate the meetings input
    meetings_recreated = dict()

    # based on time, the key is time and the value is list of people [[x,y],[a,b]]
    # this is done to have all people at same time together
    for x, y, t in meetings:

        if meetings_recreated.get(t):
            meetings_recreated[t].append([x, y])
        else:
            meetings_recreated[t] = [[x, y]]

    # a min heap, so that we always get the nearest time meeting first
    # this stores : [time, [list of people in meeting at this time]
    meetings_pq = []
    for time, person in meetings_recreated.items():
        heapq.heappush(meetings_pq, [time, person])

    disjoint = Disjoint(n)

    # create an edge between the 0th and the first person , as 0 will for sure share
    # the secret with the first person
    disjoint.union_by_rank(0, first_person)
    # add 0 and first person to secret set as they will for sure know the secret now
    secret_people = set([0, first_person])

    while meetings_pq:
        # get the meeting that is the nearest by poping from min heap
        time, person = heapq.heappop(meetings_pq)

        # multiple meetings on same time: we have to reset the parent and rank if that edge formed
        # does not have any person involved who knows the secret
        if len(person) > 1:
            # connect all the person nodes, this is done because a set of people
            # if joined first might not have person who knows secret but there is a person on same time
            # who knows the secret having meeting, what if this person meets the other set of people in meeting
            # as these all meetings are happening at same time
            for u, v in person:
                disjoint.union_by_rank(u, v)

            for u, v in person:
                up_u = disjoint.find_uparent(u)
                up_v = disjoint.find_uparent(v)
                # if the ultimate parent contains 0, that means this person know the secret
                # as 0 is the father of all person in secret
                if up_u == 0 or up_v == 0:
                    secret_people.add(u)
                    secret_people.add(v)
                # else we reset the parent and rank of these people as they have no relation to 0
                else:
                    disjoint.parent[u] = u
                    disjoint.rank[u] = 0
                    disjoint.parent[v] = v
                    disjoint.rank[v] = 0
        # case when we only have one meeting happening at same time
        else:
            u = person[0][0]
            v = person[0][1]
            up_u = disjoint.find_uparent(u)
            up_v = disjoint.find_uparent(v)
            # if they have ultimate parent as 0, then we add them to the secret people list
            # else we ignore these people
            if up_u == 0 or up_v == 0:
                disjoint.union_by_rank(u, v)
                secret_people.add(u)
                secret_people.add(v)
            else:
                continue

    print(secret_people)


n = 4
meetings = [[1, 2, 1], [0, 3, 1], [2, 0, 1]]
firstPerson = 3

find_people(n, meetings, firstPerson)
