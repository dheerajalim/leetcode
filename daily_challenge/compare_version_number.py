"""
https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2024-05-03
"""


def compare_version(version1: str, version2: str) -> int:
    # split the versions into lists of integers
    version1 = [int(item) for item in version1.split('.')]
    version2 = [int(item) for item in version2.split('.')]

    # making the lenngth of both the versions same
    len_v1, len_v2 = len(version1), len(version2)
    if len_v1 > len_v2:
        for _ in range(len_v1 - len_v2):
            version2.append(0)

    elif len_v2 > len_v1:
        for _ in range(len_v2 - len_v1):
            version1.append(0)

    # iterate over the versions and compare them
    for i in range(len(version1)):
        # if at any point we find a greate value in any version
        # we return
        if version1[i] > version2[i]:
            return 1
        if version1[i] < version2[i]:
            return -1
    return 0


version1 = "1.0"
version2 = "1.0.0"

print(compare_version(version1, version2))