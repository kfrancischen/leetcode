def KMP(pattern, s):
    m, n = len(pattern), len(s)
    lps = [0] * m
    computeLPS(pattern, m, lps)
    print lps
    i, j = 0, 0
    while i < n:
        if pattern[j] == s[i]:
            i += 1
            j += 1
        if j == m:
            print "pattern found at index " + str(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def computeLPS(pattern, m, lps):
    length = 0 # length of previous longest prefix suffix
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1] # the hardest part
            else:
                lps[i] = 0
                i += 1

s = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMP(pattern ,s)
