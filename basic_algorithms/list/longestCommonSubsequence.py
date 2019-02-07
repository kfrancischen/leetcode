def longestCommonSubstring(s, t, m, n):
    if m == 0 or n == 0:
        return 0
    elif s[m-1] == t[n-1]:
        return 1 + longestCommonSubstring(s, t, m-1, n-1)
    else:
        return max(longestCommonSubstring(s, t, m, n-1), longestCommonSubstring(s, t, m-1, n))


s = "abcde"
t = "fbcdg"
print longestCommonSubstring(s, t, len(s), len(t))
