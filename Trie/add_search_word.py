"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root

        for char in word:
            position = ord(char) - ord('a')

            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()

            node = node.childNode[position]

        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        return self.search_word(word, node)

    def search_word(self, word, node):
        # we iterate over each char of the word
        for j, char in enumerate(word):

            # if the char is not ., then it is starigh forward
            if char != ".":
                position = ord(char) - ord('a')
                if node.childNode[position] is None:
                    return False

                node = node.childNode[position]

            # if the char is a ., then we use recursion
            # we look for all nodes that are not None and then call the remaining
            # word from that node, if we find a word we return True, else we backtrack
            # and start looking for the word starting with another node at same level
            elif char == ".":
                # we check for all the non None nodes
                for i, pos in enumerate(node.childNode):
                    if pos:

                        # since we now want to check  from the next char after .
                        # so we update the word, example : for .ad, we search for ad
                        # as we now stand at node which is pos
                        ##### old logic #####
                        # dot_replacement = chr(ord('a') + i)
                        # new_word = dot_replacement + word[j + 1:]
                        # if self.search_word(new_word, node):
                        #     return True
                        ##### old logic#####

                        # then we start looking for the word agead of .
                        # example if we have '.ad', then new word is 'ad',
                        # since for . we are iterating through each pos and checking if the remaining
                        # word can be found
                        new_word = word[j + 1:]
                        # if the word is found, we return True
                        if self.search_word(new_word, pos):
                            return True

                # even after all possible tries to find the word, we cannot find it we return False
                return False

        return node.is_end_of_word


obj = WordDictionary()

words = ["bad", "dad", "mad", "pad"]
words = ["a", "a"]
for x in words:
    obj.add_word(x)

print(obj.search(".a"))
