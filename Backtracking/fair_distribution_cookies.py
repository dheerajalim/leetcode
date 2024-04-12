def backtracking(cookies, idx, dist, k, result):

    # if we reach the end of cookies, then we have assigned all cookies
    # hence we take the fairness count from current distribution and compare it with result
    if idx >= len(cookies):
        unfairness = max(dist)
        result[0] = min(result[0], unfairness)
        return

    # keep on assigning the cookies to the K kids
    for i in range(k):
        # give the cookie to the ith kid
        dist[i] += cookies[idx]
        # then since the idx cookie is assigned, we recursively call
        # to assign the idx + 1 cookie
        backtracking(cookies, idx + 1, dist, k, result)
        # now after assigning the cookie, we backtrack and take back the assigbed
        # cookie and give it to other child in distribution
        dist[i] -= cookies[idx]
        if dist[i] == 0:
            break


def distribute_cookies(cookies, k):
    # array to store the k childrens cookies allotment
    distribution = [0] * k

    # to get the unfairness value, this is the min of all max distributions
    result = [float('inf')]
    backtracking(cookies, 0, distribution, k, result)

    return result[0]


cookies = [8,15,10]
k = 2
print(distribute_cookies(cookies, k))
