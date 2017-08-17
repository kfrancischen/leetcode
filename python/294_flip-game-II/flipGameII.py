class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo={}
        def can(piles):
            piles=tuple(sorted(p for p in piles if p>=2))
            if not piles in memo:
                memo[piles]=any(not can(piles[:i]+(j, pile-2-j)+piles[i+1:]) 
                                    for i, pile in enumerate(piles) 
                                        for j in range(pile/2))
            return memo[piles]
        return can(map(len, re.findall(r'\++', s)))