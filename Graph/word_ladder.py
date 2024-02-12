from collections import deque


def word_ladder(begin_word, end_word, wordlist):
    # if the end word is not in wordlist, then we can never find it
    if end_word not in wordlist:
        return 0

    # create a hash map with key as pattern and all possible words as value
    # example : {h*t : [hit, hot], *og;[dog, log, cog]
    pattern_map = {}

    # visited set to contain words which are already created
    visited = set()

    # since begin word is may not be in wordlist , add it to generate patterns
    if begin_word not in wordlist:
        wordlist.append(begin_word)

    for word in wordlist:
        # generate pattern
        # we get all possible pattern of the word
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            # create a dict for that pattern as key
            # and words associated to that pattern are the values
            if pattern_map.get(pattern):
                pattern_map[pattern].append(word)
            else:
                pattern_map[pattern] = [word]

    # queue to do BFS traversal
    dq = deque()
    # add begin_word as source to BFS
    dq.append(begin_word)

    # add this to already visited
    visited.add(begin_word)

    # the possible count of words from begin to end
    # initialize it to 1 as begin word is already added to queue
    word_count = 1
    while dq:
        # we loop through all the current items in the queue
        # after that increment the word_count as we are considering
        # all word changes at same level as 1 possible path
        size = len(dq)
        for _ in range(size):
            # get the current word from queue
            current_word = dq.popleft()
            # if this word is equal to end word; return the word count
            # that is the count required to reach end word
            if current_word == end_word:
                return word_count

            # else generate pattern for this word
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1:]
                # look for all possible words in that pattern
                # if those words are not visited , mark them visited
                # and add to queue, this is BFS happening
                for word in pattern_map[pattern]:
                    if word not in visited:
                        visited.add(word)
                        dq.append(word)

        # after clearing all the words in one level
        # we update increment word count as per BFS
        # we are considering each level as single incerement
        if len(dq): word_count += 1

    return 0


begin_word = "hit"
end_word = "cog"
wordlist = ["hot","dot","dog","lot","log","cog"]

print(word_ladder(begin_word, end_word, wordlist))
