class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ''
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(1, len(word)+1):
            string = word[:i]
            if string in node.children:
                node = node.children[string]
            else:
                newNode = TrieNode()
                node.children[string] = newNode
                node = newNode
        node.val = word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range(1, len(word)+1):
            string = word[:i]
            if string not in node.children:
                return False
            node = node.children[string]
        return node.val == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range(1, len(prefix)+1):
            string = prefix[:i]
            if string not in node.children:
                return False
            node = node.children[string]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
