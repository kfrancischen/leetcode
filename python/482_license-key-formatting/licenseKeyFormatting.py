class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        keys = S.replace("-", "").upper()
        result = ''
        keys = keys[::-1]
        if len(keys) < K:
            return keys
        for i in range(len(keys)/K):
            result += '-' + keys[i*K:(i+1)*K]
        if (i+1) * K < len(keys):
            result += '-' + keys[(i+1)*K:]
        result = result[1:]
        return result[::-1]