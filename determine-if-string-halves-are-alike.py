def halvesAreAlike(s: str) -> bool:
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    mid_str = len(s) // 2

    a = s[:mid_str + 1]
    b = s[mid_str:]

    # need to count vowels in a and b
    count = 0
    # for part_a, part_b in zip(a,b):

    #     if part_a in vowels:
    #         count += 1

    #     if part_b in vowels:
    #         count -= 1

    for part_a in range(0, mid_str):
        if s[part_a] in vowels:
            count += 1

    for part_b in range(mid_str, len(s)):
        if s[part_b] in vowels:
            count -= 1

    return count == 0

print(halvesAreAlike('textbook'))