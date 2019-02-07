# manacher's algorithm is used to find the longest palindrome in a string

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    dp = [1] * len(s)
    center = 1
    for i in range(len(s)):
        if dp[center] + center > i:
            dp[i] = min(dp[2 * center - i], dp[center] + center - i)
        while i - dp[i] >= 0 and i + dp[i] < len(dp) and \
            s[i - dp[i]] == s[i + dp[i]]:
            dp[i] += 1

        if dp[i] > dp[center]:
            center = i
    return s[dp[center] - center + 2:dp[center] + center:2]



# this is an extension, number of palindrome in a string
def palindromeSubStrs(s):
    m = dict()
    n = len(s)
    dp = [[0] *(n+1) for _ in range(2)]
    s = '#' + s + '#'
    for j in range(2):
        rp = 0 # palindrome radius
        dp[j][0] = 0
        i = 1
        while i <= n:
            while s[i - rp - 1] == s[i + j + rp]:
                rp += 1

            dp[j][i] = rp
            k = 1
            while dp[j][i-k] != rp - k and k < rp:
                dp[j][i + k] = min(dp[j][i-k], rp - k)
                k += 1

            rp = max(rp - k, 0)
            i += k
    s = s[1:len(s) - 1]
    m[s[0]] = 1
    for i in range(1, n):
        for j in range(2):
            for rp in range(dp[j][i], 0, -1):
                m[s[i-rp - 1:i-rp-1+2*rp +j]] = 1
        m[s[i]] = 1

    for i in m:
        print i


s = "abaaa"
palindromeSubStrs(s)
