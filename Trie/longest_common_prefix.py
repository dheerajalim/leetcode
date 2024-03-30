class TrieNode:

    def __init__(self):
        self.childNode = [None] * 26
        self.is_end_of_word = False
        self.prefix_count = 0


class Trie:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root

        for char in word:

            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()

            node.childNode[position].prefix_count += 1
            node = node.childNode[position]

        node.is_end_of_word = True

    def common_prefix(self, count, word):
        node = self.root
        prefix = ""

        for char in word:
            position = ord(char) - ord('a')

            if node.childNode[position]:
                if node.childNode[position].prefix_count == count:
                    prefix += char
                else:
                    break

            node = node.childNode[position]

        return prefix


def longest_common_prefix(strs) -> str:
    trie_obj = Trie()
    for word in strs:
        trie_obj.insert(word)

    return trie_obj.common_prefix(len(strs), strs[0])


strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))
