import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        allSum = []
        result = []
        for val1 in nums1:
            for val2 in nums2:
                if len(allSum) < k:
                    heapq.heappush(allSum, (-val1 - val2, [val1, val2]))
                else:
                    if allSum and -allSum[0][0] > val1 + val2:
                        heapq.heappop(allSum)
                        heapq.heappush(allSum, (-val1 - val2, [val1, val2]))
                    else:
                        break

        for i in range(0, k):
            if not allSum:
                break
            result.append(heapq.heappop(allSum)[1])
        return result

mytest = Solution()
num1 = [-476570184,-423568801,-385585840,-375390924,-364630569,-359795128,-281872968,-126410430,-75677925,-54214495,-49178055,-32637211,-32198215,3413177,19045759,62248526,67551536,113606647,155411580,164755463,164781059,203133270,277305105,284913246,285973110,296436629,325431544,357294459,378678394,399786157]
num2 = [-408663357,-404578641,-376531700,-311642519,-294905976,-232001207,-183530032,-141524508,-115652480,-70696522,-63386299,-54656543,-32316999,29714175,33993996,45020708,62165363,84210823,93905151,102177224,209285622,288668099,328300713,338684779,342861859,384940859,408019604,410097843,458721542,475395296]
k = 1000
print mytest.kSmallestPairs(num1, num2, k)
