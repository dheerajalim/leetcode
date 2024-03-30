"""
A string is called a complete string if every prefix of this string is also present in the array
"""


class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:
            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()

            node = node.childNode[position]

        node.is_end_of_word = True


def prefix_exists(trie, word):
    node = trie.root
    for char in word:
        position = ord(char) - ord('a')
        # we check  if the char exists and it is end of the word
        # is_end_of_word = True means that this word exists already in Trie
        # this helps us understand that the prefix exists for the word we are checking
        if node.childNode[position] and node.childNode[position].is_end_of_word:
            node = node.childNode[position]
        # at any point the is_end_of_word = False, that means this prefix is not available
        # hence we return False
        else:
            return False

    return True


def complete_string(arr):
    trie = Trie()
    for word in arr:
        trie.insert(word)

    longest_prefix_word = ""

    for word in arr:
        # we check the prefix_exists
        if prefix_exists(trie, word):
            # if the new word is greater than the longest_prefix_word, then we update the
            # longest_prefix_word to new word
            if len(word) > len(longest_prefix_word):
                longest_prefix_word = word
            # in case both have same length, then we follow the lexicographical order
            # which means if we sort these word, the word at index 0 is our answer
            elif len(word) == len(longest_prefix_word) and word < longest_prefix_word:
                longest_prefix_word = word

    return longest_prefix_word


arr = ['n', 'ni', 'nin', 'ninj', 'ninja', 'ninga']

print(complete_string(arr))
