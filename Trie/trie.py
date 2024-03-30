class TrieNode:

    def __init__(self):
        self.childNode = [None] * 26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        # whenever an object is created for Trie
        # we create a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # to insert the word in Trie, we refer the root node
        # as this is the starting point
        node = self.root
        # iterate through each character of the word
        for char in word:
            # we get the index of the word
            # the childNode contains 26 items in the list
            # hence we get the index of the word by subtracting from ord('a')
            position = ord(char) - ord('a')
            # if the value at the position of char is None
            # then we insert the new TrieNode there
            # else we just update the node to the node which is present
            # at the char index
            if node.childNode[position] is None:
                node.childNode[position] = TrieNode()

            # update the node to the position of char index
            node = node.childNode[position]

        # the last char is_end_of_word is set to True
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # we get the root node fo the Trie
        node = self.root
        for char in word:
            # get the position index of the char in the childNode
            position = ord(char) - ord('a')
            # if for a char position, it has None
            # that menas this word does not exists
            if node.childNode[position] is None:
                return False
            # otherwise update the node as the node present at char posotion index
            node = node.childNode[position]

        # if we found the word, but it is not the last char of the word
        # then we return False else we return True
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        # similar to the search word
        node = self.root
        for char in prefix:
            position = ord(char) - ord('a')
            if node.childNode[position] is None:
                return False

            node = node.childNode[position]

        # only difference is if we can traverse the prefix copletely without any Node
        # then we return True , we don't check if the last char position is last char
        # or not as we only focus on the prefix existence
        return True

    def delete(self, word: str) -> None:
        # to get the root node
        node = self.root
        # the starting position for the word
        i = 0

        # base case if the root is None
        if node is None:
            return None

        def is_empty(node):
            """
            To check  if the node is empty or not
            that is all the 26 items point to None
            """

            for pos in node.childNode:
                if pos is not None:
                    return False

            return True

        def delete_word(word, node, i):
            # base case, if the len of word == i
            # in that case we have reached the last node of the given word
            if len(word) == i:
                # if the word is the end word , then we mark it as False
                # as we no longer want to consider this word , even if we search
                if node.is_end_of_word:
                    node.is_end_of_word = False

                # then we check if this node has any other child or not
                # if it has no child, then this is the only node and we can delete it , hence we return None
                if is_empty(node):
                    return None

                # otherwise we return the node itself, by marking its end of word as False
                return node

            position = ord(word[i]) - ord('a')
            # to check if the char at position exists
            # before calling recursion
            if node.childNode[position]:
                # recursively call TrieNode at the char position
                node.childNode[position] = delete_word(word, node.childNode[position], i + 1)

            # if the node is completely empty, that is it has no other child
            # and is not the end of word (means it is not forming any other word)
            # then we return None, so that its parent fill the position as None
            if is_empty(node) and node.is_end_of_word is False:
                node = None

            # else we return the node itself, as this may be forming some other word
            return node

        delete_word(word, node, i)


input_word = "and"

obj = Trie()

obj.insert(input_word)
obj.insert("ant")
obj.insert("ant")

# print(obj.search("abc"))
# print(obj.search("ac"))
# print(obj.search("ab"))
# print(obj.starts_with("ab"))
print(obj.search("and"))
print(obj.search("ant"))

obj.delete("and")
print(obj.search("and"))
print(obj.search("ant"))
