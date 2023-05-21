def digitCount(num: str) -> bool:

    for i in range(len(num)):

        if num.count(str(i)) != int(num[i]):
            return False

    return True


x = "5210010007"
y = "0123456789"

print(digitCount(x))