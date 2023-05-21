def percentageLetter(s: str, letter: str) -> int:
    total_len = len(s)
    count = 0
    for i in s:
        if i == letter:
            count += 1

    return (count *100 // total_len)

s = "foobar"
l = "o"
print(percentageLetter(s, l))