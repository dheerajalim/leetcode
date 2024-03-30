def insert_interval(intervals, new_interval):
    new_start, new_end = new_interval[0], new_interval[1]
    # to store the results after inserting new interval
    result = []
    i = 0

    # iterate over all the intervals
    for i, (start, end) in enumerate(intervals):
        # if the end time of given interval is less than new_interval start time
        # this means that the interval and new interval do not merge
        # simple add the interval in the result array
        if end < new_start:
            result.append([start, end])
        # else if the start of the interval is greater than the new interval end
        # this means that this interval do not merge with the new interval
        # hence we break the iteration
        elif start > new_end:
            break

        # otherwise we merge the new and given interval and get the minimum of the start time
        # and max of the end time  intervals
        else:
            new_interval = [min(start, new_interval[0]), max(end, new_interval[1])]

    # append the new interval to the result
    result.append(new_interval)
    # iterate over the remaining intervals and append it to the result
    if i < len(intervals) - 1:
        result.extend(intervals[i:])

    return result


intervals =[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert_interval(intervals, newInterval))
