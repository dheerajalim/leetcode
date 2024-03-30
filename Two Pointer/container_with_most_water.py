def max_area(height):
    # uses a
    i, j = 0, len(height) - 1

    max_water = 0

    while i < j:

        water = min(height[i], height[j]) * (j - i)
        max_water = max(max_water, water)

        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1

    return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]

print(max_area(height))
