"""
Here we need to count the occurance of word as well
"""


class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.end_word, self.prefix_count = 0, 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()

            node.childNode[position].prefix_count += 1

            node = node.childNode[position]

        node.end_word += 1

    def count_word(self, word):

        node = self.root

        for char in word:

            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                return 0

            node = node.childNode[position]

        return node.end_word

    def prefix_count(self, prefix):
        node = self.root

        for char in prefix:

            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                return 0

            node = node.childNode[position]

        return node.prefix_count

    def erase(self, word):

        node = self.root

        for char in word:
            position = ord(char) - ord('a')
            if node.childNode[position]:
                if node.childNode[position].prefix_count:
                    node.childNode[position].prefix_count -= 1

            node = node.childNode[position]
            if node.end_word:
                node.end_word -= 1

obj = Trie()
input_word = "abc"
obj.insert(input_word)
obj.insert(input_word)
obj.insert("abc")

print(obj.count_word(input_word))
print(obj.prefix_count("ab"))
#####
obj.erase(input_word)
print(obj.count_word(input_word))
obj.erase(input_word)
print(obj.count_word(input_word))
obj.erase(input_word)
print(obj.count_word(input_word))


