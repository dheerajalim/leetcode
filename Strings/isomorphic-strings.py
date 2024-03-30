"""
https://leetcode.com/problems/isomorphic-strings/

"""

def isomorphic(s , t):

    # this is the main condition to remeber as if the lengths are not equal , that means one char maps to more than one
    if len(set(s)) != len(set(t)):
        return False

    temp_dict = dict()

    for char in range(len(s)):

        if not temp_dict.get(s[char]):
            temp_dict[s[char]] = t[char]
        if temp_dict[s[char]] != t[char]:
            return False

    return True


s = "egg"
t = "add"

# s = "foo"
# t = "bar"

# s = "paper"
# t = "title"

s ="badc"
t = "baba"
print(isomorphic(s, t))


