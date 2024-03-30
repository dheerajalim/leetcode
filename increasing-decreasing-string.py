from collections import defaultdict
def sortString(s: str) -> str:

    output_s = ""

    # forst sort the string
    s = sorted(s)
    # need to calculate the occurance of each character in the dictionary

    count_dict = defaultdict()

    for char in s:
        if not count_dict.get(char):
            count_dict[char] = s.count(char)
    i = 0
    while sum(count_dict.values()) != 0:
        temp_output_s = ""
        for key in count_dict.keys():
            if count_dict[key] != 0 :
                temp_output_s += key
                count_dict[key] -= 1
        if i %2 ==1:
            temp_output_s = temp_output_s[::-1]

        output_s += temp_output_s
        i += 1

    print(output_s)









s = "rat"

sortString(s)





