"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""


def dfs(src, dst, graph, path, result):
    path.append(src)

    # base case is that if we reach the destination then we return
    if src == dst:
        # store the copy of the path array inside result
        # else if we pop from path then result will also be updated
        # hence we need a copy
        result.append(path.copy())
        return True

    for node in graph[src]:
        dfs(node, dst, graph, path, result)
        # remove the elements from the path while backtracking
        path.pop()


def all_paths(graph):
    n = len(graph)
    src, dst = 0, n - 1
    path, result = [], []
    dfs(src, dst, graph, path, result)

    return result


graph = [[1, 2], [3], [3], []]
print(all_paths(graph))
