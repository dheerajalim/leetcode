"""
https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2024-02-18
"""

import heapq


def most_booked(n, meetings):
    # adding the number of rooms to the rooms pq
    rooms_pq = [i for i in range(n)]
    # to store the meeting that are started
    meetings_pq = []
    heapq.heapify(rooms_pq)
    rooms_used = [0] * n

    # sort meetings based on the start time
    sorted_meetings = sorted(meetings)

    for start, end in sorted_meetings:

        # if the prev meetings ends before current meeting
        # start time, then we make the rooms available
        while meetings_pq and meetings_pq[0][0] <= start:
            _, room = heapq.heappop(meetings_pq)
            heapq.heappush(rooms_pq, room)

        # if the rooms are available, we assign the
        # meetings to those rooms
        if rooms_pq:
            room = heapq.heappop(rooms_pq)
            heapq.heappush(meetings_pq, [end, room])

        # if the rooms are not available
        # since are meetings are sorted, we wait for the previous meetings
        # to end ( they will end after the current meeting start time, therefore
        # we need to wait), then we update the end time of the new meeting by the difference
        # of time it started late and assign a room to it and add it to min heap
        else:
            current_end, room = heapq.heappop(meetings_pq)
            new_end = current_end + end - start
            heapq.heappush(meetings_pq, [new_end, room])

        # we increment the count of the room used in each iteration
        rooms_used[room] += 1

    return rooms_used.index(max(rooms_used))


n = 3
meetings = [[1, 20], [2, 10], [3, 5], [14, 19]]
# n = 3
# meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
# n = 2
# meetings = [[0,10],[1,5],[2,7],[3,4]]
# n = 2
# meetings = [[0,10],[1,2],[12,14],[13,15]]
n = 4
meetings = [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]
# n= 2
# meetings = [[0,20], [1,2], [7,10]]
n = 1
meetings = [[7, 15], [13, 18], [14, 20], [0, 6]]
# n = 4
# meetings = [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]


print(most_booked(n, meetings))
