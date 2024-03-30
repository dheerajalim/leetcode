def two_sum(numbers, target):
    # keeping the pointer at the first and the last
    # position i = 0 th index and j = n-1 index
    i, j = 0, len(numbers) - 1

    # iterate until i < j index
    while i < j:
        # if the sum of numbers at i and j index == target
        # then this is the result
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]

        # if the sum is < target then we need to increase i index as
        # we need greater value to increase value
        if numbers[i] + numbers[j] < target:
            i += 1
        # else if the sum is > target, this means we need smaller
        # value hence we need to move the j index by -1
        else:
            j -= 1

    # since the question assures we wll always have a result
    # hence we are not returning anything explicitly like return None/0


numbers = [-1, 0]
target = -1

print(two_sum(numbers, target))
