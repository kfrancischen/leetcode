class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children_map = {}
        self.has_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char in node.children_map:
                node = node.children_map[char]
            else:
                new_node = TrieNode(char)
                node.children_map[char] = new_node
                node = new_node

        node.has_word = True

        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = [self.root]
        for char in word:
            child_nodes = []
            for node in nodes:
                if char in node.children_map:
                    child_nodes.append(node.children_map[char])
                if char == '.':
                    for child in node.children_map:
                        child_nodes.append(node.children_map[child])

            nodes = child_nodes

        for node in nodes:
            if node.has_word:
                return True

        return False

                


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)