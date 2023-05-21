'''
example
Input = []
Output = [[]]
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
    result = [0]

    for i in input_num:
        temp_result = len(result)
        for item in range(temp_result):
            result.append(result[item] ^ i)
        output +=[lst+[i] for lst in output]


    return sum(result)

input_num = [3,4,5,6,7,8]
print(all_subset(input_num))
