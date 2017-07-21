class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=range(2,n)
        for i in primes:
            if not i:
                continue
            for j in xrange(i*i,n,i):
                primes[j-2]=0
        return len(primes)-primes.count(0)
