class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childrenDic = {}
        self.word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        pointer = self.root
        for i in range(0, len(word)):
            letter = word[:i + 1]
            if letter not in pointer.childrenDic.keys():
                newNode = TrieNode()
                pointer.childrenDic[letter] = newNode
            pointer = pointer.childrenDic[letter]
        pointer.word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pointer = self.root
        for i in range(0, len(word)):
            letter = word[:i + 1]
            if letter not in pointer.childrenDic.keys():
                return False
            pointer = pointer.childrenDic[letter]
        return pointer.word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pointer = self.root
        for i in range(0, len(prefix)):
            letter = prefix[:i + 1]
            if letter not in pointer.childrenDic.keys():
                return False
            pointer = pointer.childrenDic[letter]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.search("somestrin")
print trie.startsWith("some")
