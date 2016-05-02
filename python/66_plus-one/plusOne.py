class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        if len(digits) == 0:
            return [1]
        List = []

        if digits[0] < 9:
            increment = False
            List.append(digits[0] + 1)
        else:
            increment = True
            List.append(digits[0] - 9)

        for i in range(1, len(digits)):
            if increment == False:
                List.append(digits[i])
            else:
                if digits[i] < 9:
                    List.append(digits[i]+1)
                    increment = False
                else:
                    List.append(digits[i] - 9)
                    increment = True
        if increment == True:
            List.append(1)
        List.reverse()
        return List
