"""

"""

def rotate_string(s, goal):

    # Solution 1: This O(N^2) because each time we are comparing character by character
    """
    if len(s) != len(goal):
        return False

    if s == goal:
        return True

    for i in range(len(s)):

        if s[i:] + s[0:i] == goal:
            return True

    return False
    """

    # Solution 2 :

    return len(s) == len(goal) and s in goal + goal


s = "abcde"
goal = "cdeab"

s = "abcde"
goal = "abced"

s ="bbbacddceeb"
goal = "ceebbbbacdd"

print(rotate_string(s,goal))