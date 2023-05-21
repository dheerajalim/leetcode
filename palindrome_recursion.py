
def find_palindrome(input_str, start, end):

    if start > end or start == end :
        return True

    if input_str[start] != input_str[end]:
        return False

    if input_str[start] == input_str[end]:
        start += 1
        end -= 1
        return find_palindrome(input_str,start, end)


test_input ='pp'

print(find_palindrome(test_input,0,len(test_input)-1))



