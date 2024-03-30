def find_content_child_count(g, s):
    # sort the greed of the children and the cookie size
    # the idea is to satisfy the children with max greed first if we have
    # a valid cookie for him
    g = sorted(g)
    s = sorted(s)
    # to ge the count of children that are satisfied
    count = 0
    # initial index of both the child and cookie
    si, gi = 0, 0
    # iterate until both the list have items
    while gi < len(g) and si < len(s):
        # if the cookie is big enough to satisfy the child
        # we move to the next cookie and child and increment the count
        if s[si] >= g[gi]:
            si += 1
            gi += 1
            count += 1
        # else this means that the cookie was not big
        # enough to satisfy the child, hence we move to the next cookie
        # as the cookie we are at cannot satisfy the child with least requirement
        # there is a possibility that the next cookie can satisfy the child
        else:
            si += 1

    return count
