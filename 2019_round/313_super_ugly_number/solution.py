import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        result = [1]
        heap = [(prime, 0, prime) for prime in primes]
        heapq.heapify(heap)
        for i in range(1, n):
            val, idx, prime = heapq.heappop(heap)
            result.append(val)
            heapq.heappush(heap, (result[idx+1] * prime, idx+1, prime))
            while heap[0][0] <= val:
                _, idx, prime = heapq.heappop(heap)
                heapq.heappush(heap, (result[idx+1] * prime, idx+1, prime))
        return result[-1]



mytest = Solution()
n = 12
primes = [2, 7, 13, 19]
print mytest.nthSuperUglyNumber(n, primes)