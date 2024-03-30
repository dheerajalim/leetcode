
count = 0

def check_move_time(start, end):
    global count
    move = abs(ord(start) - ord(end))

    check_move = abs(26 - move)

    if check_move < move:
        move = check_move

    count += move


def minTimeToType(word: str) -> int:
    # calculate the abs diffeence between characters
    # subtract it from 26 to know the possible direction for shortest distance clock or anticlock
    # Finnaly add the len(word) which is the 1 sec to print the word

    # the initial pointer is at a , so we need to move from a to first word character

    check_move_time('a', word[0])

    for i in range(len(word) - 1):
        check_move_time(word[i], word[i + 1])

    return count + len(word)

word = "bza"

print(minTimeToType(word))