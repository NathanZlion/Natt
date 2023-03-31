class Solution:
    def countPrimes(self, n: int) -> int:
        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime
        
        if n < 3:
            return 0

        count = 0
        primes = prime_sieve(n-1)

        for prime in primes:
            if prime:
                count += 1
        
        return count
    
    
