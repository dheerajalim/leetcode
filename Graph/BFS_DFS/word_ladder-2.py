"""

Reference : https://sewb.dev/posts/leetcode-126:-word-ladder-ii-solution-cl230435f0005kgrucypyfrj7
"""
from collections import deque


def word_ladder_2(begin_word, end_word, wordlist):
    # if the end word is not in wordlist, then we can never find it
    if end_word not in wordlist:
        return []

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
    # add begin_word as source to BFS and a list of its parent path
    dq.append([begin_word, []])

    # add this to already visited
    visited.add(begin_word)

    # list for the shortest possible sequence
    result = []

    while dq:
        # since we are maintaining each level, hence we will
        # keep a sepearate visiting set for each level of the BFS
        # and update it after all the items in one level are visited
        """
        So for example, we can go from hit -> hot -> pot as well as from hit -> pit -> pot. 
        We need to capture both instances because we arrived at the destination pot through 
        different routes but in the same number of steps. Both are valid sequences, 
        and must be included in the solution.
        """
        visiting = set()
        # we loop through all the current items in the queue
        # after that increment the word_count as we are considering
        # all word changes at same level as 1 possible path
        size = len(dq)
        for _ in range(size):
            # get the current word from queue
            current_word, path_to_word = dq.popleft()
            # if this word is equal to end word; updated result
            # append the result list with the current path to word
            # since we are at the end word, append
            # that end word to the path to word as well
            if current_word == end_word:

                path_to_word.append(end_word)
                result.append(path_to_word)
                continue

            # else generate pattern for this word
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1:]
                # look for all possible words in that pattern
                # if those words are not visited , mark them visited
                # and add to queue, this is BFS happening
                for word in pattern_map[pattern]:
                    if word not in visited:
                        # update the path to the word by appending the parent to path
                        path_to_word.append(current_word)
                        # add the child word to the queue
                        # along with update path to the queue for child
                        dq.append([word, path_to_word.copy()])
                        # update the visiting set with current level words
                        visiting.add(word)
                        # once if the path is updated , remove that parent
                        # from path_to_word as now on same level we will update
                        # the parent path for next node
                        path_to_word.pop()

        # update the global visisted
        visited = visited.union(visiting)
        # after clearing all the words in one level
        # we update increment word count as per BFS
        # we are considering each level as single incerement
        # if len(dq): word_count += 1

    return result


begin_word = "hit"
end_word = "cog"
# wordlist = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
wordlist = ["hot","dot","dog","lot","log","cog"]

print(word_ladder_2(begin_word, end_word, wordlist))
