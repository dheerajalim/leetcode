def backtracking(requests, idx, buildings, count, result):
    if idx >= len(requests):
        all_zero = True
        for i in buildings:
            if i != 0:
                all_zero = False
                break
        if all_zero:
            result[0] = max(result[0], count)

        return

    from_building = requests[idx][0]
    to_building = requests[idx][1]

    buildings[from_building] -= 1
    buildings[to_building] += 1
    backtracking(requests, idx + 1, buildings, count + 1, result)

    buildings[from_building] += 1
    buildings[to_building] -= 1
    backtracking(requests, idx + 1, buildings, count, result)


def max_request(n, requests):
    count = 0
    result = [float('-inf')]
    buildings = [0] * n
    backtracking(requests, 0, buildings, count, result)

    return result[0]


n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]

# n = 3
# requests = [[0, 0], [1, 2], [2, 1]]

print(max_request(n, requests))
