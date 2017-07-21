class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        secretHash = {i:v for (i,v) in enumerate(secret)}
        guessHash = {i:v for (i,v) in enumerate(guess)}
        secretKey = {v:0 for v in secret}
        for i in range(0, len(secret)):
            secretKey[secret[i]] += 1

        for i in range(0, len(secret)):
            if guessHash[i] == secretHash[i]:
                secretKey[guessHash[i]] -= 1
                guessHash[i] = "#"
                bull += 1
        for i in range(0, len(secret)):
            if guessHash[i] == "#":
                continue
            if guessHash[i] in secretKey and secretKey[guessHash[i]] > 0:
                secretKey[guessHash[i]] -= 1
                cow += 1
        return str(bull) + 'A' + str(cow) + 'B'


mytest = Solution()
s = "1122"
g = "1222"
print mytest.getHint(s, g)
