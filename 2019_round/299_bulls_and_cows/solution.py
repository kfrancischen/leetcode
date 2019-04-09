class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_cow = 0
        secret_counts, guess_count = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_cow += 1

            if secret[i] in secret_counts:
                secret_counts[secret[i]] += 1
            else:
                secret_counts[secret[i]] = 1

            if guess[i] in guess_count:
                guess_count[guess[i]] += 1
            else:
                guess_count[guess[i]] = 1


        num_overlap = 0
        for key, val in secret_counts.items():
            if key in guess_count:
                num_overlap += min(val, guess_count[key])

        return str(num_cow) + 'A' + str(num_overlap-num_cow) + 'B'


test = Solution()
secret = '1123'
guess = '0111'
print test.getHint(secret, guess)