def min_platform(arr, dep):
    # arr_dep = zip(arr, dep)
    #
    # arr_dep = sorted(arr_dep, key = lambda x : x [1])
    # print(arr_dep)
    # platform = 1
    # max_platform = 1
    # last_arr, last_dep = arr_dep[0]

    # for arr, dep in arr_dep[1:]:
    #
    #     if arr <= last_dep:
    #         platform += 1
    #
    #
    #     else:
    #         max_platform = max(max_platform, platform)
    #         platform = 1
    #
    #     last_arr, last_dep = arr, dep
    #
    # return max_platform

    arr.sort()
    dep.sort()

    platform_count = 1
    max_platform = 1

    arr_i, dep_j = 1, 0
    while arr_i < len(arr) and dep_j < len(dep):

        if arr[arr_i] <= dep[dep_j]:
            platform_count += 1
            arr_i += 1

        else:

            platform_count -= 1
            dep_j += 1

        max_platform = max(max_platform, platform_count)

    return max_platform


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

# arr = [1020, 1200]
# dep = [1050, 1230]

print(min_platform(arr, dep))
