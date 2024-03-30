'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
def check_palindrome(arr, si, ei):

    if si > ei:
        return True

    if arr[si] != arr[ei]:
        return False

    return check_palindrome(arr, si+1, ei-1)

arr ="A man, a plan, a canal: Panama"
arr = arr.lower()
arr_alpha = ""
for i in arr:
    if i.isalnum():
        arr_alpha += i
print(arr_alpha)
print(check_palindrome(arr_alpha,0,len(arr_alpha)-1))



