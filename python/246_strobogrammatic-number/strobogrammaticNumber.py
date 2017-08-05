class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        end = len(num) / 2
        if len(num) % 2 == 1:
            end += 1
        for i in range(end):
            if num[i] not in dic or dic[num[i]] != num[len(num) - 1 - i]:
                return False
            
        return True