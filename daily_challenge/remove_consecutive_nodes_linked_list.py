def linked_list_array(head):
    array = []

    curr = head

    while curr:
        array.append(curr.data)
    return [5,-3,-4,1,6,-2,-5]
    return array

def convert_to_ll(arr):

    head = None
    for i in arr:
        if head is None:
            head = i
            curr = head
        else:
            curr.next = i
            curr = curr.next

    return head
def remove_zero_sum(head):

    # convert linked list to array

    array_ll = linked_list_array(head)

    # iterate the array and store the prefix sum
    hash_map = {}
    prefix_sum = 0

    for i in range(len(array_ll)):

        prefix_sum += array_ll[i]

        if prefix_sum == 0:

            for k, v in hash_map.items():
                if hash_map[k] <= i:
                    hash_map[k] = -1


        elif prefix_sum in hash_map and hash_map[prefix_sum]!=-1:

            start_index = hash_map[prefix_sum]
            for k,v in hash_map.items():
                if hash_map[k] > start_index:
                    hash_map[k] = -1


        else:

            hash_map[prefix_sum] = i
    res = []
    print(hash_map)
    hash_map = sorted(hash_map.items(), key = lambda x : x[1])
    print(hash_map)
    for k,v in hash_map:
        if v != -1:
            res.append(array_ll[v])

    return res
    # head = convert_to_ll(res)
    #
    # return head


print(remove_zero_sum(None))