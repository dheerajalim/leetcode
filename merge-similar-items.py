def mergeSimilarItems(items1, items2):

    # create a dictionary out of both the items
    # then compare the values and add to create a dictionary sorted in asc order
    # then create the required list of lists structure

    resultant_dict = dict()

    items1.extend(items2)

    for item in items1:

        if resultant_dict.get(item[0]):
            resultant_dict[item[0]] += item[1]
        else:
            resultant_dict[item[0]] = item[1]

    result = [[k,v] for k,v in sorted(resultant_dict.items(), key=lambda x : x[0])]

    return result


items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]

print(mergeSimilarItems(items1, items2))