class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        maxIdx = 0
        if not gas or not cost:
            reutrn -1
        total = 0
        sumRemain = 0
        diff = 0
        for i in range(0, len(gas)):
            diff = gas[i] - cost[i]
            sumRemain += diff
            if sumRemain < 0:
                maxIdx = i + 1
                sumRemain = 0
            total += diff

        return -1 if total < 0 else maxIdx
