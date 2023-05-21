def freqAlphabets(s: str) -> str:
    list_splitted = []

    for i in range(0, len(s) - 2, 3):
        print(i)
        if s[i + 2] == "#":
            list_splitted.append(s[i] + s[i + 1])
        else:
            list_splitted.append(s[i])
            list_splitted.append(s[i + 1])
    print(i)
    print(list_splitted)

freqAlphabets("10#11#1234")