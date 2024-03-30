def insert_interval(intervals, new_interval):
    new_start, new_end = new_interval

    result = []
    i = 0
    for start_i, end_i in intervals:

        if end_i < new_start:
            result.append([start_i, end_i])

        elif start_i > new_end:
            break

        else:
            new_interval = [min(start_i, new_interval[0]), max(end_i, new_interval[1])]

        i += 1


    result.append(new_interval)
    result.extend(intervals[i:])
    return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

print(insert_interval(intervals, newInterval))
