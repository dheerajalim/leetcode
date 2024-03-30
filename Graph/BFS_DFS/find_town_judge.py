"""
https://leetcode.com/problems/find-the-town-judge/description/

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.

Approach :
1. We will find inward and outward degree for each node [in, out]
2. If we find the a node with [n-1, 0] , then this is the town judge
3. As it is mentioned that there is exactly on person who follows both properties
"""


def find_judge(n, trust):

    # case where n is 0
    if len(trust) == 0 or len(trust[0]) == 0:
        return -1

    # valid town judge
    valid_judge = [n-1, 0]
    #[[inward, outward]]
    degree = [[0,0] for _ in range(n+1)]
    for u,v in trust:

        degree[u][1] = degree[u][1] + 1
        degree[v][0] = degree[v][0] + 1

    if valid_judge in degree:
        return degree.index(valid_judge)

    return -1


n = 3
trust = [[1,2],[2,3]]

print(find_judge(n, trust))



