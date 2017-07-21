class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = {v:i for i, v in enumerate(stones[2:], 2)}
        if stones[1] != 1:
            return False
        stack = [(1,1)]
        count = 1
        while stack:
            position, jump = stack.pop(0)
            count -= 1
            if position == len(stones) - 1:
                return True
            for d in [-1, 0, 1]:
                if position + jump + d > 0 and position + jump + d in dic:
                    stack.append((dic[position + jump + d], position + jump + d))
                    dic.pop(position + jump + d, None)
            if count == 0 and stack:
                print stack
                count = len(stack)


        return False


mytest = Solution()
stones = [0,1,2,3,5,6,8,10,12]
print mytest.canCross(stones)
