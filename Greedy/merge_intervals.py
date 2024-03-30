def merge_intervals(intervals):
    n = len(intervals)

    # sort the intervals based on the start time
    # as this will help us to get the intervals that merge
    intervals = sorted(intervals)

    # to store the result
    result = []
    # initialize the new_interval with the first interval details
    # this will help us to calculate the comparison with the nex tinterval
    new_interval = intervals[0]
    i = 1
    # start the loop from index i and not 0
    # as we need to compare the interval with new_interval
    # we compare i and i+1 and see if they can be merged
    while i < n:
        # if the end time of prev interval is < start time of current interval
        # this means they do not merge hence we just add the prev interval to result
        # and update the prev interval with new interval
        if new_interval[1] < intervals[i][0]:
            result.append(new_interval)
            new_interval = [intervals[i][0], intervals[i][1]]

        # else if the prev interval end time > cyrrent interval start time
        # that means they overlap, hence we then merge them
        elif new_interval[1] >= intervals[i][0]:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]

        i += 1

    # when we come out of the loop, the new_interval will contain either the last interval
    # or the merge interval, since we do not go to the line 22, hence we append it here in result
    result.append(new_interval)
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 3], [6, 9]]
intervals = [[13, 14], [5, 6], [1, 10], [5, 6], [6, 9]]

print(merge_intervals(intervals))
