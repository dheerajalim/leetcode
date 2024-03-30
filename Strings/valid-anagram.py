"""
https://leetcode.com/problems/valid-anagram/description/

"""
from datetime import datetime
datetime.now().isoformat()
def anagram(s, t):

    # Solution 1:
    """
    s = "".join(sorted(s))
    t = "".join(sorted(t))

    return s==t
    """

    # Solution 2:
    """
    if len(s) != len(t):
        return False

    dict_s , dict_t = {}, {}

    for i, j in zip(s,t):

        if dict_s.get(i):
            dict_s[i] += 1
        else:
            dict_s[i] = 1

        if dict_t.get(j):
            dict_t[j] += 1
        else:
            dict_t[j] = 1

    for k, v in dict_s.items():

        if dict_t.get(k) and dict_t[k] == v:
            continue
        else:
            return False

    return True
    """

    # Solutin 3: Using single Dict, if we encounter the key in t then -1 from dict of s

    temp_dict = {}

    for i in s:

        if temp_dict.get(i):
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    for j in t:
        if temp_dict.get(j):
            temp_dict[j] -= 1
            if temp_dict[j] < 0 :
                return False

        else:
            return False

    return sum(temp_dict.values()) == 0


s = "anagram"
t = "nagaram"

# s = "rat"
# t = "car"
print(anagram(s,t))