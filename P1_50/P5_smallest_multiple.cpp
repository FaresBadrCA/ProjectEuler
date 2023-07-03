/*
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
k = 20
Let N be the answer to the problem.

Let P[i] be the ith prime number

N = sum ( P[i]^a[i] ) be the prime factorization of N

a[i] is the highest power of P[i] which is less than or equal to k. 
therefore, p[i] ^ a[i] <= k
so a[i] * log( p[i] ) <= log(k)
a[i] <= log(k) / log(p[i])
a[i] = floor ( log(k) / log(p[i]) )

Question: which prime numbers should we consider?
Answer: Using the fact that for primes less than k where p[i]^2 > k, a[i] = 1
so we only calculate a[i] for primes less than sqrt(k)
*/

#include <iostream>
#include <vector>
#include "math.h"
#include "math_utility.hpp"

int main() { 
	uint64_t k = 20;
	uint64_t sqrt_k = floor(sqrt(k));
	double log_k = log(k);

	std::vector<uint64_t> primes = primes_less_than_n( k + 1 );

	uint64_t N = 1; // desired result: number divisible by all integers frmo 1 to k.
	int i = 0;
	// for primes less than sqrt(k) we have to calculate the powers of each prime factor
	for (i = 0; primes[i] <= sqrt_k; ++i) {
		N *= pow(primes[i], floor(log_k / log(primes[i])));
	}
	
	// for primes after sqrt(k), their power is just 1
	for (; i < primes.size(); ++i) {
		N *= primes[i];
	}

	std::cout << N << "\n";

}

