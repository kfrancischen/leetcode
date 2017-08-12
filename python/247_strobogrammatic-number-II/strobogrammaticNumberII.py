class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        nums = {'1':'1', '6':'9', '8':'8', '0':'0', '9':'6'}
        if n == 1:
            return ['1', '0', '8']
        mid = n / 2
        
        result = ['1', '6', '8', '9']
        count = len(result)
        for i in range(1, mid):
            while count > 0:
                val = result.pop(0)
                count -= 1
                for key in nums.keys():
                    result.append(val + key)
            count = len(result)
        if n % 2 == 1:
            while count > 0:
                val = result.pop(0)
                count -= 1
                for key in ['1', '0', '8']:
                    result.append(val + key)
                    
        count = len(result)
        while count > 0:
            val = result.pop(0)
            count -= 1
            for i in range(mid-1, -1, -1):
                val += nums[val[i]]
            result.append(val)
        return result