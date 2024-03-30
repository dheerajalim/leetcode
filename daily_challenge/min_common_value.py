"""
TC : O(N + M), we iterate through both the arrays in worst case
Sc : O(1), no extra space is being used

Two pointer approach
"""


def get_common(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)

    i, j = 0, 0
    # iterate both the arrays
    while i < n1 and j < n2:
        # if a match is found, then return
        if nums1[i] == nums2[j]:
            return nums1[i]

        # else increment the pointer which is smaller, as this is decreasing array
        if nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return -1


nums1 = [1, 2, 3, 6, 10, 11]
nums2 = [7, 10]
print(get_common(nums1, nums2))
