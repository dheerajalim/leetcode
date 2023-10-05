"""

https://leetcode.com/problems/reverse-words-in-a-string/

"""

def reverse_words(string):

    string_list = string.split()

    return " ".join(string_list[::-1])


s = "a good   example"
s = "  hello world  "
print(reverse_words(s))

# Solution without using Split

def reverse_words_no_split(string):

    "If we find a space then we move otherwise we keep on appending the char to a var"

    temp = ""
    result = []

    for char in string:

        if char != " ":
            temp += char

        elif temp != "":
            result.append(temp)
            temp = ""

    if temp != "" : # edge case for the last word
        result.append(temp)

    return " ".join(result[::-1])

s = "a good   example"
s = "  hello   world  "
print(reverse_words_no_split(s))