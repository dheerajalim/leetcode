class TrieNode:

    def __init__(self):
        self.childNode = [None] * 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> int:

        node = self.root
        distinct_count = 0
        for char in word:

            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()
                # whenever a new character is added we will increment this count
                distinct_count += 1

            node = node.childNode[position]

        return distinct_count


def count_distinct_substring(word):
    trie = Trie()

    i = 0
    total_distinct_count = 0
    # we iterate the word from start to end
    # where we keep on remvoving the intital character
    # from the word example : abab > bab > ab > b
    while i < len(word):
        # this will give the distinct substring count
        distinct_count = trie.insert(word[i:])
        # calculate the total count of distinct substring
        total_distinct_count += distinct_count
        # we then keep on moving to the next character in the input string
        # to find all possible substrings
        i += 1

    # the +1 is done to consider the empty string as well
    return total_distinct_count + 1


# word = "abab"
word = "abc"

# output is 8 : ["", "a", "ab", "aba", "abab", "b", "ba", "bab"]
print(count_distinct_substring(word))
