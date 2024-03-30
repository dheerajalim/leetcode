def minDeletionSize(strs) -> int:
    # make a single string from the list
    # get the length of each string and compare with n steps
    # run the loop n times where n == len(string)

    count = 0
    temp_str = ''.join(strs)
    n = len(strs[0])
    i = 0
    start = 0
    while i < n:

        for j in range(start, len(temp_str) - (n), n):
            print(j,j+n)
            print( temp_str[j] , temp_str[j + n])
            if temp_str[j] > temp_str[j + n]:
                count += 1
                break


        start += 1
        i += 1

    return count

strs = ["rrjk","furt","guzm"]
print(minDeletionSize(strs))

# #
# rrjk
# furt
# guzm
