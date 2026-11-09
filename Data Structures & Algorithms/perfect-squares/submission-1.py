from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        def isPrime(n):
            if n<=3: return True
            if n%2 == 0 or n%3 == 0: return False
            i=5
            while i*i<=n:
                if n%i == 0 or n%(i+2) == 0:
                    return False
                i+=6
            return True

        def solve(a, i, target):
            if target == 0: return 0
            if i == len(a): return float('inf')

            nottake = solve(a, i+1, target)
            take = float('inf')
            if target - a[i] >=0:
                take = 1 + solve(a, i, target-a[i])
            return min(nottake, take)
            
        
        primes = [1,4,9]
        i=4
        while primes[-1] < n:
            primes.append(i*i)
            i+=1
        
        print(primes)
        #return solve(primes, 0, n)

        dp = [[float('inf') for j in range(n+1)] for i in range(len(primes)+1)]

        for i in range(len(primes)+1):
            dp[i][0] = 0
        
        for i in range(len(primes)-1, -1, -1):
            for j in range(1,n+1):
                if j-primes[i] >= 0:
                    dp[i][j] = min(dp[i+1][j], 1+ dp[i][j-primes[i]])
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][n]
