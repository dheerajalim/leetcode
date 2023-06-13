'''

BS is basically dividing the sorted array into two parts from middle.

Then the element we need to search is compared with the center element, if element > center element : search pn the right else left

This process is repeated untile we find or element


Time complexity: O(log n)

Space complexity : O(1)


'''


def binary_search_recursive(arr, element, start, end):
    if start > end:
        return -1

    middle = (start + end) // 2

    if element == arr[middle]:
        return middle

    if element < arr[middle]:
        return binary_search_recursive(arr, element, start, middle - 1)

    elif element > arr[middle]:
        return binary_search_recursive(arr, element, middle + 1, end)


def binary_search_iterative(arr, element, start, end):
    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == element:
            return middle

        if arr[middle] > element:
            end = middle - 1

        elif arr[middle] < element:
            start = middle + 1

    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [2,3,7,10,13,14,17]
    arr = [-1,0,3,5,9,12]
    element = 9

    print(binary_search_recursive(arr, element, 0, len(arr) - 1))
    print(binary_search_iterative(arr, element, 0, len(arr) - 1))
