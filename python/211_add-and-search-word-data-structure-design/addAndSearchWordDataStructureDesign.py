class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childrenDic = {}
        self.word = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        pointer = self.root
        for letter in word:
            if letter not in pointer.childrenDic.keys():
                newNode = TrieNode()
                pointer.childrenDic[letter] = newNode
            pointer = pointer.childrenDic[letter]
        pointer.word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = [self.root]
        for letter in word:
            subNodes = []
            for node in nodes:
                if letter == '.':
                    subNodes += node.childrenDic.values()
                elif letter in node.childrenDic:
                    subNodes.append(node.childrenDic[letter])
            nodes = subNodes
        for node in nodes:
            if node.word:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("w..")
