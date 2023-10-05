"""

https://leetcode.com/problems/largest-odd-number-in-string/


"""

def largestOddNumber(num):

    odd =  {'1','3','5','7','9'} # set for faster iteration

    for i in range(len(num)-1, -1, -1):

        if num[i] in odd:
            return num[:i+1]

    return ""

num = "52"
num = "4206"
num = "35427"

print(largestOddNumber(num))