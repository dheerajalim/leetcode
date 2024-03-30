def n_meetings(n, start, end):
    meetings = zip(start, end)
    meetings = sorted(meetings, key=lambda x: x[1])

    result = 1
    taken_start, taken_end = meetings[0][0], meetings[0][1]
    for start, end in meetings[1:]:

        if start > taken_end:
            taken_start, taken_end = start, end
            result += 1

    return result


n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

print(n_meetings(n, start, end))
