def fibonnaci(n,start, arr):

    if n < 0 :
        return arr

    if start == 0:
        arr.append(0)

    elif start == 1:
        arr.append(1)

    else:
        arr.append(arr[start-2] + arr[start-1])

    return fibonnaci(n-1, start+1, arr)


print(fibonnaci(6, 0, []))