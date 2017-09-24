class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            word = words[i]
            col_word = ''
            for j in range(len(words)):
                if len(words[j]) > i:
                    col_word += words[j][i]

            if word != col_word:
                return False
            
        return True