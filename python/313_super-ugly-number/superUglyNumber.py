import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        if not n or n < 1 or not primes:
            return 0
        res = [1]
        heap = [(prime, 0, prime) for prime in primes]
        heapq.heapify(heap)
        for i in xrange(1, n):
            val, idx, prime = heapq.heappop(heap)
            res.append(val)
            heapq.heappush(heap, (res[idx + 1] * prime, idx + 1, prime))
            while heap[0][0] <= val:
                _, idx, prime = heapq.heappop(heap)
                heapq.heappush(heap, (res[idx + 1] * prime, idx + 1, prime))
        return res[-1]

mytest = Solution()
n = 12
primes = [2, 7, 13, 19]
print mytest.nthSuperUglyNumber(n, primes)
