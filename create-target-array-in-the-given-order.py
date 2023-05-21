
def createTargetArray(nums, index) :
    result_dict = dict()
    output = list()
    for i, j in zip(nums, index):

        if result_dict.get(j):
            result_dict[j].insert(0, i)
        else:
            result_dict[j] = [i]

    sorted_dict = sorted(result_dict)
    print(sorted_dict)
    for index in sorted_dict:
        output.extend(result_dict[index])


    return output

nums =[4,2,4,3,2]
index =[0,0,1,3,1]

createTargetArray(nums, index)


