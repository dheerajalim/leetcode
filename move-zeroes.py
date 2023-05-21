'''
Input: nums = [0,1,0,3,2]
Output: [1,3,2,0,0]

if i ==0 and j != 0 then we swap and i ++ j ++
if i ==0 anf j==0 then we j ++

else:
    i ++ j ++
i j
0 1 0 3 2

  i j
1 0 0 3 2

    i   j
1 3 0 0 2
      i
1 3 2 0 0

i  j
1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
   i  j
1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
      i  j
1 ,2 ,0 ,3 ,0 ,4 ,0 ,1
         i  j
1 ,2 ,3 ,0 ,0 ,4 ,0 ,1
         i     j
1 ,2 ,3 ,0 ,0 ,4 ,0 ,1
            i     j
1 ,2 ,3 ,4 ,0 ,0 ,0 ,1

               i     j
1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

'''

def move_zeros(nums):

    n = len(nums)

    if n == 1:
        return nums

    i = 0

    for j in range(1,n):
        if nums[i] == 0 and nums[j] !=0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j +=1

        elif nums[i] == 0 and nums[j] == 0:
            j += 1

        else:
            i += 1
            j += 1


nums = [0,1,0,3,12]
nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
nums = [1,2,0,1,0,4,0]
move_zeros(nums)

print(nums)