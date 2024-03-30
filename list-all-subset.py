'''
example
Input = [1]
output = [[],[1]]
Input = [1,2]
output = [[],[1], [2],[1,2]] # adding 2 to output of [1]
Input = [1,2,3]
output = [[],[1], [2],[1,2],[3],[1,3],[2,3],[1,2,3]] # adding 3 to output of [1,2]

Therfore for each new number we just add it to the previous list

'''


def all_subset(input_num):

    output = [[]]

    for i in input_num:
        print([lst+[i] for lst in output])
        output +=[lst+[i] for lst in output]

    return output

input_num = [1,2,3]
print(all_subset(input_num))
