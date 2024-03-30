def custom_sort_sting(order, string):
    hash_map = {}
    for i in string:

        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    in_order, in_string = "", ""

    for j in order:
        if j in hash_map:
            in_order = in_order + j * hash_map[j]
            hash_map[j] = 0

    for item, value in hash_map.items():
        if value > 0:
            in_order = in_order + item * value

    return in_order


order = "cba"
s = "abcdadc"

print(custom_sort_sting(order, s))
