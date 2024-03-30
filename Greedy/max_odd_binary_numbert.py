"""
https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01


The idea is to have one count of "1" at the last position
and the remoining "1" at the front positon and all the "0" in between
This way the last "1" ensures that the string is odd
and the initial "1" assure that the string is max number
"""


def maximumOddBinaryNumber(s: str) -> str:
    # solution 1: Using sorting
    """
    str_list = list(sorted(s, reverse = True))
    pos = str_list.count('1') - 1
    str_list[pos], str_list[-1] = str_list[-1], str_list[pos]

    return "".join(str_list)
    """

    # Solution 2 :
    # other solution withoout sorting
    # since we know one 1 has to be at last and rest need to be at the. intiial position
    # so we can recreate the string where (n-1)1's + all 0's + last 1

    ones_count = s.count('1')
    zeros_count = len(s) - ones_count

    return (ones_count - 1) * "1" + zeros_count * "0" + "1"
