class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        self.length = [0]
        for i in range(len(strs)):
            self.length.append(self.length[-1] + len(strs[i]))
        return ''.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(self.length) - 1):
            result.append(s[self.length[i]:self.length[i+1]])
        
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))