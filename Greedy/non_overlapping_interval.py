def remove_overlapping_intervals(intervals):
    # to store the result
    overlap_count = 0
    # sorting basd on start time
    intervals = sorted(intervals)
    # storing the first interval for comparison purpose
    prev_start, prev_end = intervals[0]
    n = len(intervals)

    i = 1
    # starting from the second index to help compare the overlapping intervals
    while i < n:
        # if the prev end time <= curr start time, means no overal
        # , so we update the prev to the curr interval
        if prev_end <= intervals[i][0]:

            prev_start, prev_end = intervals[i][0], intervals[i][1]

        # if the prev end time > current start time , this means its a overall
        # now our end time will be the once which is min of prev and curr
        # as we want to take smaller interval to avoid further overlapping
        # and the start time is going to be smaller anyways as prev_start
        # is anyways pointing to smaller start time as the array is sorted
        elif prev_end > intervals[1][0]:
            # this is overlapping interval, hence increment the counter
            overlap_count += 1
            # prev_start = min(prev_start, intervals[i][0]) # added earlier byt realise it will always be the smaller
            prev_end = min(prev_end, intervals[i][1])

        i += 1

    return overlap_count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals = [[1, 2], [1, 2], [1, 2]]
intervals = [[1, 2], [2, 3]]
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]

remove_overlapping_intervals(intervals)
