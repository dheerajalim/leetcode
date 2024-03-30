"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# this is similar to non overlapping intervals question
"""


def min_arrow_shots(points):
    # sort based on the x dimension
    points = sorted(points)

    prev_start, prev_end = points[0][0], points[0][1]

    n = len(points)
    overlap_count = 0

    i = 1

    while i < n:

        if prev_end < points[i][0]:
            prev_start, prev_end = points[i][0], points[i][1]

        elif prev_end >= points[i][0]:
            overlap_count += 1
            prev_end = min(prev_end, points[i][1])

        i += 1

    return n - overlap_count


points = [[10, 16], [2, 8], [1, 6], [7, 12]]

print(min_arrow_shots(points))
